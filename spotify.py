import win32gui


def get_info_windows():
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


def artist():
	try:
		return get_info_windows()[0]
	except:
		return None


def song():
	try:
		return get_info_windows()[1]
	except:
		return None