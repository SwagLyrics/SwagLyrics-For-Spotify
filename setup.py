import setuptools

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="swaglyrics",
    version="0.2.2",
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
    install_requires=['flask', 'requests', 'beautifulsoup4', 'pywin32; platform_system=="Windows"', 'pyobjc; platform_system=="Darwin"'],
    keywords='spotify lyrics python genius',
    classifiers=(
        "Programming Language :: Python :: 3",
        "Framework :: Flask",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: End Users/Desktop",
    ),
)
