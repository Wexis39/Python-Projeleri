import tkinter as tk

form = tk.Tk()

form.title('Login App')

form.geometry('550x400+650+300')

form.resizable(width=False,height=False)

def registerSystem():
    global nickname
    global password
    nickname = nickname_entry.get()
    password = password_entry.get()
    if len(nickname) > 7 and len(password) > 7:
        if nickname.strip() == '' or password.strip() == '':
            check_label.config(text='Registration Failed',fg='red')
            check_label.place(x=200,y=200)
        else:
            check_label.config(text='Registration Successful', fg='green')
            check_label.place(x=180, y=200)
            password_entry.delete(0,'end')
            nickname_entry.delete(0,'end')
    else:
        check_label.config(text='Must be 7 digits',fg='red')
        check_label.place(x=210,y=200)
        password_entry.delete(0,'end')
        nickname_entry.delete(0,'end')

def loginSystem():
    try:
        if len(nickname) > 7 and len(password) > 7:
            if nickname.strip() == '' or password.strip() == '':
                check_label.config(text='Login Failed',fg='red')
                check_label.place(x=225,y=200)
                password_entry.delete(0,'end')
                nickname_entry.delete(0,'end')

            if nickname == nickname_entry.get() and password == password_entry.get():
                check_label.config(text='Login Successful',fg='green')
                check_label.place(x=208,y=200)
            else:
                check_label.config(text='Login Failed',fg='red')
                check_label.place(x=225,y=200)
                password_entry.delete(0,'end')
                nickname_entry.delete(0,'end')
    except:
            check_label.config(text='Login Failed',fg='red')
            check_label.place(x=225,y=200)
            password_entry.delete(0,'end')
            nickname_entry.delete(0,'end')

#BUTTONS
login_buton = tk.Button(form,text='Login',bg='blue',fg='white',font='sans 20 bold',command=loginSystem)
login_buton.place(x=224,y=260)

register_buton = tk.Button(form,text='Register',bg='blue',fg='white',font='sans 20 bold',command=registerSystem)
register_buton.place(x=204,y=320)

#ENTRYS
nickname_entry = tk.Entry(form)
nickname_entry.place(x=195,y=70)

password_entry = tk.Entry(form,show='*')
password_entry.place(x=195,y=150)

#LABELS
nickname_label = tk.Label(form,text='Nickname',font='sans 14 bold')
nickname_label.place(x=230,y=40)

password_label = tk.Label(form,text='Password',font='sans 14 bold')
password_label.place(x=230,y=120)


check_label = tk.Label(form,text='',font='sans 12 bold',fg='green')
check_label.place(x=200,y=200)

form.mainloop()
