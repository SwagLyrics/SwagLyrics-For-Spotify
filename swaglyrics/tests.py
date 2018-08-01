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

	def test_that_wrong_song_or_artist_does_not_break_stuff(self):
		self.assertEqual(get_lyrics('Get Schwifty', 'lol'), 'Couldn\'t get lyrics for Get Schwifty by lol.')
		self.assertFalse(get_lyrics(
			'Get Schwifty', 'Rick Sanchez') == 'Couldn\'t get lyrics for Get Schwifty by Rick Sanchez.')


if __name__ == '__main__':
	unittest.main()
