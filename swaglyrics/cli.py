from bs4 import BeautifulSoup, UnicodeDammit
from unidecode import unidecode
import requests
import re
import sys
import time
import os


def clear():
	os.system('cls' if os.name == 'nt' else 'clear')  # clear command window


def stripper_genius(song, artist):
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
	song = re.sub(r'\([^)]*\)', '', song).strip()  # remove braces and included text
	song = re.sub('- .*', '', song).strip()  # remove text after '- '
	song_data = artist + '-' + song
	# Remove special characters and spaces
	url_data = song_data.replace('&', 'and')
	for ch in [',', '\'', '!', '.', '’', '"', '+', '?', 'Σ', '#']:
		if ch in url_data:
			url_data = url_data.replace(ch, '')
	url_data = ' '.join(url_data.split())  # remove multiple spaces to one space
	url_data = url_data.replace(' ', '-')  # hyphenate the words together
	url_data = unidecode(url_data)  # remove accents and other diacritics
	return url_data

def stripper_lyricsmode(song, artist):
	"""
	Generate the url path given the song and artist to format the LYRICSMODE URL with.
	Strips the song and artist of special characters and unresolved text such as 'feat.' or text within braces.
	Then concatenates both with hyphens replacing the blank spaces.
	Eg.
	>>>stripper('Paradise City', 'Guns n’ Roses')
	g/guns_n_roses/paradise_city.html
	Which then formats the url to https://lyricsmode.com/lyrics/g/guns_n_roses/paradise_city.html
	:param song: currently playing song
	:param artist: song artist
	:return: formatted url path
	"""
	song = re.sub(r'\([^)]*\)', '', song).strip()  # remove braces and included text
	song = re.sub('- .*', '', song).strip()  # remove text after '- '
	song_data = artist[0] +'/'  + artist + '/' + song
	url_data = song_data.replace('&', 'and')
	for ch in [',', '\'', '!', '.', '’', '"', '+', '?', 'Σ', '#']:
		if ch in url_data:
			url_data = url_data.replace(ch, '')
	url_data = ' '.join(url_data.split())  # remove multiple spaces to one space
	url_data = url_data.replace(' ', '_')  # hyphenate the words together
	url_data = unidecode(url_data)  # remove accents and other diacritics
	url_data = url_data + '.html'
	return url_data.lower()

def stripper_google(song, artist):
	# song = re.sub(r'\([^)]*\)', '', song).strip()  # remove braces and included text
	# song = re.sub('- .*', '', song).strip()  # remove text after '- '
	q = song + ' ' + artist + ' lyrics'
	q = q.replace('%', '%25')
	dic = {',':'%2C', '\'':'%27', '+':'%2B', '?':r'%3F', '#':'%23', '&':'%26', '^':r'%5E', '$':'%24',
		'@':'%40', '=':'%3D', '`':'%60', '{':'%7B', '}':'%7D', '[':'%5B', ']':'%5D', ':':'%3A',
		';':'%3B', '\\':'5C', '|':'%7C', '/':r'%2F'
	}
	for ch, r_ch in dic.items():
		# print(ch,)
		q = q.replace(ch, r_ch)
	# q = unidecode(q)
	q = q.replace(' ', '+')
	return q


def get_lyrics_genius(song, artist):
	"""
	Get lyrics from Genius given the song and artist.
	Formats the URL with the stripped url path to fetch the lyrics.
	:param song: currently playing song
	:param artist: song artist
	:return: song lyrics
	"""
	url_data = stripper_genius(song, artist)  # generate url path using stripper()
	url = 'https://genius.com/{}-lyrics'.format(url_data)  # format the url with the url path
	page = requests.get(url)
	if page.status_code != 200:
		url_data = requests.get('http://aadibajpai.pythonanywhere.com/stripper', data={'song': song, 'artist': artist}).text
		url = 'https://genius.com/{}-lyrics'.format(url_data)
		page = requests.get(url)
	html = BeautifulSoup(page.text, "html.parser")
	# TODO: Add error handling
	lyrics_path = html.find("div", class_="lyrics")  # finding div on Genius containing the lyrics
	if lyrics_path is None:
		return None
	else:
		lyrics = UnicodeDammit(lyrics_path.get_text().strip()).unicode_markup
	return lyrics



def get_lyrics_lyricsmode(song, artist):
	"""
	Get lyrics from LYRICSMODE.COM given the song and artist.
	Formats the URL with the stripped url path to fetch the lyrics.
	:param song: currently playing song
	:param artist: song artist
	:return: song lyrics
	"""
	url_data = stripper_lyricsmode(song, artist)  # generate url path using stripper()
	url = 'https://lyricsmode.com/lyrics/{}'.format(url_data)  # format the url with the url path
	page = requests.get(url)
	if page.status_code != 200:
		return None
	html = BeautifulSoup(page.text, "html.parser")
	lyrics_path = html.find("div", class_="js-new-text-select")  # finding div on LYRICSMODE containing the lyrics
	if lyrics_path is None:
		return None
	lyrics = UnicodeDammit(lyrics_path.get_text().strip()).unicode_markup
	return lyrics

def get_lyrics_google(song, artist):
	headers_Get = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	    'Accept-Language': 'en-US,en;q=0.5',
	    'Accept-Encoding': 'gzip, deflate',
	    'DNT': '1',
	    'Connection': 'keep-alive',
	    'Upgrade-Insecure-Requests': '1'
	}
	q = stripper_google(song, artist)
	song_ = re.sub(r'\([^)]*\)', '', song).strip()  # remove braces and included text
	song_ = re.sub('- .*', '', song_).strip()  # remove text after '- '

	url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
	# url = 'https://www.google.com/search?q={}&oq={}&aqs=chrome..69i64.10943j0j7&sourceid=chrome&ie=UTF-8'.format(url_data, url_data)
	page = requests.get(url, headers=headers_Get)
	if page.status_code!=200:
		return None
	html = BeautifulSoup(page.text, 'html.parser')
	lyrics = html.find('div', class_='Kvw2ac')
	song_google = html.find('div', class_="gsmt")
	artist_google = html.find('div', class_="wwUB2c")
	if lyrics is None or artist_google is None or song_google is None:
		return None
	# print(song_google.text, artist_google.text)
	for i in artist.split():
		if not i.lower() in artist_google.text.lower():
			return None
	# print(lyrics.text)
	return UnicodeDammit(lyrics.get_text('\n').strip()).unicode_markup

def unsupported_song_addition(song, artist, make_issue=True):
	"""
	Adds the song to the list of unsupported songs
	:param song:
	:param artist:
	:param make_issue: whether to make an issue on GitHub if song unsupported
	"""
	with open('unsupported.txt', 'a') as f:
		f.write('{song} by {artist} \n'.format(song=song, artist=artist))
		f.close()
	text = 'Couldn\'t get lyrics for {song} by {artist}.\n'.format(song=song, artist=artist)
	try:
		# Log song and artist for which lyrics couldn't be obtained
		if make_issue:
			r = requests.post('http://aadibajpai.pythonanywhere.com/unsupported', data={'song': song, 'artist': artist})
			if r.status_code == 200:
				text += r.text
	except requests.exceptions.RequestException:
		pass
	return text



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
			with open('unsupported.txt') as unsupported:
				if song in unsupported.read():
					return 'Lyrics unavailable for {song} by {artist}.\n'.format(song=song, artist=artist)
		except FileNotFoundError:
			pass
		# print('\nGetting lyrics for {song} by {artist} '.format(song=song, artist=artist), end='')
		lyrics = get_lyrics_genius(song, artist)
		if lyrics is None:
			lyrics = get_lyrics_lyricsmode(song, artist)
		if lyrics is None:
			lyrics = get_lyrics_google(song, artist)
		if lyrics is None:			
			lyrics = unsupported_song_addition(song, artist, make_issue)
		for _ in range(30):  # loading spinner
			sys.stdout.write(next(spinner))
			sys.stdout.flush()
			time.sleep(0.1)
			sys.stdout.write('\b')
		sys.stdout.write('\b.   \n\n')
		sys.stdout.flush()
		return lyrics
	else:
		return 'Nothing playing at the moment.'


def spinning_cursor():
	while True:
		for cursor in '|/-\\':
			yield cursor


spinner = spinning_cursor()

if __name__ == '__main__':
	pass
