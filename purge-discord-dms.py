# Purge private DM's in Discord

# Import needed modules
import pyautogui
import time

# Just set this so that I don't gotta type as much 
pag = pyautogui

# Moving your cursor to the top left of the screen aborts this script
pag.FAILSAFE = True

# Wait 5 seconds
pag.alert('STARTING IN 5 SECONDS!')
time.sleep(5)

### MAIN FUNCTION ###
# Will go on forever until the script is quit
while True:
    # Press the up arrow key
    pag.press('up')
    # Hold ctrl + a 
    with pag.hold('ctrl'):
        pag.press('a')
    # Delete msg with backspace key
    pag.press('backspace')
    # Confirm to delete message
    pag.press('enter', presses=2)

