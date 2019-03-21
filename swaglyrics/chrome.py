# pyFile to keep Track of Global variables related to Chrome Extension.


def initvariables():
    global song, artist, isChrome, isTerminal
    song = None
    artist = None
    isChrome = False
    isTerminal = False


def getChromeSong():
    global song, artist, isChrome
    return song, artist
