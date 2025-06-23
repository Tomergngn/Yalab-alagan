from customtkinter import *
import sendWhatsapp
import stealEverySubject
import pickle
with open('courseDict.pkl', 'rb') as handle:
    courseDict = pickle.load(handle)

app = CTk()
app.geometry("600x400")

courseList = list(courseDict.keys())

def send_messages():
    sendWhatsapp.main(str(date.get()),hour.get("1.0","end-1c"),hugim.get())

def update_subjects():
    courseList = stealEverySubject.main()
    hugim.configure(values=courseList)
frame_2 = CTkFrame(master=app, fg_color="#7C7DA7")
frame_2.grid(row=0, column=1, padx=50, pady=50)

CTkLabel(master=frame_2, text="עדכון פרטי סטודנטים", font=("Arial Bold", 20), justify="left").pack(expand=True, pady=(30, 15))
CTkButton(master=frame_2, text="עדכון", fg_color="#606190", border_color="#ffffff", command=update_subjects).pack(expand=True, side="left", padx=20, pady=(20, 50))

frame_1 = CTkFrame(master=app, fg_color="#CD8C67",height=300)
frame_1.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=50, pady=50)
CTkLabel(master=frame_1, text="שליחת הודעה", font=("Arial Bold", 20), justify="left").pack(expand=True, pady=[10, 10])
CTkLabel(master=frame_1, text="תאריך", font=("Arial", 15), justify="left").pack(expand=True, pady=(0, 0))
date = CTkOptionMenu(master=frame_1, fg_color="#C06F41",values=["מחר","ראשון"])
hour = CTkTextbox(master=frame_1, height=15, font=("Arial", 15))
hugim = CTkOptionMenu(master=frame_1, fg_color="#C06F41",values=courseList)
btn = CTkButton(master=frame_1, fg_color="#C06F41", text="שלח הודעות", font=("Arial", 15), command=send_messages)
date.pack(padx=10, pady=10)
CTkLabel(master=frame_1, text="שעה", font=("Arial", 15), justify="left").pack(expand=True,pady=(0, 0))
hour.pack(expand=True, pady=(0, 0),padx=10)
hugim.pack(expand=True, pady=20)
btn.pack(expand=True,pady=(0, 10))
app.mainloop()