import unittest
from swaglyrics.cli import stripper, lyrics, get_lyrics

class Tests(unittest.TestCase):

	def setUp(self):
		pass

	def test_that_stripping_works(self):
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
		self.assertEqual(lyrics(None, 'lol'), 'Nothing playing at the moment.')
		self.assertEqual(lyrics('lol', None), 'Nothing playing at the moment.')
		self.assertEqual(lyrics(None, None), 'Nothing playing at the moment.')

	def test_get_lyrics(self):
		self.assertEqual(get_lyrics("Faded", "Alan Walker")[:9],"[Verse 1]")
		self.assertEqual(get_lyrics("Radioactive", "Imagine Dragons")[:7],"[Intro]")
		self.assertEqual(get_lyrics("Battle Symphony", "Linkin Park")[:9],"[Verse 1]")

	def test_get_lyrics_wrong_data(self):
		self.assertEqual(get_lyrics("Battle Symphony", "One Direction"),"Couldn't get lyrics for Battle Symphony by One Direction.\n")
		self.assertEqual(get_lyrics("Faded", "Marshmellow"),"Couldn't get lyrics for Faded by Marshmellow.\n")
		self.assertEqual(get_lyrics("Battle Symphony", "Drake"),"Couldn't get lyrics for Battle Symphony by Drake.\n")

	def test_lyrics_unsupported(self):
		get_lyrics("Hello","World")
		self.assertEqual(lyrics("Hello","World"),"Lyrics unavailable for Hello by World.\n")
		get_lyrics("Foo","Bar")
		self.assertEqual(lyrics("Foo","Bar"),"Lyrics unavailable for Foo by Bar.\n")
		get_lyrics("Fantastic","Beasts")
		self.assertEqual(lyrics("Fantastic","Beasts"),"Lyrics unavailable for Fantastic by Beasts.\n")

if __name__ == '__main__':
	unittest.main()

