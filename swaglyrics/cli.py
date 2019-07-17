import requests
import re
import os
from swaglyrics import __version__, unsupported_txt
from bs4 import BeautifulSoup, UnicodeDammit
from unidecode import unidecode
from colorama import init, Fore


def clear():
	os.system('cls' if os.name == 'nt' else 'clear')  # clear command window


brc = re.compile(r'([(\[](feat|ft)[^)\]]*[)\]]|- .*)', re.I)  # matches braces with feat included or text after -
aln = re.compile(r'[^ \-a-zA-Z0-9]+')  # matches non space or - or alphanumeric characters
spc = re.compile(' *- *| +')  # matches one or more spaces
wth = re.compile(r'(?: *\(with )([^)]+)\)')  # capture text after with
nlt = re.compile(r'[^\x00-\x7F\x80-\xFF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF]')  # match only latin characters,
# built using latin character tables (basic, supplement, extended a,b and extended additional


def stripper(song, artist):
	"""
	Generate the url path given the song and artist to format the Genius URL with.
	Strips the song and artist of special characters and unresolved text such as 'feat.' or text within braces.
	Then concatenates both with hyphens replacing the blank spaces.
	Eg.
	>>>stripper('Paradise City', 'Guns n’ Roses')
	Guns-n-Roses-Paradise-City
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
			artist += '-{ar}'.format(ar=ar)
		else:
			artist += '-and-{ar}'.format(ar=ar)
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


def get_lyrics(song, artist, make_issue=True):
	"""
	Get lyrics from Genius given the song and artist.
	Formats the URL with the stripped url path to fetch the lyrics.
	:param song: currently playing song
	:param artist: song artist
	:param make_issue: whether to make an issue on GitHub if song unsupported
	:return: song lyrics
	"""
	url_data = stripper(song, artist)  # generate url path using stripper()
	url = 'https://genius.com/{}-lyrics'.format(url_data)  # format the url with the url path
	page = requests.get(url)
	if page.status_code != 200:
		url_data = requests.get('https://aadibajpai.pythonanywhere.com/stripper',
								data={'song': song, 'artist': artist}).text
		url = 'https://genius.com/{}-lyrics'.format(url_data)
		page = requests.get(url)
	html = BeautifulSoup(page.text, "html.parser")
	# TODO: Add error handling
	lyrics_path = html.find("div", class_="lyrics")  # finding div on Genius containing the lyrics
	if lyrics_path is None:
		with open(unsupported_txt, 'a') as f:
			f.write('{song} by {artist} \n'.format(song=song, artist=artist))
			f.close()
		lyrics = 'Couldn\'t get lyrics for {song} by {artist}.\n'.format(song=song, artist=artist)
		try:
			# Log song and artist for which lyrics couldn't be obtained
			if make_issue:
				r = requests.post('https://aadibajpai.pythonanywhere.com/unsupported', data={
					'song': song,
					'artist': artist,
					'version': __version__
				})
				if r.status_code == 200:
					lyrics += r.text
		except requests.exceptions.RequestException:
			pass
	else:
		lyrics = UnicodeDammit(lyrics_path.get_text().strip()).unicode_markup
	return lyrics


def lyrics(song, artist, make_issue=True):
	"""
	Displays the fetched lyrics if song playing.
	:param song: currently playing song
	:param artist: song artist
	:param make_issue: whether to make an issue on GitHub if song unsupported
	:return: lyrics if song playing
	"""
	if song and artist:  # check if song playing
		try:
			with open(unsupported_txt) as unsupported:
				if song in unsupported.read():
					return 'Lyrics unavailable for {song} by {artist}.\n'.format(song=song, artist=artist)
		except FileNotFoundError:
			pass
		init(autoreset=True)
		print(Fore.CYAN + '\nGetting lyrics for {song} by {artist}.\n'.format(song=song, artist=artist))
		lyrics = get_lyrics(song, artist, make_issue)
		return lyrics
	else:
		return 'Nothing playing at the moment.'


if __name__ == '__main__':
	pass
