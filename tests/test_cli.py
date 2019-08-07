"""
Contains unit tests for cli.py
"""
import unittest
import os
import requests
from swaglyrics.cli import stripper, lyrics, get_lyrics, clear
from swaglyrics import unsupported_txt
from mock import mock, patch


class R:
	"""
	This is a fake class created to mock requests' status code
	"""

	def __init__(self, status_code=7355608, text='google this number'):
		self.status_code = status_code
		self.text = text


class Tests(unittest.TestCase):
	"""
	Unit tests
	"""

	def setup(self):
		pass

	def test_that_stripping_works(self):
		"""
		Test that stripping works
		"""
		self.assertEqual(stripper('River (feat. Ed Sheeran)', 'Eminem'), 'Eminem-River')
		self.assertEqual(stripper('Ain\'t My Fault - R3hab Remix', 'Zara Larsson'), 'Zara-Larsson-Aint-My-Fault')
		self.assertEqual(stripper('1800-273-8255', 'Logic'), 'Logic-1800-273-8255')
		self.assertEqual(stripper('Garota', 'Erlend Øye'), 'Erlend-ye-Garota')
		self.assertEqual(stripper('Scream & Shout', 'will.i.am'), 'william-Scream-and-Shout')
		self.assertEqual(stripper('Heebiejeebies - Bonus', 'Aminé'), 'Amine-Heebiejeebies')
		self.assertEqual(stripper('FRÜHLING IN PARIS', 'Rammstein'), 'Rammstein-FRUHLING-IN-PARIS')
		self.assertEqual(stripper(
			'Chanel (Go Get It) [feat. Gunna & Lil Baby]', 'Young Thug'), 'Young-Thug-Chanel-Go-Get-It')
		self.assertEqual(stripper(
			'MONOPOLY (with Victoria Monét)', 'Ariana Grande'), 'Ariana-Grande-and-Victoria-Monet-MONOPOLY')
		self.assertEqual(stripper('Seasons (with Sjava & Reason)', 'Mozzy'), 'Mozzy-Sjava-and-Reason-Seasons')
		self.assertEqual(stripper(
			'거품 안 넘치게 따라줘 [Life Is Good] (feat. Crush, Dj Friz)', 'Dynamic Duo'), 'Dynamic-Duo-Life-Is-Good')
		self.assertEqual(stripper('Ice Hotel (ft. SZA)', 'XXXTENTACION'), 'XXXTENTACION-Ice-Hotel')

	def test_that_no_song_or_artist_does_not_break_stuff(self):
		"""
		Test that None parameters in lyrics function does not break stuff
		"""
		self.assertEqual(lyrics(None, 'lol'), 'Nothing playing at the moment.')
		self.assertEqual(lyrics('lol', None), 'Nothing playing at the moment.')
		self.assertEqual(lyrics(None, None), 'Nothing playing at the moment.')

	def test_that_get_lyrics_works(self):
		"""
		Test that get_lyrics function works
		"""
		self.assertEqual(get_lyrics("Faded", "Alan Walker")[:9], "[Verse 1]")
		self.assertEqual(get_lyrics("Radioactive", "Imagine Dragons")[:7], "[Intro]")
		self.assertEqual(get_lyrics("Battle Symphony", "Linkin Park")[:9], "[Verse 1]")

	@patch('requests.get')
	def test_that_get_lyrics_does_not_break_with_wrong_data(self, fake_get):
		"""
		Test that get_lyrics function does not break with wrong data
		"""
		fake_resp = requests.Response()
		fake_resp.status_code = 404
		fake_get.return_value = fake_resp
		self.assertEqual(get_lyrics(
			"xyzzy", "Yeet"), None)
		self.assertEqual(get_lyrics("aifone", "Muhmello"), None)
		self.assertEqual(get_lyrics("Pixel2XL", "Elgoog"), None)

	def test_that_lyrics_works_for_unsupported_songs(self):
		"""
		Test that lyrics function gives 'unsupported' message to unsupported files
		"""
		lyrics("xyzzy", "Yeet", False)
		self.assertEqual(lyrics("xyzzy", "Yeet"), "Lyrics unavailable for xyzzy by Yeet.\n")
		lyrics("wiuegi", "Muhmello", False)
		self.assertEqual(lyrics("wiuegi", "Muhmello"), "Lyrics unavailable for wiuegi by Muhmello.\n")
		lyrics("Pixel2XL", "Elgoog", False)
		self.assertEqual(lyrics("Pixel2XL", "Elgoog"), "Lyrics unavailable for Pixel2XL by Elgoog.\n")

		# Deleting above songs and artists from unsupported.txt
		with open(unsupported_txt, "r") as f:
			lines = f.readlines()
		with open(unsupported_txt, "w") as f:
			for line in lines:
				if line not in ["xyzzy by Yeet \n", "wiuegi by Muhmello \n", "Pixel2XL by Elgoog \n"]:
					f.write(line)

	@patch('swaglyrics.cli.get_lyrics')
	def test_that_lyrics_calls_get_lyrics(self, mock):
		"""
		test that lyrics function calls get_lyrics function
		"""
		lyrics("Alone", "Marshmello")
		self.assertTrue(mock.called)

	def test_that_lyrics_do_not_break_with_file_not_found(self):
		"""
		test that lyrics function does not break if unsupported.txt is not found
		"""
		os.rename(unsupported_txt, "unsupported2.txt")
		self.assertEqual(lyrics("Pixel2XL", "Elgoog", False), "Couldn't get lyrics for Pixel2XL by Elgoog.\n")

	def test_database_for_unsupported_song(self):
		"""
		test that the database set on pythonanywhere is working and giving strippers for unsupported songs
		"""
		self.assertEqual(get_lyrics("Bitch Lasagna", "Party in Backyard")[:7], "[Intro]")

	@mock.patch('requests.post', return_value=R())
	def test_that_get_lyrics_does_not_break_with_request_giving_wrong_status_code(self, mock_requests):
		"""
		Test the get_lyrics does not break with requests giving wrong status code
		"""
		self.assertEqual(get_lyrics("xyzzy", "Yeet"), None)

	@mock.patch('requests.post', side_effect=requests.exceptions.RequestException)
	def test_that_get_lyrics_do_not_break_with_error_in_request(self, mock_requests):
		"""
		Test the get_lyrics does not break with error in requests
		"""
		self.assertEqual(get_lyrics("xyzzy", "Yeet"), None)

	@mock.patch('requests.post', return_value=R())
	def test_that_lyrics_does_not_break_with_request_giving_wrong_status_code(self, mock_requests):
		"""
		Test the lyrics does not break with requests giving wrong status code
		"""
		self.assertEqual(lyrics("xyzzy", "Yee"), "Couldn't get lyrics for xyzzy by Yee.\n")

	@mock.patch('requests.post', return_value=R(200, "Phone is dope"))
	def test_that_lyrics_calls_requests(self, mock_requests):
		"""
		Test that get_lyrics calls requests
		"""
		self.assertEqual(lyrics(
			"Pixel2XL", "Elgoog", True), "Couldn't get lyrics for Pixel2XL by Elgoog.\nPhone is dope")

	@patch('os.system')
	def test_clear(self, mock):
		clear()
		self.assertTrue(mock.called)


if __name__ == '__main__':
	unittest.main()
