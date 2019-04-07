import os
import site

def get_unsupported_path():
	default = 'unsupported.txt'
	path = os.path.join(site.getusersitepackages(), 'swaglyrics')
	if not os.access(path, os.F_OK):
		try:
			os.makedirs(path)
		except OSError as e:
			print('Could not access unsupported.txt: {}'.format(e))
			return default

	if os.access(path, os.R_OK) and os.access(path, os.W_OK):
		path = os.path.join(path, 'unsupported.txt')
		return path
	return default
