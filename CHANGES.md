# Changelog

- #### v1.0.1
	- Refactor cli.py to fix #1682
	- Add type annotations to cli.py
	- Bump code coverage to 90%
	- Fully mock backend API calls in unit tests
	- Add integration tests

- #### v1.0.0
	- Refactor cli.py
	- Unify backend
	- Refactor testsuite
	- Fix bug in unsupported.txt handling
	- drop support for pre Python 3.6 versions 
	- use f-strings

- #### v0.2.9
	- Added USING.txt
	- Added comparison tests on Colab
	- Improved stripper
	- Set Travis auto-push to PyPI

- #### v0.2.8
	- Fixed creation of multiple unsupported.txt
	- Improved stripper + genius_stripper on backend as fallback
	- Full test coverage for cli.py
	- Add support for local music too
	- Add coloring
	- Remove extra dependency
	
- #### v0.2.6
    - Added favicon
    - Removed extra dependency
    
- #### v0.2.5
    - Refactored stripper to support more songs straightaway
    - Fixed bugs
    - Added -n argument (helps while testing)
    - Added more test cases

- #### v0.2.4
    - Added server-side database
    - All songs with lyrics on Genius supported now!
    - Global sync of unsupported songs
    - Added more tests (85% coverage)
    - Improved issue-making using Spotify API
    
- #### v0.2.3
    - Added macOS support
    - Added more tests
    - Added unidecode to support songs with diacritics
    - Fixed commandline not clearing b/w songs on Linux
    - Improved issue-making
    
- #### v0.2.1
    - Added Linux support
    - Added more tests
    - Set up code coverage and continuous integration

- #### v0.1.9
    - A GitHub issue is created automatically on the repo when an unsupported song is encountered (implemented server-side using pythonanywhere).