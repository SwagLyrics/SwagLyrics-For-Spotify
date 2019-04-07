import os
import requests
import site

def get_unsupported_path():
    default = 'unsupported.txt'
    path = os.path.join(site.getusersitepackages(), 'swaglyrics')
    if not os.path.isdir(path):
        try:
            os.mkdir(path)
        except OSError as e:
            print('Could not access unsupported.txt: {}'.format(e))
            return default

    path = os.path.join(path, 'unsupported.txt')
    return path
