# SkyBlockJerryEggMiner

![Jerry Eggs](images/jerryeggs.PNG)

An AFK auto-clicker for Minecraft Hypixel SkyBlock.

SkyBlock has a new NPC named "Jerry", and his egg can be farmed.

This tool will automatiacally farm it.

Instructions: 
============

Download the script.

Install pyautogui (pip install pyautogui) and python (https://www.python.org/). 

Set up a contraption like this:
![Setup](images/setup.png)

Make sure player is looking at Jerry, can drop eggs into the hopper, has the "Drop Item" keybind changed to left click, has the UI size to be normal, and is selecting the first open slot in their hotbar.
Run the script. You will have a 10 second delay to get into Minecraft and face Jerry. Ensure that Minecraft is unpaused.

If it dosen't press the "Move Jerry" button, try changing the buttonprecentx and buttonprecenty values.
![Move Jerry Button](images/jerrybutton.png)

![Controls](images/controls.PNG)


Dependencies
============

Python 2-3 (https://www.python.org/)

PyAutoGui "pip install pyautogui" (https://pypi.org/project/PyAutoGUI/)
