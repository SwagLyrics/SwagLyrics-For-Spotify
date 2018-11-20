"""
Contains unit tests for spotify.py for linux
"""
import unittest
from swaglyrics.spotify import get_info_linux, song, artist
from mock import mock, patch

class Tests(unittest.TestCase):
	"""
	Unit tests
	"""

	def setup(self):
		pass

	@patch('swaglyrics.spotify.get_info_linux')
	def test_that_artist_function_calls_get_info(self, mock):
		"""
		test that test artist function calls get_info_linux function
		"""
		x = artist()
		self.assertTrue(mock.called)

	@patch('swaglyrics.spotify.get_info_linux')
	def test_that_song_function_calls_get_info(self, mock):
		"""
		test that test song function calls get_info_linux function
		"""
		x = song()
		self.assertTrue(mock.called)


if __name__ == '__main__':
	unittest.main()
