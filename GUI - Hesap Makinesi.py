import tkinter as tk

window = tk.Tk()
window.title("PYTHON HESAP MAKİNESİ")
window.geometry("350x200")
window.resizable(width=False,height=False)


def calculate():
    data = text.get()
    try:
        result=eval(data)
        result_label.config(text="Sonuç: " + str(result))
    except Exception as i:
        result_label.config(text="Hata: Geçersiz İfade")
    
    

tag = tk.Label(window, text="Hesap Makinesi", fg="red", font="sans 20 bold")
tag.pack() 

button1 = tk.Button(window, text="Hesapla",command=calculate)
button1.pack()
button1.place(x=150,y=150)

text = tk.Entry()
text.pack()

result_label = tk.Label(window, text="", fg="blue",font="sans 10 bold")
result_label.pack()


window.mainloop()