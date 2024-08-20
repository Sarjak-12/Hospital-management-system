from tkinter import *

# Create the main window
root = Tk()
root.config(bg='#C0C0C0')  # Light gray background
root.title("ADMIN HOME")
root.geometry("400x200")
root.resizable(False, False)  # Disable resizing


# to add icon we need to call a.iconbitmap("filename.ico") function
root.iconbitmap('img_folder\\download.ico')

def medicine_usecase():
    # You can replace this function with the one that opens the Add Medicine page
   root.destroy()
   import med_use_case

def med_db():
    # You can replace this function with the one that opens the View Records page
    root.destroy()
    import med_db


# Heading label
heading_label = Label(root, text="ADMIN HOME", font=("Arial", 20), bg='#6C757D', fg='white', padx=10, pady=10)
heading_label.pack(fill=X)

# Buttons
button_style = {"bg": '#6C757D', "fg": 'white', "font": ("Arial", 12)}

use_case_button = Button(root, text="Usecase of meds", command=medicine_usecase, **button_style)
use_case_button.pack(pady=10)

Med_db_button = Button(root, text="Meds database", command=med_db, **button_style)
Med_db_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()