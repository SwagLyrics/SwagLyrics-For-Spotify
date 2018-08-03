import argparse
from swaglyrics.cli import lyrics, clear
from swaglyrics.app import app
from swaglyrics import spotify
import time

parser = argparse.ArgumentParser(
	description="Get lyrics for currently playing song on Spotify. Either --tab or --cli is required.")

parser.add_argument('-t', '--tab', action='store_true', help='Display lyrics in a browser tab.')
parser.add_argument('-c', '--cli', action='store_true', help='Display lyrics in the command-line.')

args = parser.parse_args()

if args.tab:
	app.run()

elif args.cli:
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

else:
	parser.print_help()
