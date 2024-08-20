from tkinter import *

root = Tk()
root.title("E-Pharma Welcome")
root.geometry("450x350")
root.resizable(False, False)
root.config(bg="#2A2F4F")

# to add icon we need to call a.iconbitmap("filename.ico") function
root.iconbitmap('img_folder\\download.ico')

def register_action():
    root.destroy()
    import Register_Epharma

def signin_action():
    root.destroy()
    import loggin


# Label for the welcome message
label_welcome = Label(root, text="Welcome to E-Pharma", font=("Arial", 20), fg="white", bg="#2A2F4F")
label_welcome.place(relx=0.5, rely=0.1, anchor="center")

# Title label
label_title = Label(root, text="The modern approach to pharmacy management", font=("Arial", 14, "italic"), fg="white", bg="#2A2F4F")
label_title.place(relx=0.5, rely=0.2, anchor="center")

# Frame for the buttons
button_frame = Frame(root, bg="#2A2F4F")
button_frame.place(relx=0.5, rely=0.4, anchor="center")

# Rounded Register button
register_button = Button(button_frame, text="Register", command=register_action, bg="#3CB371", fg="white", font=("Arial", 12), padx=20)
register_button.grid(row=0, column=0, padx=10)

# Rounded Sign in button
signin_button = Button(button_frame, text="Sign In", command=signin_action, bg="#3CB371", fg="white", font=("Arial", 12), padx=20)
signin_button.grid(row=0, column=1, padx=10)

root.mainloop()
