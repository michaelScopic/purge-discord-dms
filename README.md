# Purge Discord DM's
A Python script to purge all of your messages in a server/DM

This repo will not see many updates (if any), but bug reports are still welcome.

### !! SEE TIPS SECTION BEFORE RUNNING THE SCRIPT !!

## Requirements 

- A Windows/MacOS/Linux system with >= Python 3.9 (written and tested on at least 3.11).
- Python pip installed (look up how to install it if you don't already have it).
- pyautogui installed:
```bash
pip install pyautogui
```

## Tips

From my usage, **this script can get buggy if a user presses certain keys/mouse placements which could cause you to go into different channels/DM's and REALLY fuck you up,** so I recommend you to install [BetterDiscord](https://betterdiscord.app/) as well as the [Hide Channels plugin](https://betterdiscord.app/plugin/Hide%20Channels). 

Go into the channel/DM that you want to purge and then hit `Ctrl` + `H` to hide channels so that there's no way you could click on another DM, and then start the script.

### TO KILL THE SCRIPT

___`Bring your cursor to the **TOP LEFT** of your screen and wait 1-3 seconds and the script will automatically quit.`___

## Downloading and running the script

__!! PLEASE READ THESE CAREFULLY, FAILURE TO DO SO MAY END UP IN PURGING MESSAGES IN THE WRONG CHANNEL/DM. !!__

To download the script, you can either clone this repo in the command line with `git` or download it as a [.zip file]() and place the `purge-discord-dms.py` file into your Downloads folder.

**SUPER IMPORTANT: In Discord, go to the channel/DM you want to purge.**

### Windows users

If you are using Windows, hit `Win` + `R` and type `cmd` and then hit the `Enter` key.

Open the file manager with `Win` + `E` and find the script you just downloaded from here.

Type `python` (don't forget the space after) and then drag the script into the cmd window, and then hit `Enter`.

This is an example of what it should look like (THIS IS NOT REFLECTIVE OF EXACTLY WHAT YOU WILL SEE/TYPE):
```cmd
python C:\Users\xxxx\Downloads\purge-discord-dms.py
```

Quickly `Alt` + `Tab` into the Discord window (or click on the Discord window) and wait 5 seconds, and the bot will start running.

### Linux users

If you are using Linux (any distro will work), bring up a terminal and go to the directory where you placed my script.

Run this command and hit `Enter`:
```sh
python3 ./purge-discord-dms.py
```

Quickly change the window focus to Discord and wait 5 seconds and the script will start running.

### MacOS users

If you are using MacOS, press `⌘` + `Spacebar` (⌘ is the Command key), and search for terminal and hit `Enter`.

If you placed my script in the Downloads folder, type this in to change directory to `Downloads/`:
```sh
cd ~/Downloads`
```

Then type this command and hit `Enter`:
```sh
python3 ./purge-discord-dms.py
```

Quickly click on the Discord window and wait 5 seconds and the script will start running.


### TO KILL THE SCRIPT

___`Bring your cursor to the **TOP LEFT** of your screen and wait 1-3 seconds and the script will automatically quit.`___
