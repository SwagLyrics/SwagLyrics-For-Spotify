from SwagLyrics import lyrics
from flask import Flask, render_template

import spotify

app = Flask(__name__)

song = None
artist = None


@app.route('/')
def tab():
	global song, artist
	song = spotify.song()
	artist = spotify.artist()
	current_lyrics = lyrics(song, artist)
	current_lyrics = current_lyrics.split('\n')
	return render_template('lyrics.html', lyrics=current_lyrics, song=song, artist=artist)


@app.route('/songChanged', methods=['GET'])
def song_changed():
	global song
	if song == spotify.song():
		return 'no'
	return 'yes'


if __name__ == "__main__":
	app.run()
