"""
Contains unit tests for __main__.py
"""
import argparse
import io
import sys
import unittest
import time

import requests
from SwSpotify import SpotifyNotRunning
from mock import patch

from swaglyrics import SameSongPlaying
from swaglyrics.__main__ import main, unsupported_precheck, unsupported_txt
from tests.base import R


def unsupported_txt_data():
    with open(unsupported_txt, 'r') as f:
        data = f.read()
    return data


class Tests(unittest.TestCase):
    """
    Unit tests
    """

    def setup(self):
        pass

    @patch('swaglyrics.__main__.version', '0.2.6')
    @patch('swaglyrics.__main__.requests.get')
    def test_that_unsupported_precheck_works_normally(self, fake_get):
        fake_txt = 'unsupported txt test'
        fake_get.side_effect = [R(200, '0.2.9'), R(200, fake_txt)]
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        unsupported_precheck(force=True)
        update_time = time.time()  # get current time to compare with update time from the function
        sys.stdout = sys.__stdout__
        self.assertIn("New version of SwagLyrics available: v0.2.9\nPlease update :)", capturedOutput.getvalue())
        self.assertIn("Updated unsupported.txt successfully.", capturedOutput.getvalue())
        data = unsupported_txt_data().splitlines()
        time_from_txt = float(data[0])  # get actual updation time from file
        test_txt = data[1]
        self.assertEqual(test_txt, fake_txt)
        self.assertAlmostEqual(update_time, time_from_txt, delta=1)  # allow 1s mismatch

    @patch('swaglyrics.__main__.requests.get')
    def test_unsupported_precheck_handles_value_error(self, fake_get):
        """
        checks ValueError raised when first line isn't a float gets handled.
        """
        with open(unsupported_txt, 'w') as f:
            f.write('random string')  # not a float
        fake_get.side_effect = requests.exceptions.RequestException
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        unsupported_precheck()
        self.assertNotIn("New version of SwagLyrics available:", capturedOutput.getvalue())
        self.assertIn("Could not update unsupported.txt successfully.", capturedOutput.getvalue())

    @patch('swaglyrics.__main__.time.time')
    def test_that_unsupported_precheck_initial_check_handles_permission_error(self, f_time):
        # we use time to raise PermissionError although irl it will be raised by file i/o
        f_time.side_effect = PermissionError
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        with self.assertRaises(SystemExit) as se:
            unsupported_precheck()
        sys.stdout = sys.__stdout__
        self.assertEqual(se.exception.code, 1)
        self.assertIn("You should install SwagLyrics as --user or use sudo to access unsupported.txt.",
                      capturedOutput.getvalue())

    @patch('swaglyrics.__main__.requests.get')
    def test_that_unsupported_precheck_works_on_requests_errors(self, fake_get):
        fake_get.side_effect = requests.exceptions.RequestException
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        unsupported_precheck(force=True)
        sys.stdout = sys.__stdout__
        self.assertNotIn("New version of SwagLyrics available:", capturedOutput.getvalue())
        self.assertIn("Could not update unsupported.txt successfully.", capturedOutput.getvalue())

    @patch('swaglyrics.__main__.version', '1.0.0')
    @patch('swaglyrics.__main__.requests.get')
    def test_that_unsupported_precheck_works_on_permission_error(self, fake_get):
        fake_get.side_effect = [R(200, '0.2.6'), PermissionError]
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        with self.assertRaises(SystemExit) as se:
            unsupported_precheck(force=True)
        sys.stdout = sys.__stdout__
        self.assertEqual(se.exception.code, 1)
        self.assertNotIn("New version of SwagLyrics available:", capturedOutput.getvalue())
        self.assertIn("You should install SwagLyrics as --user or use sudo to access unsupported.txt.",
                      capturedOutput.getvalue())

    def test_that_unsupported_precheck_does_not_update_under_a_day(self):
        with open(unsupported_txt, 'w') as f:
            f.write(str(time.time()))
        val = unsupported_precheck()
        self.assertIsNone(val)

    @patch('swaglyrics.__main__.requests.get')
    def test_that_unsupported_precheck_updates_after_a_day(self, fake_get):
        fake_get.side_effect = requests.exceptions.RequestException
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        with open(unsupported_txt, 'w') as f:
            f.write(str(time.time() - 86500))  # more than a day
        unsupported_precheck()
        sys.stdout = sys.__stdout__
        self.assertTrue(fake_get.called)
        self.assertIn("Could not update unsupported.txt successfully.", capturedOutput.getvalue())

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(tab=False, cli=False))
    def test_parser_prints_description(self, mock_argparse):
        """
        Tests whether prints its description
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        main()
        sys.stdout = sys.__stdout__
        # the newline is necessary since argparse wraps it there in terminal
        self.assertIn("Get lyrics for the currently playing song on Spotify. Either --tab or --cli is\nrequired.",
                      capturedOutput.getvalue())

    @patch('webbrowser.open')
    @patch('threading.Timer', side_effect=None)
    @patch('swaglyrics.tab.app.run', side_effect=None)
    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(tab=True, cli=False, no_issue=False,
                                                                                 update_check=False))
    def test_parser_runs_tab(self, mock_argparse, mock_app, mock_timer, mock_browser):
        """
        Tests whether parser runs tab
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("Firing up a browser tab!", capturedOutput.getvalue())
        self.assertTrue(mock_app.called)

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(tab=False, cli=True, no_issue=True,
                                                                                 update_check=False))
    @patch('swaglyrics.__main__.spotify.current')
    @patch('swaglyrics.cli.get_lyrics')
    @patch('swaglyrics.__main__.unsupported_precheck')
    def test_parser_cli_changes_song(self, f_precheck, fake_lyrics, fake_spotify, mock_argparse):
        """
        Tests whether parser runs cli properly
        """
        outputs = [('Hello', 'Adele'), ('Panini', 'Lil Nas X'), ('Panini', 'Lil Nas X'),
                   SpotifyNotRunning, KeyboardInterrupt]
        fake_spotify.side_effect = outputs
        fake_lyrics.side_effect = ['Yello', 'Bruhnini']
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        with self.assertRaises(SystemExit):
            main()
        sys.stdout = sys.__stdout__
        self.assertIn("\n(Press Ctrl+C to quit)", capturedOutput.getvalue())
        self.assertIn("\nYello", capturedOutput.getvalue())
        self.assertIn("Bruhnini", capturedOutput.getvalue())
        self.assertIn("\nSure boss, exiting.", capturedOutput.getvalue())

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(tab=False, cli=True, no_issue=True,
                                                                                 update_check=False))
    @patch('swaglyrics.__main__.spotify.current')
    @patch('swaglyrics.__main__.unsupported_precheck')
    def test_parser_cli_works_when_spotify_not_playing(self, f_precheck, fake_spotify, mock_argparse):
        """
        Tests whether parser prints Nothing Playing initially
        """
        outputs = [SpotifyNotRunning, KeyboardInterrupt]
        fake_spotify.side_effect = outputs
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        with self.assertRaises(SystemExit):
            main()
        sys.stdout = sys.__stdout__
        self.assertIn("\n(Press Ctrl+C to quit)", capturedOutput.getvalue())
        self.assertIn("Spotify appears to be paused or closed at the moment.", capturedOutput.getvalue())
        self.assertIn("\nSure boss, exiting.", capturedOutput.getvalue())

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(tab=False, cli=True, no_issue=True,
                                                                                 update_check=False))
    @patch('swaglyrics.__main__.spotify.current')
    @patch('swaglyrics.cli.get_lyrics', return_value='Bruhnini')
    @patch('swaglyrics.__main__.unsupported_precheck')
    def test_parser_cli_works_when_same_song_playing(self, f_precheck, fake_lyrics, fake_spotify, mock_argparse):
        """
        Tests whether parser cli can raise SongNotPlaying
        """
        outputs = [('Panini', 'Lil Nas X'), ('Panini', 'Lil Nas X'), KeyboardInterrupt]
        fake_spotify.side_effect = outputs
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        with self.assertRaises((SystemExit, SameSongPlaying)):
            main()
        sys.stdout = sys.__stdout__
        self.assertIn("Bruhnini", capturedOutput.getvalue())
        self.assertIn("\nSure boss, exiting.", capturedOutput.getvalue())


if __name__ == '__main__':
    unittest.main()
