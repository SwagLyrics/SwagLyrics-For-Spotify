from SwagLyrics import lyrics
from flask import Flask

import spotify

app = Flask(__name__)


@app.route('/')
def tab():
	song = spotify.song()
	artist = spotify.artist()
	current_lyrics = lyrics(song, artist)
	return current_lyrics


if __name__ == "__main__":
	app.run()
