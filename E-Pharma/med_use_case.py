from tkinter import *
from tkinter import messagebox

# Create the main window
root = Tk()
root.config(bg='#C0C0C0')  # Light gray background
root.title("Medicine Database")
root.geometry("850x500")
root.resizable(False, False)  # Disable resizing

# to add icon we need to call a.iconbitmap("filename.ico") function
root.iconbitmap('img_folder\\download.ico')

def create_file():
    with open("medicine_data.txt", "w") as file:
        file.write("Category,Name,Purpose\n")

def view_records(category):
    try:
        with open("medicine_data.txt", "r") as file:
            records = [line.strip().split(",") for line in file.readlines()]
            records = [record for record in records if record[0] == category]
            listbox.delete(0, END)
            for record in records[1:]:
                listbox.insert(END, record)
    except FileNotFoundError:
        create_file()

def insert_record():
    category = category_var.get()
    name = name_entry.get()
    purpose = purpose_entry.get()

    if category and name and purpose:
        with open("medicine_data.txt", "a") as file:
            file.write(f"{category},{name},{purpose}\n")

        messagebox.showinfo("Success", "Medicine record added successfully.")
        view_records(category)
        name_entry.delete(0, END)
        purpose_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Please fill in all fields.")
#setting path back to ui1
def logout():
    root.destroy()
    import ui1
   


# Entry fields for adding new records
entry_style = {"font": ("Arial", 12), "bg": '#D3D3D3', "fg": '#333333', "borderwidth": 0}  # Modified entry style

category_label = Label(root, text="Category:", font=("Arial", 12), bg='#707070', fg='white')
category_label.place(relx=0.02, rely=0.1)
category_var = StringVar()
category_entry = Entry(root, textvariable=category_var, **entry_style)
category_entry.place(relx=0.2, rely=0.1)

name_label = Label(root, text="Medicine Name:", font=("Arial", 12), bg='#707070', fg='white')
name_label.place(relx=0.02, rely=0.2)
name_entry = Entry(root, **entry_style)
name_entry.place(relx=0.2, rely=0.2)

purpose_label = Label(root, text="Purpose:", font=("Arial", 12), bg='#707070', fg='white')
purpose_label.place(relx=0.02, rely=0.3)
purpose_entry = Entry(root, **entry_style)
purpose_entry.place(relx=0.2, rely=0.3)

# Buttons for actions
button_style = {"bg": '#6C757D', "fg": 'white', "font": ("Arial", 12)}

insert_button = Button(root, text="Insert Record", command=insert_record, **button_style)
insert_button.place(relx=0.02, rely=0.4)

logout_button = Button(root, text="Logout", command=logout, **button_style)
logout_button.place(relx=0.92, rely=0.02)

# Listbox to display records with Scrollbar
listbox_frame = Frame(root)
listbox_frame.place(relx=0.45, rely=0.1, relheight=0.8)

scrollbar = Scrollbar(listbox_frame, orient=VERTICAL)
listbox = Listbox(listbox_frame, width=40, height=20, bg="#595959", fg="white", selectbackground="#AED6F1", borderwidth=0, yscrollcommand=scrollbar.set, font=("Arial", 15))
listbox.pack(side=LEFT, fill=Y)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Category selection menu
category_menu = OptionMenu(root, category_var, "Pain and Fever", "Cough and Cold", "Allergies",
                           "Acid Reflux and Indigestion", "Diarrhea", "Constipation", "Topical Analgesics",
                           "First Aid", "Motion Sickness", "Eye Care", "Sleep Aids", "Nasal Care", "Oral Health",
                           "Antifungal Medications")
category_menu.place(relx=0.02, rely=0.5)

# View records initially for the default category
default_category = "Pain and Fever"
category_var.set(default_category)
view_records(default_category)

# Run the Tkinter event loop
root.mainloop()
