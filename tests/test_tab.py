"""
Contains unit tests for tab.py
"""
from flask_testing import TestCase
from mock import mock
import os

class Tests(TestCase):
	"""
	Unit tests
	"""

	def setup(self):
		pass

	def create_app(self):
		from swaglyrics.tab import app
		return app

	@mock.patch('swaglyrics.spotify.song', return_value="Blank Space")
	@mock.patch('swaglyrics.spotify.artist', return_value="Taylor Swift")
	def test_lyrics_are_shown_in_tab(self, mock_song, mock_artist):
		"""
		that that tab.py is working
		"""
		with self.app.test_client() as c:
			response = c.get('/')
			self.assert_template_used("lyrics.html")

if __name__ == '__main__':
	unittest.main()
