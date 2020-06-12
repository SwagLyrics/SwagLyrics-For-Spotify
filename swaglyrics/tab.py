import os

from SwSpotify import spotify, SpotifyNotRunning
from flask import Flask, render_template

from swaglyrics import SameSongPlaying
from swaglyrics.cli import lyrics

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
# use relative path of the template folder

song = None
artist = None


@app.route('/')
def tab() -> str:
    # format lyrics for the browser tab template
    global song, artist
    try:
        song, artist = spotify.current()
        current_lyrics = lyrics(song, artist)
    except SpotifyNotRunning:
        current_lyrics = 'Nothing playing at the moment.'
    current_lyrics = current_lyrics.split('\n')  # break lyrics line by line
    return render_template('lyrics.html', lyrics=current_lyrics, song=song, artist=artist)


@app.route('/songChanged', methods=['GET'])
def song_changed() -> str:
    # to refresh lyrics when song changed
    global song, artist
    try:
        if spotify.current() == (song, artist):
            raise SameSongPlaying
        else:
            return 'yes'
    except (SpotifyNotRunning, SameSongPlaying):
        return 'no'


if __name__ == '__main__':
    app.run()
