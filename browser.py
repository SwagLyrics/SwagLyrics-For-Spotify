from SwagLyrics import lyrics
from flask import Flask, render_template

import spotify

app = Flask(__name__)


@app.route('/')
def tab():
	song = spotify.song()
	artist = spotify.artist()
	current_lyrics = lyrics(song, artist)
	current_lyrics = current_lyrics.split('\n')
	return render_template('lyrics.html', lyrics=current_lyrics, song=song)


if __name__ == "__main__":
	app.run()
