# Contributors Guide

Please read and understand this contribution guide before creating an issue or pull request related to the Windows System Tray App. Please also refer to the main contribution guide.

## How the Program Works

When the .exe file is ran it starts the main swaglyrics program with the arguement `-ta` to signify that the system tray app is being opened. When that is recieved it then runs the `systray()` function. This starts the system tray app and defines the actions taken when user interactes with the program.

## Files to Edit

### I want to change the .exe....

To do this please edit the swaglyrics.bat program [here](swaglyrics.bat). Then using [Slimm Bat to Exe](https://www.softpedia.com/get/Programming/Other-Programming-Files/Slimm-Bat-to-Exe.shtml) generate a windowless .exe. When doing so make sure you are in the /dist directory so all the files are inculded (.bat & .ico). The files should also be named swaglyrics so the program is correctly generated. After generating test that the .exe launches the system tray app as well as the program's icon being the Swag Lyrics logo.

### I want to change the final system tray program ...

This is fully generated in the systray() function which is defined [here](..\swaglyrics\systray.py). The program uses infi.systray to generate the system tray icon and menu, it then uses tkinter to generate the window generated after double clicking the icon. 

## What should I contribute?

Improvements still need to be made to this program.

- [ ] Find and intergrate an alternative to tkinter that allows for a similar exprience but can change the colour of the scrollbar (**In Windows**)
- [ ] Make the window resizeable
- [ ] Streamline the process from .exe to systray()