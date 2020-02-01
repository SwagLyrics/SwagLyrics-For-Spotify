"""
Contains unit tests for tab.py
"""
import flask_testing
from SwSpotify import SpotifyNotRunning
from mock import patch

from swaglyrics.tab import app


class Tests(flask_testing.TestCase):
    """
    Unit tests
    """

    def setup(self):
        pass

    def create_app(self):
        return app

    @patch('SwSpotify.spotify.current', return_value=("Blank Space", "Taylor Swift"))
    def test_lyrics_are_shown_in_tab(self, mock_song):
        """
        that that tab.py is working
        """
        with self.app.test_client() as c:
            response = c.get('/')
            self.assert_template_used("lyrics.html")

    @patch('SwSpotify.spotify.current', side_effect=SpotifyNotRunning)
    def test_no_lyrics_are_shown_in_tab(self, mock_song):
        """
        that that tab.py is working when no song playing
        """
        with self.app.test_client() as c:
            response = c.get('/')
            self.assertIn(b'Nothing playing at the moment.', response.data)

    @patch('SwSpotify.spotify.current', side_effect=SpotifyNotRunning)
    def test_songchanged_returns_no(self, mock_current):
        """
        that that songChanged can return no
        """
        with self.app.test_client() as c:
            response = c.get('/songChanged')
            self.assertEqual(response.data, b'no')

    @patch('SwSpotify.spotify.current', return_value=("Blank Space", "Taylor Swift"))
    def test_songchanged_can_raise_songplaying(self, mock_current):
        """
        that that songChanged can raise SongPlaying
        """
        with self.app.test_client() as c:
            response = c.get('/songChanged')
            self.assertEqual(response.data, b'no')

    @patch('SwSpotify.spotify.current', return_value=('Rodeo', 'Lil Nas X'))
    def test_songchanged_returns_yes(self, mock_current):
        """
        that that songChanged can return yes
        """
        with self.app.test_client() as c:
            response = c.get('/songChanged')
            self.assertEqual(response.data, b'yes')


if __name__ == '__main__':
    pass
