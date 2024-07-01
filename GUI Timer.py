import tkinter as tk
from tkinter.ttk import Combobox
import time

root = tk.Tk()
root.geometry('242x140')

root.config(bg='#fab7ef')

def timer():
    current_time = time.strftime('%H:%M:%S')
    label_time.config(text=current_time)
    label_time.after(1000,timer)

label_time = tk.Label(root,bg='#b38be5',font='sans 45 bold',fg='#ffffff')
label_time.pack(padx=0,pady=0)

label = tk.Label(root,bg='#8f5bd1',font='sans 36 bold',fg='#00fe92',text='Timer')
label.pack(padx=0,pady=0,fill='x')

timer()

root.mainloop()
