import platform

def get_info_windows():
	import win32gui

	windows = []

	# Older Spotify versions - simply FindWindow for "SpotifyMainWindow"
	windows.append(win32gui.GetWindowText(win32gui.FindWindow("SpotifyMainWindow", None)))

	# Newer Spotify versions - create an EnumHandler for EnumWindows and flood the list with Chrome_WidgetWin_0s
	def find_spotify_uwp(hwnd, windows):
		text = win32gui.GetWindowText(hwnd)
		if win32gui.GetClassName(hwnd) == "Chrome_WidgetWin_0" and len(text) > 0:
			windows.append(text)

	win32gui.EnumWindows(find_spotify_uwp, windows)

	while windows.count != 0:
		try:
			text = windows.pop()
		except:
			return None
		try:
			artist, track = text.split(" - ", 1)
			return artist, track
		except:
			pass

def get_info_linux():
	import dbus

	session_bus = dbus.SessionBus()
	spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify",
	                                     "/org/mpris/MediaPlayer2")
	spotify_properties = dbus.Interface(spotify_bus,
	                                    "org.freedesktop.DBus.Properties")
	metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
	track = str(metadata['xesam:title'])
	artist = str(metadata['xesam:artist'][0])
	return artist,track

def artist():
	if platform.system() == "Windows":
		try:
			return get_info_windows()[0]
		except:
			return None
	else:
		try:
			return get_info_linux()[0]
		except:
			return None

def song():
	if platform.system() == "Windows":
		try:
			return get_info_windows()[1]
		except:
			return None
	else:
		try:
			return get_info_linux()[1]
		except:
			return None
