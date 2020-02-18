import os

name = 'SwagLyrics'
__version__ = '1.1.1'
unsupported_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'unsupported.txt')
backend_url = 'https://api.swaglyrics.dev'


class SameSongPlaying(Exception):
	pass
