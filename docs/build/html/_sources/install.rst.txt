.. _install:

Installation of SwagLyrics
==========================

This part of the documentation covers the installation of SwagLyrics for Spotify.
The first step to using any software package is getting it properly installed.


$ pip install swaglyrics
------------------------

To install SwagLyrics, simply run this simple command in your terminal of choice::

    $ pip install swaglyrics

SwagLyrics requires Python 3.6+. Use pip or pip3 depending on your installation. You might want to use the --user flag on Linux to avoid using pip as root.

Cool kids these days recommend doing :bash:`python -m pip install swaglyrics`, but either work.

Living on the edge
-------------------

SwagLyrics is actively developed on GitHub, where the code is
`always available <https://github.com/SwagLyrics/SwagLyrics-For-Spotify>`_. It contains the latest code before it is released but should `hopefully` always work.

You can clone the public repository::

    $ git clone git://SwagLyrics/SwagLyrics-For-Spotify.git

Once you have a copy of the source, you can embed it in your own Python
package, or install it into your site-packages easily::

    $ cd SwagLyrics-For-Spotify
    $ pip install .