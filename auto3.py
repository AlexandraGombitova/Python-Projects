import pyautogui


screenwidth, screenheight = pyautogui.size()
print(screenwidth, "x",  screenheight, sep= " ")
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, ",", currentMouseY, sep= " ")

pyautogui.hotkey("win", "m")
pyautogui.hotkey("win", "right")
pyautogui.hotkey("win", "left")