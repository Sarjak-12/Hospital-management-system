from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title('LOGIN')
root.geometry('925x500+300+200')  # size of background
root.configure(bg='white')  # background
root.resizable(False, False)  # resize horizontal ways or vertical ways

# to add icon we need to call a.iconbitmap("filename.ico") function
root.iconbitmap('img_folder\\download.ico')


conn = sqlite3.connect('user_database.db')  # Connect to the database
cursor = conn.cursor()

img = PhotoImage(file='img_folder\\pharmacy1.png')  # add image at side
Label(root, image=img, bg='white').place(x=50, y=20)

frame = Frame(root, width=350, height=350, bg='lavender')  # background frame for login work
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='chocolate', bg='lavender', font=('Microsoft YaHei UI Light', 24, 'bold'))
heading.place(x=130, y=5)

def on_enter(e):
    user.delete(0, 'end')  # making function for animation in entry box of username

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=26, fg='black', border=0, bg='lavender', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)  # adds line under entry

def on_enter(e):
    password.delete(0, 'end')  # making function for animation in entry box of password

def on_leave(e):
    name = password.get()
    if name == '':
        password.insert(0, 'Password')

password = Entry(frame, width=26, fg='black', border=0, bg='lavender', font=('Microsoft YaHei UI Light', 11))
password.place(x=30, y=150)
password.insert(0, 'Password')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)  # adds line under entry

def login():
    username = user.get()
    entered_password = password.get()

    # Query the database to check if the user exists
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, entered_password))
    user_data = cursor.fetchone()

    if user_data:
        root.destroy()
        import ui1
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

    # Clear the entry boxes after login attempt
    user.delete(0, 'end')
    password.delete(0, 'end')

Button(frame, width=39, pady=10, text='Sign in', bg='white', cursor='hand2', fg='chocolate', border=0,
       command=login).place(x=35, y=204)  # adding signin button

label = Label(frame, text='Create Account ?', fg='black', bg='lavender', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='lavender', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)

def reg():
    root.destroy()
    import Register_Epharma

sign_up.config(command=reg)

root.mainloop()