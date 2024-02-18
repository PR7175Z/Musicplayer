from tkinter import *
import tkinter as tk
from tkinter import ttk
root = Tk()
root.title("Music Player")
root.geometry("350x500")
# icon for the app
root.iconbitmap(r'D:\pythonlectures\semprojectraw\assets\images\logo.ico')
frm = ttk.Frame(root, padding=(70,20,0,0))
frm.place(relx=0.5, rely=0.5, anchor=CENTER)
frm.grid()

def enterClicked():
    searchquery.get()
    ttk.Label(frm, text="", textvariable=showsearchquery).grid(column=0, row=1)
    showsearchquery.set('Searching for ' + searchquery.get())

Progress_Bar=ttk.Progressbar(frm,orient=HORIZONTAL,length=250,mode='determinate')

def Slide():
    import time
    Progress_Bar['value'] =0
    for x in range(0, 100):
        Progress_Bar['value']+=x
        frm.update_idletasks()
        time.sleep(0.1)

Progress_Bar.grid(row=0, column=0)
Button(frm,text='Run',command=Slide).grid(row=0, column=1)

searchquery = tk.StringVar()
showsearchquery = tk.StringVar()
# entry_box = ttk.Entry(frm, textvariable=searchquery)
# entry_box.grid(column=0, row=0)
# enterbtn = ttk.Button(frm, text="Enter", command=enterClicked)
# enterbtn.grid(column=12, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=12, row=1)
root.mainloop()