import unittest
from SwagLyrics import stripper, lyrics


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

	def test_that_no_song_or_artist_does_not_break_stuff(self):
		self.assertEqual(lyrics(None, 'lol'), 'Nothing playing at the moment.')
		self.assertEqual(lyrics('lol', None), 'Nothing playing at the moment.')
		self.assertEqual(lyrics(None, None), 'Nothing playing at the moment.')


if __name__ == '__main__':
	unittest.main()
