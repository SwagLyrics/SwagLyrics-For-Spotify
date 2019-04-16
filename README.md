<h1 align="center"><img src="https://github.com/SwagLyrics/SwagLyrics/blob/master/assets/swaglyrics_transparent.png?raw=true" alt="SwagLyrics" height=200 width=200 align="middle">SwagLyrics-For-Spotify</h1>
<p align="center">
  <a href="https://travis-ci.com/SwagLyrics/SwagLyrics-For-Spotify">
    <img src="https://travis-ci.com/SwagLyrics/SwagLyrics-For-Spotify.svg?branch=master" alt="Build Status" />
  </a>
  <a href="https://ci.appveyor.com/project/TheClashster/swaglyrics-for-spotify-yo7jh">
    <img src="https://ci.appveyor.com/api/projects/status/eon538lm2of04sll?svg=true" alt="Build Status" />
  </a>
  <a href="https://codecov.io/gh/SwagLyrics/SwagLyrics-For-Spotify">
  <img src="https://codecov.io/gh/SwagLyrics/SwagLyrics-For-Spotify/branch/master/graph/badge.svg" />
  </a>                                                                                                        
  <a href="https://pypi.org/project/swaglyrics/">
    <img src="https://img.shields.io/pypi/v/swaglyrics.svg" alt="PyPI" />
  </a>
  <a href="https://github.com/SwagLyrics/SwagLyrics-For-Spotify">
    <img src="https://img.shields.io/github/issues-closed/SwagLyrics/swaglyrics-for-spotify.svg" alt="GitHub closed issues" />
  </a>
  <a href="https://pepy.tech/project/swaglyrics">
    <img src="https://pepy.tech/badge/swaglyrics" alt="Downloads" />
  </a>
</p>

Fetches the currently playing song from Spotify on Windows, Linux and macOS and displays the lyrics in the command-line or in a browser tab.
Refreshes automatically when song changes. The lyrics are fetched from Genius.
Turns out Deezer already has this feature in-built but with `swaglyrics`, you can have it in Spotify as well.

I'm mainly trying to build this project as far as I can,
for practice and to learn and work with more technologies and platforms.

Initially developed this for personal use. Pretty much functionality oriented -- I usually develop something that I
can see helping me and other users in the same situation.
Packaged so I can first hand handle production-ready code to an extent and to make
distribution and usage easier.

## Community
- SwagLyrics participated in [Google Code-in 2018](https://g.co/gci) with CCExtractor Development.
- SwagLyrics is participating in [Google Summer of Code](https://g.co/gsoc) with CCExtractor Development. Interested? Read more about it [here](https://www.ccextractor.org/public:gsoc:swaglyrics).

## Changelog
- #### v0.2.4
    - Added server-side database
    - All songs with lyrics on Genius supported now!
    - Global sync of unsupported songs
    - Added more tests (85% coverage)
    - Improved issue-making using Spotify API
    
- #### v0.2.3
    - Added macOS support
    - Added more tests
    - Added unidecode to support songs with diacritics
    - Fixed commandline not clearing b/w songs on Linux
    - Improved issue-making
    
- #### v0.2.1
    - Added Linux support
    - Added more tests
    - Set up code coverage and continuous integration
- #### v0.1.9
    - A GitHub issue is created automatically on the repo when an unsupported song is encountered (implemented server-side using pythonanywhere).

## Installation
Requires Python3. Use pip or pip3 depending on your installation.
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
You can quit by pressing <kbd>Ctrl</kbd>+<kbd>C</kbd>

## Compiling SwagLyrics for Development

- Clone the repo by `git clone https://github.com/SwagLyrics/SwagLyrics-For-Spotify.git` or use ssh.
- `cd` into the cloned repo.
- `pip install -e .` the -e flag installs it locally in editable mode.

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

## SwagLyrics on Windows with Firefox Side-View
<p align="center">
  <img src="https://i.imgur.com/TcSpbP9.png" alt="SwagLyrics with Side-View">
</p>

## Screencast - SwagLyrics on Linux
<p align="center">
  <a href="http://www.youtube.com/watch?v=-rxYcXAsO1U">
    <img src="https://i.imgur.com/v3iWyia.gif" alt="Watch the video">
  </a>
</p>

## Screencast - SwagLyrics on macOS
<p align="center">
  <a href="https://www.youtube.com/watch?v=XcobDTljMdM">
    <img src="https://i.imgur.com/7BVWB99.gif" alt="Watch the video">
  </a>
</p>
