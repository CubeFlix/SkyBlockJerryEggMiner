#!python3
#
# Automatic Hypixel Skyblock Jerry Farmer
#
# Make sure player is looking at Jerry, can drop eggs into hopper, has "Drop Item" keybind changed to left click, UI size normal, and is selecting the first open slot in their hotbar.
#
# By Kevin Chen

import time
import pyautogui as p
import logging

afkcounter = 0
direction = True

screenWidth, screenHeight = p.size()
buttonprecentx, buttonprecenty = 0.65, 0.437

logging.basicConfig(format='%(asctime)s %(levelname)s : %(message)s', level=logging.DEBUG)

logging.info("Beginning 10 second delay. Please enter Minecraft and unpause the game. Pause game and move cursor to any corner of the screen to end the program.")

for i in range(1, 11):
    time.sleep(1)
    logging.info(i)
    
while True:
    logging.info("Beginning Iteration")
    time.sleep(0.1)
    p.click(button='right')
    logging.info("Pressed Jerry")
    time.sleep(0.1)
    p.moveTo(screenWidth*buttonprecentx, screenHeight*buttonprecenty)
    time.sleep(0.1)
    p.click(button='right')
    logging.info("Pressed Move Jerry")
    time.sleep(0.1)
    p.click()
    logging.info("Pressed Drop")
    logging.info("Ended Iteration")
    if afkcounter == 2:
        if direction:
            time.sleep(1)
            p.press('w')
            time.sleep(1)
        else:
            time.sleep(1)
            p.press('s')
            time.sleep(1)
            
        direction = not direction
        afkcounter = 0
    else:
        afkcounter += 1
        
        
