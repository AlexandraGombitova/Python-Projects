import pyautogui
import PIL



screenwidth, screenheight = pyautogui.size()
print(screenwidth, "x",  screenheight, sep= " ")
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, ",", currentMouseY, sep= " ")

picture_1 = pyautogui.screenshot()
picture_1.save("screenshot.png")