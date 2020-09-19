"""
Contains integration tests for swaglyrics
These will typically only be run once since they consume external resources
"""
import unittest

from swaglyrics.cli import get_lyrics


class Tests(unittest.TestCase):
    """
    Unit tests
    """

    def setup(self):
        pass

    # Integration test
    def test_that_get_lyrics_works(self):
        """
        Test that get_lyrics function works
        """
        self.assertEqual(get_lyrics('果てるまで', 'ハゼ馳せる'), None)  # song and artist non-latin
        self.assertEqual(get_lyrics('Hello', 'ハゼ馳せる'), None)  # artist non-latin
        self.assertEqual(get_lyrics('ハゼ馳せる果てるまで', 'ZUTOMAYO'), None)  # song non-latin
        self.assertEqual(get_lyrics("Faded", "Alan Walker")[:9], "[Verse 1]")
        self.assertEqual(get_lyrics("Radioactive", "Imagine Dragons")[:7], "[Intro]")
        self.assertEqual(get_lyrics("Battle Symphony", "Linkin Park")[:9], "[Verse 1]")

    # Integration test
    def test_database_for_unsupported_song(self):
        """
        test that the database set on pythonanywhere is working and giving strippers for unsupported songs
        """
        self.assertEqual(get_lyrics("Bitch Lasagna", "Party in Backyard")[:7], "[Intro]")
        self.assertEqual(get_lyrics("Let Me Hold You (Turn Me On)", "Cheat Codes")[:9], "[Verse 1]")
