import pyautogui
import time

def Mewtwo():
    pyautogui.press('f1')
    
    for j in range(0,920):
        pyautogui.press(['tab'])
        pyautogui.click(1200,550)
        time.sleep(0.5)

def Cresselia():
    pyautogui.press('f2')
    
    for j in range(0,920):
        pyautogui.press(['tab'])
        pyautogui.click(1200,550)
        time.sleep(0.5)
        
def Darkay():
    pyautogui.press('f3')
    
    for j in range(0,920):
        pyautogui.press(['tab'])
        pyautogui.click(1200,550)
        time.sleep(0.5)

pyautogui.keyDown('alt')
pyautogui.press(['tab'])
pyautogui.keyUp('alt')


for i in range(0,2):
    Mewtwo()
    Cresselia()
    Darkay()

