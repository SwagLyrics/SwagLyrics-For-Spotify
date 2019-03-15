from swaglyrics.cli import lyrics
from flask import Flask, render_template,jsonify,request
from flask_cors import CORS, cross_origin
import os
from swaglyrics import spotify


app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath('SwagLyrics-For-Spotify')), 'swaglyrics/templates'))
# use relative path of the template folder

CORS(app, support_credentials=True)


song = None
artist = None
isChrome = False
chromeSong=None
isSameSong=True

@app.route('/',methods=["GET","POST"])
@cross_origin(supports_credentials=True)
def tab():
    # format lyrics for the browser tab template
    global song,artist,isChrome,isSameSong
    isSameSong=True
    if request.method=="POST" or request.method=="OPTIONS" :
        isChrome=True
        isSameSong=False
        response=request.get_json(force=True)
        song=response["title"]
        artist=response["artist"]
        
    if isChrome==False:
        song = spotify.song()
        artist = spotify.artist()   
        
    current_lyrics = lyrics(song, artist)
    current_lyrics = current_lyrics.split('\n')  # break lyrics line by line
    return render_template('lyrics.html', lyrics=current_lyrics, song=song, artist=artist)


@app.route('/songChanged', methods=['GET'])
def song_changed():
    # to refresh lyrics when song changed
    global song,isChrome,chromeSong
    if not isChrome:
        if song == spotify.song() or spotify.song() is None:
           return 'no' 
    if isSameSong==True:
        return 'no'       
    return 'yes'


if __name__ == '__main__':
    app.run()
