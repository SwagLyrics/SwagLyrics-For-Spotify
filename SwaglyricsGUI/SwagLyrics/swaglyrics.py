import argparse
import os
import sys
import requests
import time
from SwSpotify import spotify, SpotifyNotRunning
from cli import lyrics, clear
from tab import app
from init import unsupported_txt, SameSongPlaying, __version__ as version, backend_url
import eel

song = None
artist = None

# window = tkinter.Tk()
# window.title("SwagLyrics")
eel.init('web')

@eel.expose
def song_changed():
    # to refresh lyrics when song changed
    global song, artist
    try:
        if spotify.current() == (song, artist):
            raise SameSongPlaying
        else:
            return 'yes'
    except (SpotifyNotRunning, SameSongPlaying):
        return 'no'


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


def show_tab():
	from threading import Timer
	from webbrowser import open
	print('Firing up a browser tab!')
	app.template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
	app.static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
	port = 5042  # random
	url = f"http://127.0.0.1:{port}"
	Timer(1.25, open, args=[url]).start()
	app.run(port=port)

@eel.expose
def show_cli(make_issue=False):
	try:
		song, artist = spotify.current()  # get currently playing song, artist
		return(lyrics(song, artist, make_issue))
		print('\n(Press Ctrl+C to quit)')
	except SpotifyNotRunning as e:
		return(e)
		print('\n(Press Ctrl+C to quit)')
		song, artist = None, None


@eel.expose
def artist_song(make_issue=False):
	try:
		song, artist = spotify.current()  # get currently playing song, artist
		if(song == "Advertisement"):
			return("Advertisement")
		return("Song : "+ song +"<br> Artist : "+artist)
		print('\n(Press Ctrl+C to quit)')
	except SpotifyNotRunning as e:
		print(e)
		print('\n(Press Ctrl+C to quit)')
		song, artist = None, None
	
# def printLyrics():
# 	tkinter.Label(window, text = show_cli()).pack()

# tkinter.Button(window, text="Get Lyrics", command = printLyrics).pack()

# window.mainloop()


# def main():
# 	print(r"""
# 	 ____                     _               _
# 	/ ___|_      ____ _  __ _| |   _   _ _ __(_) ___ ___
# 	\___ \ \ /\ / / _` |/ _` | |  | | | | '__| |/ __/ __|
# 	 ___) \ V  V / (_| | (_| | |__| |_| | |  | | (__\__ \
# 	|____/ \_/\_/ \__,_|\__, |_____\__, |_|  |_|\___|___/
# 	                    |___/      |___/
# 		""")
# 	print('\n')

# 	parser = argparse.ArgumentParser(
# 		description="Get lyrics for the currently playing song on Spotify. Either --tab or --cli is required.")

# 	parser.add_argument('-t', '--tab', action='store_true', help='Display lyrics in a browser tab.')
# 	parser.add_argument('-c', '--cli', action='store_true', help='Display lyrics in the command-line.')
# 	parser.add_argument('-n', '--no-issue', action='store_false', help='Disable issue-making on cli.')
# 	args = parser.parse_args()

# 	if args.tab:
# 		unsupported_precheck()
# 		show_tab()

# 	elif args.cli:
# 		unsupported_precheck()
# 		make_issue = args.no_issue
# 		return show_cli(make_issue)
# 	else:
# 		parser.print_help()

eel.start('index.html',size=(800,600))
# if __name__ == '__main__':
# 	main()
