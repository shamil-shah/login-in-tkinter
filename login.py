
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Giris')
root.geometry('925x500+230+130')
root.configure(bg='#333333')
root.resizable(False, False)



def signin():
    username = user.get()
    password = code.get()
    usrname = 'admin'
    paswrd = 'admin'

    if username == usrname and password == paswrd:
        screen = Toplevel(root)
        screen.title('Tetbiq')
        screen.geometry('925x500')
        screen.config(bg='skyblue')

        Label(screen, text='XOS GELMISINIZ!', bg='skyblue', font=('Times', 50, 'bold')).pack(expand=True)

        screen.mainloop()

    elif username != usrname and password != paswrd:
        messagebox.showerror('Xeta', 'Istifadeci adi ve parolu yanlisdir!')

    elif password != paswrd:
        messagebox.showerror('Xeta', 'Parolu yanlisdir!')

    elif username != usrname:
        messagebox.showerror('Xeta', 'Istifadeci adi yanlisdir!')

#qeydiyyat hissesi
def log_up():
    
    def sign_up():
        username1 = username_entry.get()
        password1 = password_entry.get()
        confirm_password = confirm_password_entry.get()
        email = email_entry.get()
        
        if not all([username1, password1, confirm_password, email]):
            error_label.config(text="Zehmet olmasa butun xanalari doldurun")
            return
        if password1 != confirm_password:
            error_label.config(text="Parol ugun deyil")
            return

        
        success_label.config(text="Qeydiyyat ugurlu oldu!",)

    
    signup = Toplevel(root)
    signup.title("Qeydiyyat")
    signup.geometry('400x250+300+200')
    # signup.resizable(False, False)
    bgcolor = 'skyblue' 
    entrycolor = '#33FFFF'
    signup.config(bg=bgcolor)
    
   
    username_label = Label(signup, text="Istifadeci adi", bg=bgcolor)
    password_label = Label(signup, text="Parol", bg=bgcolor)
    confirm_password_label = Label(signup, text="Parolun tesdiqi", bg=bgcolor)
    email_label = Label(signup, text="elektron poct", bg=bgcolor)
    error_label = Label(signup, fg="red", bg=bgcolor)
    success_label = Label(signup, fg="#66FF33", bg=bgcolor)

    
    username_entry = Entry(signup, bg=entrycolor, border=0)
    password_entry = Entry(signup, show="*", bg=entrycolor, border=0)
    confirm_password_entry = Entry(signup, show="*", bg=entrycolor, border=0)
    email_entry = Entry(signup, bg=entrycolor, border=0)

    sign_up_button = Button(signup, text="Qeydiyyat", command=sign_up, bg='#66CCCC', border=0, activebackground='#33FFFF')

  
    username_label.grid(row=0, column=0)
    username_entry.grid(row=0, column=1)
    password_label.grid(row=1, column=0)
    password_entry.grid(row=1, column=1)
    confirm_password_label.grid(row=2, column=0)
    confirm_password_entry.grid(row=2, column=1)
    email_label.grid(row=3, column=0)
    email_entry.grid(row=3, column=1)
    error_label.grid(row=4, columnspan=2)
    success_label.grid(row=5, columnspan=2)
    sign_up_button.grid(row=6, columnspan=2)

    signup.mainloop()

img = PhotoImage(file='login1.png')
Label(root, image=img, bg='#333333', width=350, height=380).place(x=50, y=50)

frame = Frame(root, width=350, height=380, bg='#666666')
frame.place(x=480, y=70)

heading = Label(frame, text='Giris', fg='skyblue', bg='#666666', font=('Times', 23, 'bold'))
heading.place(x=140, y=5)

#istifadeci adi
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name == '':
        user.insert(0, 'Istifadeci adi')


user = Entry(frame, width=41, fg='white', border=0, bg='#666666', font=('Times', 11))
user.place(x=30, y=110)
user.insert(0, 'Istifadeci adi')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=292, height=2, bg='black').place(x=25, y=135)
#parol
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name == '':
        code.insert(0, 'Parol')

code = Entry(frame, width=41, fg='white', border=0, bg='#666666', font=('Times', 11))
code.place(x=30, y=147)
code.insert(0, 'Parol')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame, width=292, height=2, bg='black').place(x=25, y=165)
#giris ucun duyme

Button(frame, width=39, pady=7, text='Daxil ol', bg='#333333', activebackground='#666666',fg='skyblue', border=0, command=signin).place(x=35, y=204)

label = Label(frame, text='hesabiniz yoxdur?', fg='skyblue', bg='#666666', font=('Times', 9))
label.place(x=90, y=270)

sign_up = Button(frame, width=7, text='Qeydiyyat', border=0, bg='#666666', activebackground='#666666', cursor='hand2', fg='skyblue', command=log_up)
sign_up.place(x=200, y=270)


root.mainloop()
