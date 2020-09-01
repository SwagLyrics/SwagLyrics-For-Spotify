"""
Contains unit tests for cli.py
"""
import os
import unittest

import requests
from mock import patch

from swaglyrics import unsupported_txt
from swaglyrics.cli import stripper, lyrics, get_lyrics, clear
from tests.base import R


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
		self.assertEqual(stripper("Ain't My Fault - R3hab Remix", 'Zara Larsson'), 'Zara-Larsson-Aint-My-Fault')
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
		self.assertEqual(stripper('Zikr (From "Amavas")', 'Armaan Malik'), 'Armaan-Malik-Zikr')

	@patch('swaglyrics.cli.requests.get')
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
		self.assertEqual(get_lyrics("Pixel2XL", "Goog-el"), None)

	@patch('swaglyrics.cli.get_lyrics')
	def test_that_lyrics_works_for_unsupported_songs(self, fake_get_lyrics):
		"""
		Test that lyrics function gives 'unsupported' message to unsupported files
		"""
		fake_get_lyrics.return_value = None
		lyrics("Pixel2XL", "Elgoog", False)
		self.assertEqual(lyrics("Pixel2XL", "Elgoog"), "Lyrics unavailable for Pixel2XL by Elgoog.\n")

		# Deleting above songs and artists from unsupported.txt
		with open(unsupported_txt, "r") as f:
			lines = f.readlines()
		with open(unsupported_txt, "w") as f:
			for line in lines:
				if line not in ["Pixel2XL by Elgoog \n"]:
					f.write(line)

	@patch('swaglyrics.cli.get_lyrics')
	def test_that_lyrics_calls_get_lyrics(self, mock):
		"""
		test that lyrics function calls get_lyrics function
		"""
		lyrics("Alone", "Marshmello")
		self.assertTrue(mock.called)

	@patch('swaglyrics.cli.get_lyrics')
	def test_that_lyrics_do_not_break_with_file_not_found(self, fake_get_lyrics):
		"""
		test that lyrics function does not break if unsupported.txt is not found
		"""
		fake_get_lyrics.return_value = None
		os.rename(unsupported_txt, "unsupported2.txt")
		resp = lyrics("Pixel2XL", "Elgoog", False)
		self.assertEqual(resp, "Couldn't get lyrics for Pixel2XL by Elgoog.\n")

	@patch('swaglyrics.cli.requests.post', return_value=R())
	@patch('swaglyrics.cli.get_lyrics', return_value=None)
	def test_that_lyrics_does_not_break_with_request_giving_wrong_status_code(self, f_get_lyrics, mock_requests):
		"""
		Test lyrics does not break with requests giving wrong status code
		"""
		self.assertEqual(lyrics("xyzzy", "Yello", True), "Couldn\'t get lyrics for xyzzy by Yello.\n")

	# TODO: reenable this one after adding logging
	# @patch('requests.post', side_effect=requests.exceptions.RequestException)
	# def test_that_lyrics_do_not_break_with_error_in_request(self, mock_requests):
	# 	"""
	# 	Test the lyrics does not break with error in requests
	# 	"""
	# 	self.assertEqual(lyrics("xyzzy", "Yeet", True), "Couldn\'t get lyrics for xyzzy by Yeet.\n")

	@patch('swaglyrics.cli.requests.post', return_value=R(200, "Phone is dope"))
	@patch('swaglyrics.cli.get_lyrics', return_value=None)
	def test_that_lyrics_calls_requests(self, f_get_lyrics, mock_requests):
		"""
		Test that get_lyrics calls requests when not a trivial case 
		"""
		self.assertEqual(lyrics(
			"Pixel2XL!", "Elgoog", True), "Couldn't get lyrics for Pixel2XL! by Elgoog.\nPhone is dope")
		self.assertEqual(lyrics(
			"Pixel2XL", "Elgoog", True), "Couldn't get lyrics for Pixel2XL by Elgoog.\n")

	@patch('swaglyrics.cli.requests.post', return_value=R(404))
	@patch('swaglyrics.cli.get_lyrics', return_value=None)
	def test_that_lyrics_requests_can_fail(self, f_get_lyrics, mock_requests):
		"""
		Test that when get_lyrics calls requests and it does not succeed it doesn't append r.text
		"""
		self.assertEqual(lyrics(
			"Pixel2XL!", "Elgoog", True), "Couldn't get lyrics for Pixel2XL! by Elgoog.\n")

	@patch('os.system')
	def test_clear(self, mock):
		clear()
		self.assertTrue(mock.called)


if __name__ == '__main__':
	unittest.main()
