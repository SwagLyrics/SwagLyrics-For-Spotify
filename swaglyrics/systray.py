import argparse
import os
import sys
import requests
import time
from SwSpotify import spotify, SpotifyNotRunning
from swaglyrics.cli import lyrics, clear
from swaglyrics.tab import app
from swaglyrics import unsupported_txt, SameSongPlaying, __version__ as version, backend_url
from tkinter import *
def systray():
    
    from infi.systray import SysTrayIcon
    x = 0 
    def get_lyrics(systray):
        try:
            song, artist = spotify.current()  # get currently playing song, artist
            songlyrics = lyrics(song, artist)
            master = Tk()
            scroll = Scrollbar(master)
            scroll.pack(side=RIGHT, fill=Y)
            eula = Text(master, wrap=NONE, yscrollcommand=scroll.set)
            eula.insert("1.0", songlyrics)
            eula.pack(side="left")
            scroll.config(command=eula.yview)
            master.title(song+" by "+artist)
            mainloop()  
        except SpotifyNotRunning as e:
            print(e)
            song, artist = None, None
    def on_quit_callback(systray):
        program.shutdown()
        exit()
    menu_options = (("Get Lyrics", None,  get_lyrics),)
    current_path = os.path.abspath(__file__)
    img_path = current_path.replace("systray.py", "icon.ico")
    systray = SysTrayIcon(img_path, "SwagLyrics", menu_options)
    systray.start()
systray()
