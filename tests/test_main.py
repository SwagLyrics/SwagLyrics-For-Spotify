"""
Contains unit tests for __main__.py
"""
import unittest
from swaglyrics.__main__ import main
from mock import mock
import argparse
import io
import sys
import threading
from swaglyrics.tab import app

class Tests(unittest.TestCase):
    """
    Unit tests
    """

    def setup(self):
        pass

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(tab=False, cli=False))
    def test_parser_prints_description(self, mock_argparse):
        """
        Tests whether prints its description
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("Get lyrics for the currently playing song on Spotify. Either --tab or --cli is\nrequired.", capturedOutput.getvalue())

    @mock.patch('threading.Timer', side_effect=None)
    @mock.patch('swaglyrics.tab.app.run', side_effect=None)
    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(tab=True, cli=False))
    def test_parser_runs_tab(self, mock_argparse, mock_app, mock_threader):
        """
        Tests whether parser runs tab
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("Firing up a browser tab!", capturedOutput.getvalue())
        self.assertTrue(mock_app.called)

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(tab=False, cli=True))
    @mock.patch('time.sleep', side_effect=KeyboardInterrupt)
    def test_parser_runs_cli(self, mock_time, mock_argparse):
        """
        Tests whether parser runs cli
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("\n(Press Ctrl+C to quit)", capturedOutput.getvalue())


if __name__ == '__main__':
	unittest.main()
