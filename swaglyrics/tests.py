"""
Contains unit tests
"""
import unittest
from swaglyrics.cli import stripper, lyrics, get_lyrics


class Tests(unittest.TestCase):
	"""
	Unit tests
	"""

	def setUp(self):
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

	def test_that_no_song_or_artist_does_not_break_stuff(self):
		"""
		Test that None parameters in lyrics function does not break stuff
		"""
		self.assertEqual(lyrics(None, 'lol'), 'Nothing playing at the moment.')
		self.assertEqual(lyrics('lol', None), 'Nothing playing at the moment.')
		self.assertEqual(lyrics(None, None), 'Nothing playing at the moment.')

	def test_get_lyrics_function_works(self):
		"""
		Test that get_lyrics function works
		"""
		self.assertEqual(get_lyrics("Faded", "Alan Walker")[:9], "[Verse 1]")
		self.assertEqual(get_lyrics("Radioactive", "Imagine Dragons")[:7], "[Intro]")
		self.assertEqual(get_lyrics("Battle Symphony", "Linkin Park")[:9], "[Verse 1]")

	def test_get_lyrics_function_does_not_break_with_wrong_data(self):
		"""
		Test that get_lyrics function does not break with wrong data
		"""
		self.assertEqual(get_lyrics(
			"Battle Symphony", "One Direction", False), "Couldn't get lyrics for Battle Symphony by One Direction.\n")
		self.assertEqual(get_lyrics("Faded", "Marshmello", False), "Couldn't get lyrics for Faded by Marshmello.\n")
		self.assertEqual(get_lyrics("Battle Symphony", "Drake", False), "Couldn't get lyrics for Battle Symphony by Drake.\n")

		# Deleting above lyrics from unsupported.txt
		f = open("unsupported.txt", "r")
		lines = f.readlines()
		f.close()
		f = open("unsupported.txt", "w")
		for line in lines:
			if line not in ["Battle Symphony by One Direction \n", " Battle Symphony by One Direction \n", " Faded by Marshmello \n", " Battle Symphony by Drake \n"]:
				f.write(line)
		f.close()


	def test_lyrics_gives_unsupported_message(self):
		"""
		Test that lyrics function gives 'unsupported' message to unsupported files
		"""
		get_lyrics("Hello", "World", False)
		self.assertEqual(lyrics("Hello", "World"), "Lyrics unavailable for Hello by World.\n")
		get_lyrics("Foo", "Bar", False)
		self.assertEqual(lyrics("Foo", "Bar"), "Lyrics unavailable for Foo by Bar.\n")
		get_lyrics("Fantastic", "Beasts", False)
		self.assertEqual(lyrics("Fantastic", "Beasts"), "Lyrics unavailable for Fantastic by Beasts.\n")

		# Deleting above lyrics from unsupported.txt
		f = open("unsupported.txt", "r")
		lines = f.readlines()
		f.close()
		f = open("unsupported.txt", "w")
		for line in lines:
			if line not in [" Hello by World \n", " Foo by Bar \n", " Fantastic by Beasts \n"]:
				f.write(line)
		f.close()


if __name__ == '__main__':
	unittest.main()
