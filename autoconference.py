from configparser import ConfigParser
import pyautogui
from time import sleep
# from ac_cec import *

config = ConfigParser()
config.read("config.ini")

conference_url = config.get('HANGOUTS', 'conference_url', fallback='https://hangouts.google.com')


def turn_on_tv():
    pass

def init_conference():
    turn_on_tv()
    # sleep(2)
    pyautogui.hotkey('f11') # full screen
    sleep(1)
    screenWidth, screenHeight = pyautogui.size()
    # currentMouseX, currentMouseY = pyautogui.position()
    # print(f"{screenWidth} {screenHeight} {currentMouseX} {currentMouseY}")
    # pyautogui.moveTo(100, 150)
    # pyautogui.click()
    # pyautogui.screenshot('temp.png') # save screenshot to crop the button image from here
    start_conf_but = pyautogui.locateOnScreen('boton_iniciar.png', grayscale=True, region=(100,50, 900, 400))
    print(f"button found at {start_conf_but}")
    # pyautogui.alert('Ready!')
    if start_conf_but:
        buttonx, buttony = pyautogui.center(start_conf_but)
        pyautogui.click(buttonx, buttony)
    else:
        pyautogui.click(716, 207)

if __name__ == '__main__':
    init_conference()
