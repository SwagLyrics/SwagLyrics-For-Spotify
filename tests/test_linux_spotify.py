"""
Contains unit tests for spotify.py for linux
"""
import unittest
from swaglyrics.spotify import get_info_linux, song, artist
from mock import mock, patch, Mock

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

	@patch('swaglyrics.spotify.get_info_linux', side_effect=ValueError)
	def test_that_artist_function_returns_None_when_error(self, mock):
		"""
		test that test artist function returns None when the get_info_linux function will return an error
		"""
		x = artist()
		self.assertEqual(x, None)

	@patch('swaglyrics.spotify.get_info_linux', side_effect=ValueError)
	def test_that_song_functio_returns_None_when_error(self, mock):
		"""
		test that test song function returns None when the get_info_linux function will return an error
		"""
		x = song()
		self.assertEqual(x, None)


if __name__ == '__main__':
	unittest.main()
