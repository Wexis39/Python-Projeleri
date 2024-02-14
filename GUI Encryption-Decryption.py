import tkinter as tk
from tkinter import messagebox

window=tk.Tk()
window.resizable(width=False,height=False)
window.geometry("500x500")
window.title("GUI Encryption-Decryption")

def encrypt():
    data = tag2.get()
    encrypt_text = "".join(chr(ord(char) + 2) for char in data)
    tag5.delete(0.0, tk.END)
    tag5.insert(0.0, encrypt_text)
    
def decrypt():
    data2 = tag2.get()
    decrypt_text = "".join(chr(ord(char)-2) for char in data2)
    tag5.delete(0.0,tk.END)
    tag5.insert(0.0, decrypt_text)
    
    
def cikis():
    messagebox.showinfo("Exit")
    window.destroy()
    
gui=tk.Label(window, text="GUI Encryption Decryption", fg="green", font="sans 25 bold")
gui.pack()

tag1=tk.Label(window, text="Enter Text", fg="blue", font="sans 15 bold")
tag1.place(x=188,y=110)

tag2=tk.Entry(window)
tag2.place(x=180,y=150)

tag3=tk.Button(window, text="Encrypt", fg="red", font="sans 15 bold",command=encrypt)
tag3.place(x=195,y=190)

tag4=tk.Button(window, text="Decrypt", fg="red", font="sans 15 bold",command=decrypt)
tag4.place(x=195,y=250)

tag5=tk.Text(window)
tag5.place(x=0,y=355)

tag6=tk.Label(window,text="Output",fg="orange",font="sans 14 bold")
tag6.place(x=206,y=320)

tag7=tk.Button(window,text="Exit",fg="blue",font="sans 11 italic",command=cikis)
tag7.place(x=390,y=320)

window.mainloop()