import time
import pyautogui
import stealWebsite
import pickle
import os

firstFilter = True

courseDict = {"BJJ Morning": []}

def main():
    def changeFilter():
        global firstFilter

        pyautogui.hotkey('ctrl', 'shift', 'a')
        time.sleep(0.5)
        pyautogui.hotkey('enter')
        if(not firstFilter):
            pyautogui.hotkey('space')
            pyautogui.hotkey('tab')
        firstFilter = False
        pyautogui.hotkey('space')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'shift', 'a')
        time.sleep(0.5)
        pyautogui.hotkey('enter')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'r')
        time.sleep(12)
        for _ in range(3):
            pyautogui.hotkey('tab')

    def getBJJNum(index: int):
        num = site[index][site[index].find("dirItc\">")+14:]
        return num[:num.find("</span>")]

    def getTag(index: int):
        tmp = site[index].find("dirItc\">")+12
        num = site[index][tmp]
        return num[:1]
    filterList = stealWebsite.main()

    for course in filterList:
        changeFilter()
        courseDict[course] = []

        stealWebsite.downloadSite(course+".mhtml")
        site = open(course+".mhtml", encoding="utf8").read().replace("=\n","").split("\n")
        os.remove(course+".mhtml")
        site = "".join(site).split("<tr class=")[2:-1]

        for subjectIndex in range(len(site)):
            try:
                os.remove("a.mhtml")
            except OSError:
                pass

            for _ in range(subjectIndex + 10):
                pyautogui.hotkey('tab')
            
            pyautogui.hotkey('enter')
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 's')
            time.sleep(1)
            pyautogui.hotkey("a")
            pyautogui.hotkey('enter')
            time.sleep(0.5)
            for _ in range(6):
                pyautogui.hotkey('shift','tab')
            pyautogui.hotkey('enter')

            try:
                subjectDetails = open("a.mhtml", encoding="utf8").read().replace("=\n","").split("cQOkvj")
            except:
                time.sleep(0.5)
                subjectDetails = open("a.mhtml", encoding="utf8").read().replace("=\n","").split("cQOkvj")
            os.remove("a.mhtml")

            subjectName = subjectDetails[0][subjectDetails[0].find("jcNdsM")+23:]
            subjectName = subjectName[:subjectName.find("</h2>")].split(" ")
            for i in range(len(subjectName)):
                subjectName[i] = subjectName[i].split("=D7")[1:]
                for j in range(len(subjectName[i])):
                    subjectName[i][j] = chr(int(subjectName[i][j][1:3],16)+1344) + subjectName[i][j][3:]
                subjectName[i] = "".join(subjectName[i])
            subjectName = " ".join(subjectName)


            subjectPhone = subjectDetails[1][5:]
            subjectPhone = subjectPhone[:subjectPhone.find("</p>")].replace("-", "").replace(" ","")

            subjectGender = subjectDetails[4][5:]
            subjectGender = subjectGender[:subjectGender.find("</p>")]
            
            if subjectPhone[:2] == "05":
                subjectPhone = "972" + subjectPhone[1:]
            elif subjectPhone[0] == "5":
                subjectPhone = "972" + subjectPhone
            elif subjectPhone[0] == "+972":
                subjectPhone = subjectPhone[1:]
            if getTag(subjectIndex) not in "CP":
                if course == "BJJ" and int(getBJJNum(subjectIndex)) >= 127:
                    courseDict["BJJ Morning"].append((subjectName, subjectGender, subjectPhone))
                courseDict[course].append((subjectName, subjectGender, subjectPhone))

    
    with open("./courseDict.pkl", 'wb') as f:
        pickle.dump(courseDict, f)
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.hotkey('ctrl', 'w')
    return list(courseDict.keys())