import argparse
import os
import webbrowser
import threading
import requests
import time
from swaglyrics.cli import lyrics, clear
from swaglyrics import spotify
from swaglyrics.tab import app
from swaglyrics import chrome



def main():
	# 	print(r"""
	#  ____                     _               _
	# / ___|_      ____ _  __ _| |   _   _ _ __(_) ___ ___
	# \___ \ \ /\ / / _` |/ _` | |  | | | | '__| |/ __/ __|
	#  ___) \ V  V / (_| | (_| | |__| |_| | |  | | (__\__ \
	# |____/ \_/\_/ \__,_|\__, |_____\__, |_|  |_|\___|___/
	#                     |___/      |___/
	# 	""")
	print('Updating unsupported.txt from server.')
	with open('unsupported.txt', 'w', encoding='utf-8') as f:
		response = requests.get('http://aadibajpai.pythonanywhere.com/master_unsupported')
		f.write(response.text)
	print("Updated unsupported.txt successfully.")

	parser = argparse.ArgumentParser(
		description="Get lyrics for the currently playing song on Spotify. Either --tab or --cli is required.")

	parser.add_argument('-t', '--tab', action='store_true', help='Display lyrics in a browser tab.')
	parser.add_argument('-c', '--cli', action='store_true', help='Display lyrics in the command-line.')
	parser.add_argument('--chrome', action='store_true', help='Display lyrics from browser.')

	args = parser.parse_args()
	app.template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
	app.static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
	port = 5042  # random
	url = "http://127.0.0.1:{port}".format(port=port)
	chrome.initvariables()
	#checking whether if chrome was passed via arguments or not
	if args.chrome:
		chrome.isChrome = True
		print("Listesning to chrome")
	else:
		chrome.isChrome = False
		print("Listesning to local")
		

	if args.tab:
		print('Firing up a browser tab!')
		threading.Timer(1.25, lambda: webbrowser.open(url)).start()
		app.run(port=port)

	elif args.cli:
		chrome.isTerminal = True
		if chrome.isChrome == True:
			# Starts a new thread with server running, to post requests from extension.
			t1 = threading.Thread(target=app.run(port=port))
			t1.start()
			exit()
		song = spotify.song()  # get currently playing song
		artist = spotify.artist()  # get currently playing artist
		print(lyrics(song, artist))
		print('\n(Press Ctrl+C to quit)')
		while True:
			# refresh every 5s to check whether song changed
			# if changed, display the new lyrics
			try:
				if song == spotify.song() and artist == spotify.artist():
					time.sleep(5)
				else:
					song = spotify.song()
					artist = spotify.artist()
					if song and artist is not None:
						clear()
						print(lyrics(song, artist))
						print('\n(Press Ctrl+C to quit)')
			except KeyboardInterrupt:
				exit()
			if os.environ.get("TESTING", "False") != "False":
				break

	else:
		parser.print_help()


if __name__ == '__main__':
	main()

