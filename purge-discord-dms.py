# Purge private DM's in Discord

# Import needed modules
import pyautogui    ## Install with: `pip install pyautogui`
import time

# Moving your cursor to the TOP LEFT of the screen aborts this script
pyautogui.FAILSAFE = True

# Wait 5 seconds
pyautogui.alert('STARTING IN 5 SECONDS!\nBring your cursor to the TOP LEFT of your screen to abort this script!')
time.sleep(5)

### MAIN FUNCTION ###
# Will go on forever until the script is quit
while True:
    # Press the up arrow key
    pyautogui.press('up')
    # Hold ctrl + a 
    with pyautogui.hold('ctrl'):
        pyautogui.press('a')
    # Delete msg with the backspace key
    pyautogui.press('backspace')
    # Confirm to delete the message (first press to delete the message, second press to confirm deletion)
    pyautogui.press('enter', presses=2)
