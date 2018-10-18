from bs4 import BeautifulSoup
import requests
import re
import sys
import time
import os

clear = lambda: os.system('cls')  # clear command window


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
	song = re.sub(r'\([^)]*\)', '', song).strip()  # remove braces and included text
	song = re.sub('- .*', '', song).strip()  # remove text after '- '
	song_data = artist + '-' + song
	# Remove special characters and spaces
	url_data = song_data.replace('&', 'and')
	url_data = url_data.replace(' ', '-')  # hyphenate the words together
	for ch in [',', '\'', '!', '.', '’', '"', '+']:
		if ch in url_data:
			url_data = url_data.replace(ch, '')
	return url_data


def get_lyrics(song, artist):
	"""
	Get lyrics from Genius given the song and artist.
	Formats the URL with the stripped url path to fetch the lyrics.
	:param song: currently playing song
	:param artist: song artist
	:return: song lyrics
	"""
	url_data = stripper(song, artist)  # generate url path using stripper()
	url = 'https://genius.com/{}-lyrics'.format(url_data)  # format the url with the url path
	page = requests.get(url)
	html = BeautifulSoup(page.text, "html.parser")
	# TODO: Add error handling
	lyrics_path = html.find("div", class_="lyrics")  # finding div on Genius containing the lyrics
	if lyrics_path is None:
		with open('unsupported.txt', 'a') as f:
			f.write('{song} by {artist} \n '.format(song=song, artist=artist))
			f.close()
		lyrics = 'Couldn\'t get lyrics for {song} by {artist}.\n'.format(song=song, artist=artist)
		try:
			# Log song and artist for which lyrics couldn't be obtained
			r = requests.post('http://aadibajpai.pythonanywhere.com/unsupported', data={'song': song, 'artist': artist})
			if r.status_code == 200:
				lyrics += r.text
		except requests.exceptions.RequestException:
			pass
	else:
		lyrics = lyrics_path.get_text().encode('ascii', 'ignore').decode('utf-8').strip()
	return lyrics


def lyrics(song, artist):
	"""
	Displays the fetched lyrics if song playing.
	:param song: currently playing song
	:param artist: song artist
	:return: lyrics if song playing
	"""
	if song and artist:  # check if song playing
		try:
			if song in open('unsupported.txt').read():
				return 'Lyrics unavailable for {song} by {artist}.\n'.format(song=song, artist=artist)
		except FileNotFoundError:
			pass
		print('\nGetting lyrics for {song} by {artist} '.format(song=song, artist=artist), end='')
		lyrics = get_lyrics(song, artist)
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
