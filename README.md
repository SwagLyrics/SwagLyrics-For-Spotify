<h1 align="center">SwagLyrics-For-Spotify</h1>
<p align="center">
  <a href="https://travis-ci.org/aadibajpai/SwagLyrics-For-Spotify">
    <img src="https://travis-ci.org/aadibajpai/SwagLyrics-For-Spotify.svg?branch=master" alt="Build Status" />
  </a>
  <a href="https://ci.appveyor.com/project/TheClashster/swaglyrics-for-spotify">
    <img src="https://ci.appveyor.com/api/projects/status/a9bpa86dcx7vke0p?svg=true" alt="Build Status" />
  </a>
  <a href="https://codecov.io/gh/aadibajpai/SwagLyrics-For-Spotify">
    <img src="https://codecov.io/gh/aadibajpai/SwagLyrics-For-Spotify/branch/master/graph/badge.svg" alt="codecov" />
  </a>                                                                                                         
  <a href="https://pypi.org/project/swaglyrics/">
    <img src="https://img.shields.io/pypi/v/swaglyrics.svg" alt="PyPI" />
  </a>
  <a href="https://github.com/aadibajpai/SwagLyrics-For-Spotify">
    <img src="https://img.shields.io/github/issues-closed/aadibajpai/swaglyrics-for-spotify.svg" alt="GitHub closed issues" />
  </a>
  <a href="https://pepy.tech/project/swaglyrics">
    <img src="https://pepy.tech/badge/swaglyrics" alt="Downloads" />
  </a>
</p>

Fetches the currently playing song from Spotify on Windows, Linux and macOS and displays the lyrics in the command-line or in a browser tab.
Refreshes automatically when song changes. The lyrics are fetched from Genius.
Turns out Deezer already has this feature in-built but with `swaglyrics`, you can have it in Spotify as well.

Probably wasn't thinking when I put _Swag_ in the name (will probably be seen
by admission officers sigh) but I'm mainly trying to build this project as far as I can,
for practice and to learn and work with more technologies (learnt AJAX).

Initially developed this for personal use. Pretty much functionality oriented -- I usually develop something that I
can see helping me and other users in the same situation.
Packaged so I can first hand handle production-ready code to an extent and to make
distribution and usage easier.

---
[![Google Code-In 2018](https://raw.githubusercontent.com/CCExtractor/ccextractor-org-media/master/ext/google-code-In-2018.gif)](https://codein.withgoogle.com/)
<p align="center">
  SwagLyrics is participating in Google Code-in 2018 with CCExtractor Development!
</p>

Google Code-in is a global, online open source development & outreach contest for pre-university students aged between 13-17. Participants complete “tasks” ranging from coding, documentation, quality assurance, design, outreach and research to earn t-shirts, digital certificates, and hooded sweatshirts for their work. Grand Prize Winners receive a four day trip to Google in Mountain View, CA, USA the following summer!

We have a long and proud history of taking part in the Google Summer of Code with university students, and are excited to participate in GCI again for 3rd year with pre-university students!

Sounds interesting? Read more about it on our website [here](https://ccextractor.org/public:codein:google_code-in_2018) and on the official website [here](https://codein.withgoogle.com/).

---
## Changelog
- #### v0.2.1
    - Added Linux support
    - Added more tests
    - Set up code coverage and continuous integration
- #### v0.1.9
A GitHub issue is created automatically on the repo when an unsupported song is encountered (implemented server-side using pythonanywhere).

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
    |-- tests.py
    |-- unsupported.txt  # to log unsupported songs
|-- LICENSE.md
|-- MANIFEST.in
|-- README.md
|-- setup.py
```

## Improvements Planned
1. ~~Linux and macOS support **done**~~
2. ~~Better logging of unsupported songs, the isolated unsupported.txt is sub-optimal for multiple users since the
file will only update locally with songs which worked fine when it was just me but since I hope others use it too, I'll
try to add a better method with server support.~~
3. Better tests to test all of the functionality.
4. Perhaps a tiny app using Electron that could fit in your tray to be opened whenever you want lyrics for a song.
5. Supporting more songs, currently the program sometimes fails at remixes since while the lyrics are same as original,
 the artist is the remixer.
6. Documenting all the files.

## Screencast - SwagLyrics on Linux
<p align="center">
  <a href="http://www.youtube.com/watch?v=-rxYcXAsO1U">
    <img src="https://i.imgur.com/v3iWyia.gif" alt="Watch the video">
  </a>
</p>

## Screencast - SwagLyrics on macOS
<p align="center">
  <a href="https://www.youtube.com/watch?v=XcobDTljMdM">
    <img src="https://i.imgur.com/82DsYPd.gif" alt="Watch the video">
  </a>
</p>
