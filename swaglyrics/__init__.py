import os

name = 'swaglyrics'
__version__ = '1.1.0'
unsupported_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'unsupported.txt')
backend_url = 'https://aadibajpai.pythonanywhere.com'


class SameSongPlaying(Exception):
	pass
