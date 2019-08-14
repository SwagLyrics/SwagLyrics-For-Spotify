# SwagLyrics for Spotify
# Copyright (c) 2019 Aadi Bajpai
# The SwagLyrics Project


class R:
	"""
	This is a fake class created to mock requests' status code
	"""

	def __init__(self, status_code=7355608, text='google this number'):
		self.status_code = status_code
		self.text = text
