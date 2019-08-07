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

## Why SwagLyrics?
SwagLyrics is THE fastest and the most accurate package for getting lyrics.<a href=#footnote1 id=a1><sup>1</sup></a>

Provided optimal internet, SwagLyrics can fetch lyrics for a track in as less as 0.28s.<a href=#footnote2 id=a2><sup>2</sup></a>

It also does not require the user to generate any sort of API token (Spotify or Genius) and serves functionality 
right off the bat. This is possible as the song identification is done using our in-house library 
[SwSpotify](https://github.com/SwagLyrics/SwSpotify) which does it locally for all operating systems. 

The enhanced user experience is possible due to the [backend](https://github.com/SwagLyrics/swaglyrics-issue-maker) 
which manages creating issues for unsupported songs and then adding support for them where possible by employing various 
techniques. Any song with lyrics on Genius can be supported without any user interaction owing to the backend.
If say, lyrics do not exist for a track then subsequent playings of that track will not waste your resources in trying
to fetch lyrics, this is done by a [master list of unsupported songs](https://aadibajpai.pythonanywhere.com) which is 
handled by the backend as well. 

<a href="https://colab.research.google.com/gist/aadibajpai/439cd358b001ae7d1ba970b68f70d92b/swaglyrics_test.ipynb" id="footnote1">
1. <small>[results]</small></a> Tested against <a href=https://github.com/johnwmillr/LyricsGenius>LyricsGenius</a>, the most popular 
similar package on the US Top 50 Chart on Spotify. SwagLyrics was fractionally more accurate and 2.4x times faster. 
<a href=#a1>↩</a>
<br>
<a href="https://colab.research.google.com/gist/aadibajpai/06a596ad753007b0faea132e96f372e0/swaglyrics_test.ipynb" id="footnote2">
2. <small>[results]</small></a> Speed and accuracy benchmark using Google Colab on the Spotify US Top 50 chart. 
<a href=#a2>↩</a>

## Installation
Requires Python 3.6+. Use pip or pip3 depending on your installation. You might want to use the `--user` flag on Linux to
avoid using pip as root.
```
pip install swaglyrics
```

## Usage
`usage: swaglyrics [-h] [-t] [-c] [-n]`

Either the tab or cli argument is required to output lyrics.

Arguments:
```
  -h, --help      show this help message and exit       
  -t, --tab       Display lyrics in a browser tab.      
  -c, --cli       Display lyrics in the command-line.   
  -n, --no-issue  Disable issue-making on cli.
```
You can quit by pressing <kbd>Ctrl</kbd>+<kbd>C</kbd>.

Before using, you should check [USING.txt](swaglyrics/USING.txt) to comply with the Genius ToS. There's a copy 
included inside the package as well.

## Community
- SwagLyrics participated in [Google Code-in 2018](https://g.co/gci) with CCExtractor Development.
- SwagLyrics is participating in [Google Summer of Code 2019](https://g.co/gsoc) with CCExtractor Development. 
The selected project can be found [here](https://summerofcode.withgoogle.com/projects/#5694893526089728).

## Changelog

- #### v1.0.0
	- Refactor cli.py
	- Unify backend
	- Refactor testsuite
	- Fix bug in unsupported.txt handling
	- drop support for pre Python 3.6 versions 
	- use f-strings
	
See [CHANGES.md](CHANGES.md) for prior release notes.

## Compiling SwagLyrics for Development

- Clone the repo by `git clone https://github.com/SwagLyrics/SwagLyrics-For-Spotify.git` or use ssh.
- `cd` into the cloned repo.
- `pip install -e .` the -e flag installs it locally in editable mode.

## Improvements Planned
1. ~~Linux and macOS support **done**~~
2. ~~Better logging of unsupported songs, the isolated unsupported.txt is sub-optimal for multiple users since the
file will only update locally with songs which worked fine when it was just me but since I hope others use it too, I'll
try to add a better method with server support.~~
3. Better tests to test all of the functionality. (cli.py fully tested!)
4. Perhaps a tiny app using Electron that could fit in your tray to be opened whenever you want lyrics for a song.
5. ~~Supporting more songs, currently the program sometimes fails at remixes since while the lyrics are same as 
original,
 the artist is the remixer. **done**~~
6. Documenting all the files.

## SwagLyrics on Windows with Terminal
<p align="center">
  <img src="https://i.imgur.com/SRRbxbr.png" alt="SwagLyrics with Hyper">
</p>

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
