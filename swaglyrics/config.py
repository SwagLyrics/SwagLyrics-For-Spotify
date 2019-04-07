import os
import platform
import site

def get_unsupported_path():
    default = 'unsupported.txt'
    if platform.system() == 'Windows':
        path = os.path.join(site.getusersitepackages(), 'swaglyrics')
    else:
        path = os.path.join(site.getsitepackages()[1], 'swaglyrics')
    if not os.path.isdir(path):
        try:
            os.mkdir(path)
        except OSError as e:
            print('Could not access unsupported.txt: {}'.format(e))
            return default

    path = os.path.join(path, 'unsupported.txt')
    return path
