import tkinter as tk
import random
import string

window=tk.Tk()
window.title("Şifre Üret")
window.geometry("300x200")
window.resizable(width=False,height=False)

def sifre_uret():
    karakterler = string.digits + string.ascii_letters
    karakterDizisi = "".join(random.choice(karakterler) for i in range(int(karakter_girme.get())))
    cıktı.delete(0,tk.END)
    cıktı.insert(0,karakterDizisi)

tag=tk.Label(window,text="Şifre Üretici",fg="green",font="sans 18 bold")
tag.pack()


karakter_girme=tk.Entry()
karakter_girme.pack()

tag1=tk.Label(window,text="Kaç karakterli istiyosun",fg="red",font="sans 13 italic")
tag1.pack()

uretme=tk.Button(window,text="Üret",fg="blue",font="sans 8 bold",command=sifre_uret)
uretme.pack()

tag2=tk.Label(window,text="Üretilen Şifre",fg="green",font="sans 13 bold")
tag2.place(x=94,y=122)


cıktı=tk.Entry()
cıktı.place(x=87,y=150)

window.mainloop()


