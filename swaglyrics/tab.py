from swaglyrics.cli import lyrics
from flask import Flask, render_template
import os
from swaglyrics import spotify

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath('SwagLyrics-For-Spotify')), 'swaglyrics/templates'))
# use relative path of the template folder

song = None
artist = None


@app.route('/')
def tab():
    # format lyrics for the browser tab template
    global song, artist
    if spotify.get_searched_song() and spotify.get_searched_artist():
        song = spotify.get_searched_song()
        artist = spotify.get_searched_artist()
    else:
        song = spotify.song()
        artist = spotify.artist()
    current_lyrics = lyrics(song, artist)
    current_lyrics = current_lyrics.split('\n')  # break lyrics line by line
    return render_template('lyrics.html', lyrics=current_lyrics, song=song, artist=artist)


@app.route('/songChanged', methods=['GET'])
def song_changed():
    # to refresh lyrics when song changed
    global song
    spotify.set_searched_song(None)
    spotify.set_searched_artist(None)
    if song == spotify.song() or spotify.song() is None:
        return 'no'
    return 'yes'


if __name__ == '__main__':
    app.run()
