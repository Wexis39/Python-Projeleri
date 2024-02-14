import tkinter as tk

window = tk.Tk()
window.geometry("550x650")
window.resizable(width=False,height=False)
window.title("Rectangle Maker")


def rectangle():
    x = int(tag_x.get())
    y = int(tag_y.get())
    rectangle_text = ""
    a = "*"
    
    for i in range(y):
        rectangle_text += str(a)*x + "\n"
        tag4.config(text=rectangle_text)

        
tag1=tk.Label(window,text="Rectangle Maker",fg="green",font="comic 26 bold")
tag1.pack()

tag2=tk.Label(window,text="X Axis: ",fg="red",font="comic 16 italic")
tag2.place(x=84,y=72)

tag3=tk.Label(window,text="Y Axis: ",fg="red",font="comic 16 italic")
tag3.place(x=80,y=125)

tag3=tk.Button(window,text="MAKE",fg="black",font="comic 12 bold",command=rectangle)
tag3.place(x=340,y=100)

tag_x = tk.Entry(window)
tag_x.place(x=185,y=80)

tag_y = tk.Entry(window)
tag_y.place(x=185,y=132)

tag4=tk.Label(window,text="",fg="blue",font="comic 14")
tag4.place(x=200,y=180)

window.mainloop()