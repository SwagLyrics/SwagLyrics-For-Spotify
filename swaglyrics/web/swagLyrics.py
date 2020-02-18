import sys
import eel
from base64 import b64encode

eel.init('web')

@eel.expose
def getLyric():
	lyrics = ""
	for line in sys.stdin:
		line = line.strip()
		lyrics += line + "<br>"
	return lyrics




eel.start('index.html',size=(1000,600))