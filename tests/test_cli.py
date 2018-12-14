"""
Contains unit tests for cli.py
"""
import unittest
from swaglyrics.cli import stripper, lyrics, get_lyrics
from mock import patch
import os

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
		self.assertEqual(
			stripper(
				'CAN\'T STOP THE FEELING!'
				' (Original Song from DreamWorks Animation\'s \"TROLLS\")', 'Justin Timberlake'),
			'Justin-Timberlake-CANT-STOP-THE-FEELING')
		self.assertEqual(stripper('Ain\'t My Fault - R3hab Remix', 'Zara Larsson'), 'Zara-Larsson-Aint-My-Fault')
		self.assertEqual(stripper('1800-273-8255', 'Logic'), 'Logic-1800-273-8255')
		self.assertEqual(stripper('Scream & Shout', 'will.i.am'), 'william-Scream-and-Shout')
		self.assertEqual(stripper('Heebiejeebies - Bonus', 'Aminé'), 'Amine-Heebiejeebies')

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

	def test_that_get_lyrics_does_not_break_with_wrong_data(self):
		"""
		Test that get_lyrics function does not break with wrong data
		"""
		self.assertEqual(get_lyrics(
			"Battle Symphony", "One Direction", False), "Couldn't get lyrics for Battle Symphony by One Direction.\n")
		self.assertEqual(get_lyrics("Faded", "Muhmello", False), "Couldn't get lyrics for Faded by Muhmello.\n")
		self.assertEqual(get_lyrics("Battle Symphony", "Drake", False), "Couldn't get lyrics for Battle Symphony by Drake.\n")

		# Deleting above songs and artists from unsupported.txt
		with open("unsupported.txt", "r") as f:
			lines = f.readlines()
		with open("unsupported.txt", "w") as f:
			for line in lines:
				if line not in [" Battle Symphony by One Direction \n", " Faded by Muhmello \n", " Battle Symphony by Drake \n"]:
					f.write(line)

	def test_that_lyrics_works_for_unsupported_songs(self):
		"""
		Test that lyrics function gives 'unsupported' message to unsupported files
		"""
		get_lyrics("Hello", "World", False)
		self.assertEqual(lyrics("Hello", "World"), "Lyrics unavailable for Hello by World.\n")
		get_lyrics("Foo", "Bar", False)
		self.assertEqual(lyrics("Foo", "Bar"), "Lyrics unavailable for Foo by Bar.\n")
		get_lyrics("Fantastic", "Beasts", False)
		self.assertEqual(lyrics("Fantastic", "Beasts"), "Lyrics unavailable for Fantastic by Beasts.\n")

		# Deleting above songs and artists from unsupported.txt
		with open("unsupported.txt", "r") as f:
			lines = f.readlines()
		with open("unsupported.txt", "w") as f:
			for line in lines:
				if line not in [" Hello by World \n", " Foo by Bar \n", " Fantastic by Beasts \n"]:
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
		os.rename("unsupported.txt", "unsupported2.txt")
		self.assertEqual(lyrics("Crimes", "Grindelwald", False), "Couldn\'t get lyrics for Crimes by Grindelwald.\n")

	def test_database_for_unsupported_song(self):
		"""
		test that the database set on pythonanywhere is working and giving strippers for unsupported songs
		"""
		self.assertEqual(get_lyrics("Bitch Lasagna", "Party in Backyard")[:7], "[Intro]")

if __name__ == '__main__':
	unittest.main()
