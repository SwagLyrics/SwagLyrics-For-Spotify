# SwagLyrics-For-Spotify 
![PyPI](https://img.shields.io/pypi/v/swaglyrics.svg)

Fetches the currently playing song from Spotify on Windows and displays the lyrics on cmd or in a browser tab.
Refreshes automatically when song changes. The lyrics are fetched from Genius.
Turns out Deezer already has this feature in-built but with `swaglyrics`, you can have it in Spotify as well.

Probably wasn't thinking when I put _Swag_ in the name (Imagine if this project ends on my CV and will probably be seen 
by admission officers and the likes) but I'm mainly trying to build this project as far as I can, 
for practice and to learn more and more stuff.

Initially developed this for personal use. Pretty much functionality oriented -- I usually develop something that I
can see helping me and other users in the same situation. 
Made it into a package so I can first hand see how production-ready code looks like to an extent and to make 
distribution and usage easier.

## Installation
```
pip install swaglyrics
```
Make sure to use a version >= 0.1.6 since the previous ones don't have the `tab` option supported.

## Usage
`swaglyrics [-h] [-t] [-c]`

Either the tab or cli argument is required to output lyrics.

Arguments:
```
  -h, --help  show this help message and exit
  -t, --tab   Display lyrics in a browser tab.
  -c, --cli   Display lyrics in the command-line.
```

## Package Structure
```
.
|-- swaglyrics
    |-- static  # contains styling and the AJAX script needed to dynamically refresh browser tab with new lyrics
    |-- templates  # contains template for the browser tab
    |-- __init__.py
    |-- __main__.py  # holds primary function that parses args and executes accordingly
    |-- cli.py  # defines functions to fetch lyrics from Genius
    |-- spotify.py  # defines functions to get currently playing song and artist from the Spotify app
    |-- tab.py  # Flask app to display lyrics in a browser tab
    |-- tests.py    # need overhauling
    |-- unsupported.txt  # to log unsupported songs, will be updated soon
|-- LICENSE.md
|-- MANIFEST.in
|-- README.md
|-- setup.py
```

## Improvements Planned
1. MacOS support
2. Better logging of unsupported songs, the isolated unsupported.txt is sub-optimal for multiple users since the
file will only update locally with songs which worked fine when it was just me but since I hope others use it too, I'll
try to add a better method with server support.
3. Better tests to test all of the functionality.
4. Perhaps a tiny app using Electron that could fit in your tray to be opened whenever you want lyrics for a song.
5. Supporting more songs, currently the program sometimes fails at remixes since while the lyrics are same as original,
 the artist is the remixer.
6. Documenting all the files.



