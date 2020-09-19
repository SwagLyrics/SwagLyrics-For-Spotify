import sys
from os import getenv
from pathlib import Path


# create unsupported.txt in os specific user directory
# doc: https://github.com/ActiveState/appdirs/blob/master/appdirs.py#L44 derivative
def user_data_dir(file_name):
    r"""
    Get OS specific data directory path for SwagLyrics.

    Typical user data directories are:
        macOS:    ~/Library/Application Support/SwagLyrics
        Unix:     ~/.local/share/SwagLyrics   # or in $XDG_DATA_HOME, if defined
        Win 10:   C:\Users\<username>\AppData\Local\SwagLyrics
    For Unix, we follow the XDG spec and support $XDG_DATA_HOME if defined.
    :param file_name: file to be fetched from the data dir
    :return: full path to the user-specific data dir
    """
    # get os specific path
    if sys.platform.startswith("win"):
        os_path = getenv("LOCALAPPDATA")
    elif sys.platform.startswith("darwin"):
        os_path = "~/Library/Application Support"
    else:
        # linux
        os_path = getenv("XDG_DATA_HOME", "~/.local/share")

    # join with SwagLyrics dir
    path = Path(os_path) / "SwagLyrics"

    return path.expanduser() / file_name


name = 'swaglyrics'
__version__ = '1.2.2'
backend_url = 'https://api.swaglyrics.dev'
api_timeout = 10
genius_timeout = 20
unsupported_txt = user_data_dir("unsupported.txt")

# create unsupported.txt if it doesn't exist
unsupported_txt.parent.mkdir(parents=True, exist_ok=True)
unsupported_txt.touch(exist_ok=True)


class SameSongPlaying(Exception):
    pass
