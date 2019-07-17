import setuptools
import swaglyrics

with open("README.md", "r", encoding='utf8') as fh:
	long_description = fh.read()

setuptools.setup(
	name="swaglyrics",
	version=swaglyrics.__version__,
	author="Aadi Bajpai",
	author_email="aadibajpai@gmail.com",
	description="Fetch the currently playing song from Spotify and display the lyrics in terminal or a browser tab. "
						"Very fast.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/aadibajpai/SwagLyrics-For-Spotify",
	entry_points={'console_scripts': ['swaglyrics=swaglyrics.__main__:main']},
	packages=setuptools.find_packages(),
	license='MIT',
	include_package_data=True,
	install_requires=['SwSpotify', 'flask', 'requests', 'unidecode', 'beautifulsoup4', 'colorama'],
	keywords='spotify lyrics python genius',
	classifiers=(
		"Programming Language :: Python :: 3",
		"Framework :: Flask",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Intended Audience :: End Users/Desktop",
	),
)
