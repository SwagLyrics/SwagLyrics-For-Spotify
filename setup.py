import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="swaglyrics",
    version="0.2.0",
    author="Aadi Bajpai",
    author_email="aadibajpai@gmail.com",
    description="Fetch the currently playing song from Spotify and display lyrics on cmd or in a browser tab.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aadibajpai/SwagLyrics-For-Spotify",
    entry_points={'console_scripts': ['swaglyrics=swaglyrics.__main__:main']},
    packages=setuptools.find_packages(),
    license='MIT',
    include_package_data=True,
    install_requires=['flask', 'pywin32', 'requests', 'beautifulsoup4'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ),
)