from tkinter import *
from tkinter import messagebox
# import ast
import sqlite3

register=Tk()

#######################################
#Adding title on the top
register.title("Register")

#######################################################
# Setting a fixed size for the gui when first opened
register.geometry("920x500+300+200")

#######################################################
#Adding background color for the gui page
register.config(bg="#fff")

#########################################################
# Makes it so that the size of the gui cannot be changed  
register.resizable(False,False)


# to add icon we need to call a.iconbitmap("filename.ico") function
register.iconbitmap('img_folder\\download.ico')




# Create a database connection and cursor
conn = sqlite3.connect('user_database.db')  # Create or connect to the database
cursor = conn.cursor()

# Create a table for storing user information
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password VARCHAR(255)
    )
''')
conn.commit()
conn.close()


# Writting code to add the given user  data in the database
def add_user():
 if username_UI.get()=='' or password_UI.get()=='' or confirm_password_UI.get()=='':
      messagebox.showerror("Error", "Please fill in both username and password.")

 elif password_UI.get()!=confirm_password_UI.get():
      messagebox.showerror("Error", "Passwords doesn't match .")

 elif len(password_UI.get())<8:
     messagebox.showerror("Error","Password length should be at least eight ")

 else:
     conn=sqlite3.connect("user_database.db")
     c=conn.cursor()
     c.execute("INSERT INTO users(username,password) VALUES(?,?)",(username_UI.get(),password_UI.get()))
     conn.commit()
     conn.close()
     username_UI.delete(0,END)
     password_UI.delete(0,END)
     confirm_password_UI.delete(0,END)
    #  messagebox.INFO("Sucess", 'regestered sucessfully')


    











##################################
# Adding a image on the gui
img=PhotoImage(file='img_folder\\pharmacy1.png')
Label(register,image=img,border=0,bg="white").place(x=50,y=90)



#############################################################
# making a function so that we can open another gui

def log():
    register.destroy()
    import loggin



# Makes a different workspace that we can write and place stuff on 
frame=Frame(register,width=350,height=390,bg="lavender")
frame.place(x=480,y=50)




# Writting a title in the frame that we just created
Title=Label(frame,text="Register",fg="#57a1f8",bg="white",background="lavender",font=('Microsoft Yahei UI Light',23,'bold'))
Title.place(x=100,y=5)



###############################################################
# Making funcions for animations in the entrybox of Username

def on_enter(e):
    username_UI.delete(0,END)

def on_leave(e):
    if username_UI.get()=='':
        username_UI.insert(0,'Username')


#Creating entryboxes for user input of Username

username_UI=Entry(frame,width=25,fg='black',border=2,bg='white', bd=0,background="lavender",font=('Microsoft Yahei UI Light',11))
username_UI.place(x=30,y=80) 
username_UI.insert(0,"Username")#adds a default entry on entrybox when running the code
username_UI.bind("<FocusIn>",on_enter)
username_UI.bind("<FocusOut>",on_leave)

# Making a line under the username Entrybox of Username
Frame(frame,width=290,height=2,bg='black').place(x=25,y=107)







#####################################################################
# Making funcions for animations in the entrybox of password

def on_enter(e):
    password_UI.delete(0,END)

def on_leave(e):
    if password_UI.get()=='':
        password_UI.insert(0,'Password')





#Creating entryboxes for user input of password

password_UI=Entry(frame,width=25,fg='black',border=2,bg='white', bd=0,background="lavender",font=('Microsoft Yahei UI Light',11))
password_UI.place(x=30,y=150) 
password_UI.insert(0,"Password")#adds a default entry on entrybox when running the code
password_UI.bind("<FocusIn>",on_enter)
password_UI.bind("<FocusOut>",on_leave)




# Making a line under the username Entrybox of password
Frame(frame,width=290,height=2,bg='black').place(x=25,y=177)










#############################################################################
# Making funcions for animations in the entrybox of confirm password

def on_enter(e):
    confirm_password_UI.delete(0,END)

def on_leave(e):
    if confirm_password_UI.get()=='':
        confirm_password_UI.insert(0,'Confirm Password')




#################################################################################
#Creating entryboxes for user input of confirm password

confirm_password_UI=Entry(frame,width=25,fg='black',border=2,bg='white',background="lavender", bd=0,font=('Microsoft Yahei UI Light',11))
confirm_password_UI.place(x=30,y=220) 
confirm_password_UI.insert(0,"Confirm Password")#adds a default entry on entrybox when running the code
confirm_password_UI.bind("<FocusIn>",on_enter)
confirm_password_UI.bind("<FocusOut>",on_leave)



# Making a line under the username Entrybox of confirm password
Frame(frame,width=290,height=2,bg='black').place(x=25,y=247)








##################################################
# Creating a button for logging in 

Button(frame,width=39,pady=7,text="Register",bg="#57a1f8",fg="white",bd=0,command=add_user).place(x=35,y=280)




#################################################
# adding a lebel for already existing accounts

label=Label(frame,text='Wanna log a into existing account?',fg='black',background="lavender",font=('Microsoft Yahei UI Light',9))
label.place(x=75,y=340)



###################################################################################################################################################################
# adding a login button without a background or anything for it to have only underline and if clicked on will open a login page and destroy the register page

login=Button(frame,width=6,text="Log In",bd=0,bg="lavender",cursor='hand2',fg='#57a1f8',underline=True,command=log)
login.place(x=280,y=340)


























register.mainloop()