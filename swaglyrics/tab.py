from cli import lyrics
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
import os
import spotify
import chrome

song = None
artist = None
isSameSong = True


app = Flask(
    __name__,
    template_folder=os.path.join(
        os.path.dirname(os.path.abspath("SwagLyrics-For-Spotify")),
        "swaglyrics/templates",
    ),
)
# use relative path of the template folder
CORS(app, support_credentials=True)
# using CORS module to handle cross origin ajax requests possible from browsers, for security reasons


@app.route("/", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def tab():
    # format lyrics for the browser tab template
    # runs at the starting and when song changes to refresh changes onto browser
    global song, artist, isSameSong
    isSameSong = True

    song = spotify.song()
    artist = spotify.artist()

    current_lyrics = lyrics(song, artist)
    current_lyrics = current_lyrics.split("\n")  # break lyrics line by line

    return render_template(
        "lyrics.html", lyrics=current_lyrics, song=song, artist=artist
    )


@app.route("/getsong", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def chromeSong():
    # Route to handle post request from browser
    global isSameSong
    isSameSong = False

    if request.method == "POST" or request.method == "OPTIONS":

        response = request.get_json(force=True)
        chrome.song = response["title"]
        chrome.artist = response["artist"]

        if chrome.isTerminal is True:
            # if called on terminal, print lyrics on terminal

            current_lyrics = lyrics(chrome.song, chrome.artist)
            print(current_lyrics)

    return chrome.artist, chrome.song


@app.route("/songChanged", methods=["GET"])
def song_changed():
    # to refresh lyrics when song changed
    global song, isChrome, chromeSong, isSameSong
    if chrome.isChrome == False:
        if song == spotify.song() or spotify.song() is None:
            return "no"
        else:
            return "yes"

    if isSameSong == True:
        return "no"

    return "yes"


if __name__ == "__main__":
    app.run()
