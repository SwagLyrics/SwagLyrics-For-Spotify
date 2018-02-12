from bs4 import BeautifulSoup
import requests
import spotify
import re
import sys
import time


def stripper(song, artist):
	song = re.sub(r'\([^)]*\)', '', song).strip()
	song = re.sub('\- .*', '', song).strip()
	song_data = artist + '-' + song
	url_data = song_data.replace('&', 'and')
	url_data = url_data.replace(' ', '-')
	for ch in [',', '\'', '!', '.', '’']:
		if ch in url_data:
			url_data = url_data.replace(ch, '')
	return url_data


def get_lyrics(song, artist):
	url_data = stripper(song, artist)
	url = 'https://genius.com/{}-lyrics'.format(url_data)
	page = requests.get(url)
	html = BeautifulSoup(page.text, "html.parser")
	lyrics_path = html.find("div", class_="lyrics")
	if lyrics_path is None:
		lyrics = 'Couldn\'t get lyrics for {song} by {artist}.'.format(song=song, artist=artist)
	else:
		lyrics = lyrics_path.get_text().encode('ascii', 'ignore').decode('utf-8')
	return lyrics


def lyrics(song, artist):
	if song and artist:
		print('Getting lyrics for {song} by {artist} '.format(song=song, artist=artist), end='')
		for _ in range(30):
			sys.stdout.write(next(spinner))
			sys.stdout.flush()
			time.sleep(0.1)
			sys.stdout.write('\b')
		sys.stdout.write('\b   \n')
		sys.stdout.flush()
		return get_lyrics(song, artist)
	else:
		return 'Nothing playing at the moment.'


def spinning_cursor():
	while True:
		for cursor in '|/-\\':
			yield cursor


spinner = spinning_cursor()

if __name__ == "__main__":
	song = spotify.song()
	artist = spotify.artist()
	print(lyrics(song, artist))
	while True:
		if song == spotify.song()and artist == spotify.artist():
			time.sleep(5)
		else:
			song = spotify.song()
			artist = spotify.artist()
			print(lyrics(song, artist))
