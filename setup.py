import setuptools

import swaglyrics

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="swaglyrics",
    version=swaglyrics.__version__,
    author="Aadi Bajpai",
    author_email="aadi@swaglyrics.dev",
    description="Fetch the currently playing song from Spotify and display the lyrics in terminal or a browser tab. "
                "Very fast.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SwagLyrics/SwagLyrics-For-Spotify",
    entry_points={'console_scripts': ['swaglyrics=swaglyrics.__main__:main']},
    packages=['swaglyrics'],
    license='MIT',
    include_package_data=True,
    install_requires=[
        'SwSpotify>=1.2.0',
        'flask==2.0.1',
        'requests>=2.24.0',
        'unidecode==1.2.0',
        'beautifulsoup4==4.9.3',
        'colorama==0.4.4'
    ],
    extras_require={
        'dev': [
            'mock',
            'pytest',
            'pytest-cov',
            'blinker',
            'Werkzeug==2.0.1',  # remove this once stuff's resolved
            'flask_testing',
            'mypy'
        ]
    },
    python_requires='>=3.6',
    keywords='spotify lyrics python genius',
    project_urls={
        'Documentation': 'https://swaglyrics.dev',
        'Funding': 'https://www.paypal.me/sendclash',
        'Source': 'https://github.com/SwagLyrics/SwagLyrics-For-Spotify',
        'Tracker': 'https://github.com/SwagLyrics/SwagLyrics-For-Spotify/issues',
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Framework :: Flask",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
    ),
)
