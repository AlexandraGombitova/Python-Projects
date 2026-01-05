import pyautogui


screenwidth, screenheight = pyautogui.size()
print(screenwidth, "x",  screenheight, sep= " ")
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, ",", currentMouseY, sep= " ")

pyautogui.moveTo(150, 150)
pyautogui.click()

