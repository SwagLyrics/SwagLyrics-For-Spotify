from bs4 import BeautifulSoup
import requests
import spotify

song = spotify.song()
artist = spotify.artist()

if song or artist is not None:
	song_data = artist+'-'+song
	url_data = song_data.replace(' ', '-')
	url_data = url_data.replace(',', '')
	url_data = url_data.replace("'", '')
	URL = 'https://genius.com/{}-lyrics'.format(url_data)
	page = requests.get(URL)    
	html = BeautifulSoup(page.text, "html.parser") 

	lyrics = html.find("div", class_="lyrics").get_text().encode('ascii', 'ignore')
	print(lyrics.decode('utf-8'))
else:
	print("Nothing playing at the moment.")
