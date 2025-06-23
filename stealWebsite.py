import webbrowser
import time
import pyautogui
import os
import ctypes
def downloadSite(name: str):
    try:
        os.remove(name)
    except OSError:
        pass
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    for i in name:
        pyautogui.hotkey(i)
    pyautogui.hotkey('enter')
    time.sleep(1)

def disableFilters():
    global filterList
    for _ in range(9):
        pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    time.sleep(1)
    downloadSite(os.path.abspath("") + "\\filterCheck.mhtml")

    # FIND THE ACTIVATED FILTERS
    filterMap = []
    i = 0
    while len(filterMap) == 0:
        i += 1
        try:
            filterMap = ["eAGzZj" in c for c in open("./filterCheck.mhtml", encoding="utf8").read().replace("=\n","").split("\n")[i].split("kmjwzs")[1:]]
        except:
            filterMap = []
    
    # GO TO THE FILTERS TAB
    tmp = "".join(open("./filterCheck.mhtml", encoding="utf8").read().replace("=\n","").split("\n")[i-1:i+2])
    os.remove("./filterCheck.mhtml")
    for _ in range(tmp.count("jnkcEN") + tmp.count("bJlvfU") + 5):
        pyautogui.hotkey('tab')

    # ON THE WAY, GET THE FILTERS' NAMES
    filterList = [c[:c.find("</")] for c in tmp.split("iFZhTj regular\">")[1:]]

    # DISABLE FILTERS
    for i in range(len(filterMap)):
        if filterMap[i]:
            pyautogui.hotkey('space')
        pyautogui.hotkey('tab')
    for _ in range(len(filterMap)):
        pyautogui.hotkey('shift','tab')


def main():
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    while user32.GetKeyboardLayout(user32.GetWindowThreadProcessId(user32.GetForegroundWindow(), 0)) != 67699721:
        pyautogui.hotkey('shift','alt')

    # OPEN SITE
    webbrowser.open("https://yalab-plasticity20-icmw.glide.page/dl/d8fc49")
    time.sleep(1)
    pyautogui.click(x=100, y=200)
    time.sleep(9)

    # DISABLE FILTERS AND GO TO FILTER TAB
    disableFilters()
    time.sleep(1)

    # OPEN SECOND SITE
    webbrowser.open("https://yalab-plasticity20-icmw.glide.page/dl/d8fc49")
    time.sleep(15)

    return filterList