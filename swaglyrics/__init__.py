import os

name = 'swaglyrics'
__version__ = '1.2.0'
unsupported_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'unsupported.txt')
backend_url = 'https://api.swaglyrics.dev'
api_timeout = 10
genius_timeout = 20


class SameSongPlaying(Exception):
	pass
