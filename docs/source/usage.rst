.. _usage:

Usage pls work
==============

It's very easy, play something on Spotify and just run this in your terminal:

    $ swaglyrics -c

The `-c` flag stands for cli, which sends lyrics straight into your terminal. 

Browser Mode
------------

SwagLyrics also has an option to display lyrics in a browser tab, in case you want to multitask like that or something.
You can do that by passing the `-t` flag:

    $ swaglyrics -t

All Arguments
-------------

    usage: swaglyrics [-h] [-t] [-c] [-n]

Either the tab or cli argument is required to output lyrics.


Arguments:

  -h, --help      show this help message and exit       
  -t, --tab       Display lyrics in a browser tab.      
  -c, --cli       Display lyrics in the command-line.   
  -n, --no-issue  Disable issue-making on cli.

