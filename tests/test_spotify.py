"""
Contains unit tests for spotify.py for linux
"""
import unittest
from swaglyrics.spotify import get_info_linux, get_info_windows, get_info_mac, song, artist
from mock import mock, patch, Mock
import platform

class LinuxTests(unittest.TestCase):
	"""
	Unit tests for Linux
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
	def test_that_song_function_returns_None_when_error(self, mock):
		"""
		test that test song function returns None when the get_info_linux function will return an error
		"""
		x = song()
		self.assertEqual(x, None)

class WindowsTests(unittest.TestCase):
	"""
	Unit tests for Windows
	"""

	def setup(self):
		pass

	if platform.system() == "Windows":
		import win32gui
	@mock.patch('win32gui.GetWindowText', return_value='Alan Walker - Darkside')
	@mock.patch('win32gui.EnumWindows', return_value=None)
	def test_get_info_windows(self, mock_win32gui_1, mock_win32gui_2):
		"""
		test that get_info_windows works
		"""
		x = get_info_windows()
		self.assertEqual(x, ("Alan Walker","Darkside"))

	@patch('swaglyrics.spotify.get_info_windows')
	def test_that_artist_function_calls_get_info(self, mock):
		"""
		test that test artist function calls get_info_windows function
		"""
		x = artist()
		self.assertTrue(mock.called)

	@patch('swaglyrics.spotify.get_info_windows')
	def test_that_song_function_calls_get_info(self, mock):
		"""
		test that test song function calls get_info_windows function
		"""
		x = song()
		self.assertTrue(mock.called)

	@patch('swaglyrics.spotify.get_info_windows', side_effect=ValueError)
	def test_that_artist_function_returns_None_when_error(self, mock):
		"""
		test that test artist function returns None when the get_info_windows function will return an error
		"""
		x = artist()
		self.assertEqual(x, None)

	@patch('swaglyrics.spotify.get_info_windows', side_effect=ValueError)
	def test_that_song_function_returns_None_when_error(self, mock):
		"""
		test that test song function returns None when the get_info_windows function will return an error
		"""
		x = song()
		self.assertEqual(x, None)

@mock.patch('platform.system', return_value='Darwin')
class DarwinTests(unittest.TestCase):
	"""
	Unit tests for OSX
	"""

	def setup(self, mock_os):
		pass

	@patch('swaglyrics.spotify.get_info_mac')
	def test_that_artist_function_calls_get_info(self, mock, mock_os):
		"""
		test that test artist function calls get_info_mac function
		"""
		x = artist()
		self.assertTrue(mock.called)

	@patch('swaglyrics.spotify.get_info_mac')
	def test_that_song_function_calls_get_info(self, mock, mock_os):
		"""
		test that test song function calls get_info_mac function
		"""
		x = song()
		self.assertTrue(mock.called)

	@patch('swaglyrics.spotify.get_info_mac', side_effect=ValueError)
	def test_that_artist_function_returns_None_when_error(self, mock, mock_os):
		"""
		test that test artist function returns None when the get_info_mac function will return an error
		"""
		x = artist()
		self.assertEqual(x, None)

	@patch('swaglyrics.spotify.get_info_mac', side_effect=ValueError)
	def test_that_song_function_returns_None_when_error(self, mock, mock_os):
		"""
		test that test song function returns None when the get_info_mac function will return an error
		"""
		x = song()
		self.assertEqual(x, None)
<<<<<<< HEAD

class WindowsSpotifyTests(unittest.TestCase):

	if platform.system() == "Windows":
		import win32gui
	from swaglyrics.spotify import get_info_windows
	@mock.patch('win32gui.GetWindowText', return_value='Alan Walker - Darkside')
	@mock.patch('win32gui.EnumWindows', return_value=None)
	def test_get_info_windows(self, mock_win32gui_1, mock_win32gui_2):
		"""
		test that get_info_windows works
		"""
		self.assertEqual(get_info_windows(), ("Alan Walker","Darkside"))
=======
>>>>>>> 0c0634871bb49d9c80985821133795f7902418e5

if __name__ == '__main__':
	unittest.main()
