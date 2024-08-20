from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('LOGIN')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False, False)

# to add icon we need to call a.iconbitmap("filename.ico") function
root.iconbitmap('img_folder\\download.ico')

def login1():
    root.destroy()
    import loggin

def signin():
    Username = user.get()
    Password = password.get()

    if Username == '@dmin' and Password == '6969':
        root.destroy()
        import Admin_Home
    elif Username != '@dmin' and Password != '6969':
        messagebox.showerror("Error", "Username or password is incorrect")
    elif password != '6969':
        messagebox.showerror("Error", "Invalid Password!")
    elif Username != '@dmin':
        messagebox.showerror("Error", "Invalid Username!")

def back_to_home():
    root.destroy()
    import ui1


img = PhotoImage(file='img_folder\\pharmacy1.png')
Label(root, image=img, bg='white').place(x=50, y=20)

frame = Frame(root, width=350, height=350, bg='lavender')
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='chocolate', bg='lavender', font=('Microsoft YaHei UI Light', 24, 'bold'))
heading.place(x=130, y=5)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=26, fg='black', border=0, bg='lavender', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Admin Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter(e):
    password.delete(0, 'end')

def on_leave(e):
    name = password.get()
    if name == '':
        password.insert(0, 'Password')

password = Entry(frame, width=26, fg='black', border=0, bg='lavender', font=('Microsoft YaHei UI Light', 11))
password.place(x=30, y=150)
password.insert(0, 'Password')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=10, text='Sign in', bg='white', cursor='hand2', fg='chocolate', border=0, command=signin).place(x=35, y=204)

label = Label(frame, text='Not an admin?', fg='black', bg='lavender', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=8, text='User Login', border=0, bg='lavender', cursor='hand2', fg='#57a1f8', command=login1)
sign_up.place(x=215, y=270)

# Back to home button
back_button = Button(root, text="Back to Home", command=back_to_home, bg='#6C757D', fg='white', font=('Arial', 12), cursor='hand2', bd=0)
back_button.place(x=20, y=10)

root.mainloop()
