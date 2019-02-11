import unittest
from swaglyrics.cli import (stripper_genius,
	stripper_lyricsmode,
	stripper_google,
	lyrics,
	get_lyrics_genius,
	get_lyrics_lyricsmode,
	get_lyrics_google,
	clear,
	unsupported_song_addition
)
from mock import mock, patch
import os
import requests



class R:
	"""
	This is a fake class created to mock requests' status code
	"""
	status_code = 7355608
	text = 'google this number'
	def __init__(self, status_code=7355608, text='google this number'):
		self.status_code = status_code
		self.text = text

class Test(unittest.TestCase):
	"""
	Unit tests for the new cli
	"""

	def setup(self):
		pass

	def test_that_all_the_strippers_work(self):
		## Genius
		self.assertEqual(stripper_genius('River (feat. Ed Sheeran)', 'Eminem'), 'Eminem-River')
		self.assertEqual(
			stripper_genius(
				'CAN\'T STOP THE FEELING!'
				' (Original Song from DreamWorks Animation\'s \"TROLLS\")', 'Justin Timberlake'),
			'Justin-Timberlake-CANT-STOP-THE-FEELING')
		self.assertEqual(stripper_genius('Ain\'t My Fault - R3hab Remix', 'Zara Larsson'), 'Zara-Larsson-Aint-My-Fault')
		self.assertEqual(stripper_genius('1800-273-8255', 'Logic'), 'Logic-1800-273-8255')
		self.assertEqual(stripper_genius('Scream & Shout', 'will.i.am'), 'william-Scream-and-Shout')
		self.assertEqual(stripper_genius('Heebiejeebies - Bonus', 'Aminé'), 'Amine-Heebiejeebies')

		## LyricsMode
		self.assertEqual(stripper_lyricsmode('River (feat. Ed Sheeran)', 'Eminem'), 'e/eminem/river.html')
		self.assertEqual(
			stripper_lyricsmode(
				'CAN\'T STOP THE FEELING!'
				' (Original Song from DreamWorks Animation\'s \"TROLLS\")', 'Justin Timberlake'),
			'j/justin_timberlake/cant_stop_the_feeling.html')
		self.assertEqual(stripper_lyricsmode('Ain\'t My Fault - R3hab Remix', 'Zara Larsson'), 'z/zara_larsson/aint_my_fault.html')
		self.assertEqual(stripper_lyricsmode('1800-273-8255', 'Logic'), 'l/logic/1800-273-8255.html')
		self.assertEqual(stripper_lyricsmode('Scream & Shout', 'will.i.am'), 'w/william/scream_and_shout.html')
		self.assertEqual(stripper_lyricsmode('Heebiejeebies - Bonus', 'Aminé'), 'a/amine/heebiejeebies.html')

		##Google search
		self.assertEqual(stripper_google('River (feat. Ed Sheeran)', 'Eminem'), 'River+(feat.+Ed+Sheeran)+Eminem+lyrics')
		self.assertEqual(
			stripper_google(
				'CAN\'T STOP THE FEELING!'
				' (Original Song from DreamWorks Animation\'s \"TROLLS\")', 'Justin Timberlake'),
			'CAN%27T+STOP+THE+FEELING!+(Original+Song+from+DreamWorks+Animation%27s+"TROLLS")+Justin+Timberlake+lyrics')
		self.assertEqual(stripper_google('Ain\'t My Fault - R3hab Remix', 'Zara Larsson'), 'Ain%27t+My+Fault+-+R3hab+Remix+Zara+Larsson+lyrics')
		self.assertEqual(stripper_google('1800-273-8255', 'Logic'), '1800-273-8255+Logic+lyrics')
		self.assertEqual(stripper_google('Scream & Shout', 'will.i.am'), 'Scream+%26+Shout+will.i.am+lyrics')
		self.assertEqual(stripper_google('Heebiejeebies - Bonus', 'Aminé'), 'Heebiejeebies+-+Bonus+Aminé+lyrics')

	def test_that_no_song_or_artist_does_not_break_stuff(self):
		"""
		Test that None parameters in lyrics function does not break stuff
		"""
		self.assertEqual(lyrics(None, 'lol'), 'Nothing playing at the moment.')
		self.assertEqual(lyrics('lol', None), 'Nothing playing at the moment.')
		self.assertEqual(lyrics(None, None), 'Nothing playing at the moment.')

	def test_that_get_lyrics_works(self):
		"""
		Test that get_lyrics_genius, get_lyrics_google, get_lyrics_lyricsmode functions work
		"""
		##genius
		self.assertEqual(get_lyrics_genius("Faded", "Alan Walker")[:9], "[Verse 1]")
		self.assertEqual(get_lyrics_genius("Radioactive", "Imagine Dragons")[:7], "[Intro]")
		self.assertEqual(get_lyrics_genius("Battle Symphony", "Linkin Park")[:9], "[Verse 1]")

		## lyricsmode
		self.assertEqual(get_lyrics_lyricsmode("Faded", "Alan Walker")[:9], "[Verse 1]")
		self.assertEqual(get_lyrics_lyricsmode("Radioactive", "Imagine Dragons")[:10], "I'm waking")
		self.assertEqual(get_lyrics_lyricsmode("Battle Symphony", "Linkin Park")[:9], "[Verse 1]")
		##google
		self.assertEqual(get_lyrics_google("Faded", "Alan Walker")[:8], "You were")
		self.assertEqual(get_lyrics_google("Radioactive", "Imagine Dragons")[:9], "Whoa, oh,")
		self.assertEqual(get_lyrics_google("Battle Symphony", "Linkin Park")[:7], "I got a")

	def test_that_get_lyrics_does_not_break_with_wrong_data(self):
		"""
		Test that get_lyrics_genius, get_lyrics_google, get_lyrics_lyricsmode functions don't break with wrong data
		"""
		assert get_lyrics_genius("Battle Symphony", "One Direction") is None
		assert get_lyrics_genius("Faded", "Muhmello") is None
		assert get_lyrics_genius("Battle Symphony", "Drake") is None

		assert get_lyrics_lyricsmode("Battle Symphony", "One Direction") is None
		assert get_lyrics_lyricsmode("Faded", "Muhmello") is None
		assert get_lyrics_lyricsmode("Battle Symphony", "Drake") is None

		assert get_lyrics_google("Battle Symphony", "One Direction") is None
		assert get_lyrics_google("Faded", "Muhmello") is None
		assert get_lyrics_google("Battle Symphony", "Drake") is None



	def test_that_lyrics_works_for_unsupported_songs(self):
		"""
		Test that lyrics function gives 'unsupported' message to unsupported files
		"""
		self.assertEqual(lyrics("Hello", "World", False), "Couldn't get lyrics for Hello by World.\n")
		self.assertEqual(lyrics("Foo", "Bar", False), "Couldn't get lyrics for Foo by Bar.\n")
		self.assertEqual(lyrics("Fantastic", "Beasts", False), "Couldn't get lyrics for Fantastic by Beasts.\n")

		# Deleting above songs and artists from unsupported.txt
		with open("unsupported.txt", "r") as f:
			lines = f.readlines()
		with open("unsupported.txt", "w") as f:
			for line in lines:
				if line not in [" Hello by World \n", " Foo by Bar \n", " Fantastic by Beasts \n"]:
					f.write(line)

	def test_that_lyrics_do_not_break_with_file_not_found(self):
		"""
		test that lyrics function does not break if unsupported.txt is not found
		"""
		os.rename("unsupported.txt", "unsupported2.txt")
		self.assertEqual(lyrics("Crimes", "Grindelwald", False), "Couldn\'t get lyrics for Crimes by Grindelwald.\n")

	def test_database_for_unsupported_song(self):
		"""
		test that the database set on pythonanywhere is working and giving strippers for unsupported songs
		"""
		self.assertEqual(get_lyrics_genius("Bitch Lasagna", "Party in Backyard")[:7], "[Intro]")

	@mock.patch('requests.post', return_value=R())
	def test_that_unsupported_song_addition_does_not_break_with_request_giving_wrong_status_code(self, mock_requests):
		"""
		Test the unsupported_song_addition does not break with requests giving wrong status code
		"""
		self.assertEqual(unsupported_song_addition("Ki", "Ki", True), "Couldn\'t get lyrics for Ki by Ki.\n")


	@mock.patch('requests.post', side_effect=requests.exceptions.RequestException)
	def test_that_unsupported_song_addition_do_not_break_with_error_in_request(self, mock_requests):
		"""
		Test the unsupported_song_addition does not break with error in requests
		"""
		self.assertEqual(unsupported_song_addition("Ki", "Ki", True), "Couldn\'t get lyrics for Ki by Ki.\n")

	@mock.patch('requests.post', return_value=R(200, "Season 3 is supernatural"))
	def test_that_unsupported_song_addition_calls_requests(self, mock_requests):
		"""
		Test that unsupported_song_addition calls requests
		"""
		self.assertEqual(unsupported_song_addition("River", "Dale", True), "Couldn't get lyrics for River by Dale.\nSeason 3 is supernatural")



	@patch('os.system')
	def test_clear(self, mock):
		clear()
		self.assertTrue(mock.called)


if __name__ == '__main__':
	unittest.main()
