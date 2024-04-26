#Choose your favorites program/actions to launch!
import pyautogui
import subprocess
import keyboard as kb

#Put your commands below:
PEACECLICK = pyautogui.leftClick()
DOUBLE_TOROCLICK = kb.press_and_release('alt+tab')
TOROCLICK = subprocess.run([r'start', r'firefox', r'google.com'], shell=True)

