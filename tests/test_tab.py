"""
Contains unit tests for tab.py
"""
import flask_testing
from mock import mock
import os


class Tests(flask_testing.TestCase):
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

	# @mock.patch('swaglyrics.spotify.get_searched_song', return_value="Perfect")
	# @mock.patch('swaglyrics.spotify.get_searched_artist', return_value="Ed Sheeran")
	# def test_lyrics_are_shown_in_tab_when_song_and_artist_given(self, mock_song, mock_artist):
	# 	with self.app.test_client() as c:
	# 		response = c.get('/')
	# 		self.assert_template_used("lyrics.html")

	@mock.patch('swaglyrics.spotify.song', return_value=None)
	@mock.patch('swaglyrics.spotify.artist', return_value=None)
	def test_tab_runs_when_no_song_and_artist_on_spotify(self, mock_song, mock_artist):
		with self.app.test_client() as c:
			response = c.get('/songChanged')
			self.assertEqual(response.status_code, 200)

	@mock.patch('swaglyrics.spotify.song', return_value="Truthfully")
	@mock.patch('swaglyrics.spotify.artist', return_value="DNCE")
	def test_tab_runs_when_song_and_artist_on_spotify(self, mock_song, mock_artist):
		with self.app.test_client() as c:
			response = c.get('/songChanged')
			self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
	flask_testing.main()
