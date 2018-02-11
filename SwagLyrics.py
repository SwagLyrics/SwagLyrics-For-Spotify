from bs4 import BeautifulSoup
import requests
import spotify

song = spotify.song()
artist = spotify.artist()

if song and artist:
	song_data = artist+'-'+song
	url_data = song_data.replace(' ', '-')
	url_data = url_data.replace(',', '')
	url_data = url_data.replace("'", '')
	URL = 'https://genius.com/{}-lyrics'.format(url_data)
	page = requests.get(URL)
	html = BeautifulSoup(page.text, "html.parser")
	lyrics_path = html.find("div", class_="lyrics")
	if lyrics_path is None:
		print('Could not get lyrics for {song} by {artist}.'.format(song=song, artist=artist))
	else:
		lyrics = lyrics_path.get_text().encode('ascii', 'ignore').decode('utf-8')
		print(lyrics)
else:
	print("Nothing playing at the moment.")
