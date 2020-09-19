import os
import re
from typing import Optional

import requests
from bs4 import BeautifulSoup, UnicodeDammit
from colorama import init, Fore, Style
from html import unescape
from unidecode import unidecode

from swaglyrics import __version__, unsupported_txt, backend_url, api_timeout, genius_timeout


def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')  # clear command window


# matches braces with feat included or text after -, also adds support for Bollywood songs by matching (From "<words>")
brc = re.compile(r'([(\[](feat|ft|From "[^"]*")[^)\]]*[)\]]|- .*)', re.I)
aln = re.compile(r'[^ \-a-zA-Z0-9]+')  # matches non space or - or alphanumeric characters
spc = re.compile(' *- *| +')  # matches one or more spaces
wth = re.compile(r'(?: *\(with )([^)]+)\)')  # capture text after with
nlt = re.compile(r'[^\x00-\x7F\x80-\xFF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF]')  # match only latin characters,
# built using latin character tables (basic, supplement, extended a,b and extended additional)


def stripper(song: str, artist: str) -> str:
    """
    Generate the url path given the song and artist to format the Genius URL with.
    Strips the song and artist of special characters and unresolved text such as 'feat.' or text within braces.
    Then concatenates both with hyphens replacing the blank spaces.
    Eg.
    >>>stripper('Paradise City', 'Guns n’ Roses')
    >>>'Guns-n-Roses-Paradise-City'
    Which then formats the url to https://genius.com/Guns-n-Roses-Paradise-City-lyrics
    :param song: currently playing song
    :param artist: song artist
    :return: formatted url path
    """
    song = re.sub(brc, '', song).strip()  # remove braces and included text with feat and text after '- '
    ft = wth.search(song)  # find supporting artists if any
    if ft:
        song = song.replace(ft.group(), '')  # remove (with supporting artists) from song
        ar = ft.group(1)  # the supporting artist(s)
        if '&' in ar:  # check if more than one supporting artist and add them to artist
            artist += f'-{ar}'
        else:
            artist += f'-and-{ar}'
    song_data = artist + '-' + song
    # swap some special characters
    url_data = song_data.replace('&', 'and')
    # replace /, !, _ with space to support more songs
    url_data = url_data.replace('/', ' ').replace('!', ' ').replace('_', ' ')
    for ch in ['Ø', 'ø']:
        if ch in url_data:
            url_data = url_data.replace(ch, '')
    url_data = re.sub(nlt, '', url_data)  # remove non-latin characters before unidecode
    url_data = unidecode(url_data)  # convert accents and other diacritics
    url_data = re.sub(aln, '', url_data)  # remove punctuation and other characters
    url_data = re.sub(spc, '-', url_data.strip())  # substitute one or more spaces to -
    return url_data


def get_lyrics(song: str, artist: str) -> Optional[str]:
    """
    Get lyrics from Genius given the song and artist.
    Formats the URL with the stripped url path to fetch the lyrics.
    :param song: currently playing song
    :param artist: song artist
    :return: song lyrics or None if lyrics unavailable
    """
    url_data = stripper(song, artist)  # generate url path using stripper()
    if url_data.startswith('-') or url_data.endswith('-'):
        return None  # url path had either song in non-latin, artist in non-latin, or both
    url = f'https://genius.com/{url_data}-lyrics'  # format the url with the url path
    try:
        page = requests.get(url, timeout=genius_timeout)
        page.raise_for_status()
    except requests.exceptions.HTTPError:
        url_data = requests.get(f'{backend_url}/stripper', data={
            'song': song,
            'artist': artist}, timeout=api_timeout).text
        if not url_data:
            return None
        url = 'https://genius.com/{}-lyrics'.format(url_data)
        page = requests.get(url, timeout=genius_timeout)

    html = BeautifulSoup(page.text, "html.parser")
    lyrics_path = html.find("div", class_="lyrics")  # finding div on Genius containing the lyrics
    if lyrics_path:
        lyrics = UnicodeDammit(lyrics_path.get_text().strip()).unicode_markup
    else:
        # hotfix!
        lyrics_path = html.find_all("div", class_=re.compile("^Lyrics__Container"))
        lyrics_data = []
        for x in lyrics_path:
            lyrics_data.append(UnicodeDammit(re.sub("<.*?>", "", str(x).replace("<br/>", "\n"))).unicode_markup)

        lyrics = "\n".join(unescape(lyrics_data))  # also convert escaped characters to symbols
    return lyrics


def lyrics(song: str, artist: str, make_issue: bool = True) -> str:
    """
    Displays the fetched lyrics if song playing and handles if lyrics unavailable.
    :param song: currently playing song
    :param artist: song artist
    :param make_issue: whether to make an issue on GitHub if song unsupported
    :return: lyrics if song playing
    """
    try:
        with open(unsupported_txt, encoding='utf-8') as unsupported:
            if f'{song} by {artist}' in unsupported.read():
                return f'Lyrics unavailable for {song} by {artist}.\n'
    except FileNotFoundError:
        pass
    init(autoreset=True)
    print(Fore.CYAN + Style.BRIGHT + f'\nGetting lyrics for {song} by {artist}.\n')
    lyrics = get_lyrics(song, artist)
    if not lyrics:
        lyrics = f"Couldn't get lyrics for {song} by {artist}.\n"
        # log song and artist for which lyrics couldn't be obtained
        with open(unsupported_txt, 'a', encoding='utf-8') as f:
            f.write(f'{song} by {artist} \n')
        if make_issue and re.search(aln, song + artist):
            # only runs if non space or non alphanumeric characters are present
            r = requests.post(f'{backend_url}/unsupported', data={
                'song': song,
                'artist': artist,
                'version': __version__
            }, timeout=api_timeout)
            if r.status_code == 200:
                lyrics += r.text
    return lyrics


if __name__ == '__main__':
    pass
