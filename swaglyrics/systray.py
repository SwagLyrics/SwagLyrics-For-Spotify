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
def unsupported_precheck():
	try:
		v = requests.get(f'{backend_url}/version')
		ver = v.text
		if ver > version:
			print("New version of SwagLyrics available: v{ver}\nPlease update :)".format(ver=ver))
	except requests.exceptions.RequestException:
		pass
	print('Updating unsupported.txt from server.')
	with open(unsupported_txt, 'w', encoding='utf-8') as f:
		try:
			response = requests.get(f'{backend_url}/master_unsupported')
			f.write(response.text)
			print("Updated unsupported.txt successfully.")
		except requests.exceptions.RequestException as e:
			print("Could not update unsupported.txt successfully.", e)
		except PermissionError as e:
			print("You should install SwagLyrics as --user or use sudo to access unsupported.txt.", e)
			sys.exit(1)
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
            eula = Text(master, wrap=NONE, yscrollcommand=scroll.set, background="black", foreground="white")
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
