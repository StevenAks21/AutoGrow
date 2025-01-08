import pyautogui as auto
import keyboard as kb


print("Please press enter to continue..")

kb.wait("enter")


currentPosition = auto.position()
print(currentPosition)