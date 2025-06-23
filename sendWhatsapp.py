import pickle
import pyautogui
import time
import webbrowser as web
from urllib.parse import quote
from pywhatkit.core import core
import makeMessage
from PIL import ImageGrab
import pyperclip
def main(day: str, hour: str, hugim: str):
    web.open(f"https://web.whatsapp.com")
    clip = pyperclip.paste()
    with open('courseDict.pkl', 'rb') as f:
        info = pickle.load(f)
    info = info[hugim]
    time.sleep(1)
    pyautogui.click(x=100, y=200)

    screenshot = ()
    while screenshot != (84, 101, 111):
        screenshot = ImageGrab.grab(bbox=(1848, 214, 1849, 215)).getpixel((0, 0))
        time.sleep(0.5)

    for _ in range(9):
        pyautogui.press("tab")
    for subject in info:
        # USE IF IT STOPPED AT STUDENT NUMBER <X> AND YOU WANT TO CONTINUE FROM THERE
        # if(info.index(subject) <= <X>):
        #     print(info.index(subject))
        #     continue
        pyperclip.copy(subject[2])
        time.sleep(0.5)
        pyautogui.hotkey("ctrl","v")
        screenshot = ImageGrab.grab(bbox=(1287, 275, 1297, 285))
        time.sleep(0.5)
        while (165, 176, 185) not in [screenshot.getpixel((i//10,i%10)) for i in range(100)]:
            screenshot = ImageGrab.grab(bbox=(1287, 275, 1297, 285))
            time.sleep(0.5)
        time.sleep(0.5)
        screenshot = ImageGrab.grab(bbox=(1595, 463,1605, 473))
        if (102, 119, 129) in [screenshot.getpixel((i//10,i%10)) for i in range(100)]:
            pyautogui.hotkey("ctrl","backspace")
            time.sleep(0.5)
            continue
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")
        pyperclip.copy(makeMessage.main(day,hour,hugim,subject[1]))
        pyautogui.hotkey("ctrl","v")
        pyautogui.press("enter")
        time.sleep(0.5)
        for _ in range(10):
            pyautogui.press("tab")
    pyperclip.copy(clip)
    core.close_tab()