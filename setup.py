import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="swaglyrics",
    version="0.0.1",
    author="Aadi Bajpai",
    author_email="aadibajpai@gmail.com",
    description="Display lyrics for currently playing song from Spotify as cli or a browser tab.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aadibajpai/SwagLyrics-For-Spotify",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ),
)