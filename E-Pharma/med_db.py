import sqlite3
from tkinter import *
from tkinter import messagebox

# Create the main window
root = Tk()
root.config(bg='#C0C0C0')  # Light gray background
root.title("Medicine Database Admin Area")
root.geometry("850x500")
root.resizable(False, False)  # Disable resizing


# to add icon we need to call a.iconbitmap("filename.ico") function
root.iconbitmap('img_folder\\download.ico')

def create_database():
    conn = sqlite3.connect("medicine_database.db")
    cursor = conn.cursor()

    # Create medicines table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS medicines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            expiry_date TEXT NOT NULL,
            purpose TEXT
        )
    ''')

    conn.commit()
    conn.close()

create_database()

def view_records():
    conn = sqlite3.connect("medicine_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicines")
    records = cursor.fetchall()
    conn.close()

    listbox.delete(0, END)
    for record in records:
        listbox.insert(END, record)

def insert_record():
    name = name_entry.get()
    quantity = quantity_entry.get()
    expiry_date = expiry_date_entry.get()
    purpose = purpose_entry.get()

    if name and quantity and expiry_date and purpose:
        conn = sqlite3.connect("medicine_database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO medicines (name, quantity, expiry_date, purpose) VALUES (?, ?, ?, ?)",
                       (name, quantity, expiry_date, purpose))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Medicine record added successfully.")
        view_records()
        name_entry.delete(0, END)
        quantity_entry.delete(0, END)
        expiry_date_entry.delete(0, END)
        purpose_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def delete_record():
    selected_item = listbox.curselection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a record to delete.")
        return

    conn = sqlite3.connect("medicine_database.db")
    cursor = conn.cursor()
    record_id = listbox.get(selected_item)[0]
    cursor.execute("DELETE FROM medicines WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Medicine record deleted successfully.")
    view_records()

def retrieve_record():
    selected_item = listbox.curselection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a record to retrieve.")
        return

    conn = sqlite3.connect("medicine_database.db")
    cursor = conn.cursor()
    record_id = listbox.get(selected_item)[0]
    cursor.execute("SELECT * FROM medicines WHERE id=?", (record_id,))
    record = cursor.fetchone()
    conn.close()

    # Fill entry fields with retrieved data
    name_entry.delete(0, END)
    name_entry.insert(END, record[1])
    quantity_entry.delete(0, END)
    quantity_entry.insert(END, record[2])
    expiry_date_entry.delete(0, END)
    expiry_date_entry.insert(END, record[3])
    purpose_entry.delete(0, END)
    purpose_entry.insert(END, record[4])

def update_record():
    selected_item = listbox.curselection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a record to update.")
        return

    conn = sqlite3.connect("medicine_database.db")
    cursor = conn.cursor()
    record_id = listbox.get(selected_item)[0]
    new_name = name_entry.get()
    new_quantity = quantity_entry.get()
    new_expiry_date = expiry_date_entry.get()
    new_purpose = purpose_entry.get()

    cursor.execute("UPDATE medicines SET name=?, quantity=?, expiry_date=?, purpose=? WHERE id=?",
                   (new_name, new_quantity, new_expiry_date, new_purpose, record_id))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Medicine record updated successfully.")
    view_records()

    # Clear entry boxes after update
    name_entry.delete(0, END)
    quantity_entry.delete(0, END)
    expiry_date_entry.delete(0, END)
    purpose_entry.delete(0, END)

def log_out():
    # You can implement the logout functionality here
    root.destroy()
    import ui1



# Adding a background image
img = PhotoImage(file='img_folder\\admin_a.png')
Label(root, image=img).place(x=0, y=0)

# Entry fields for adding new records
entry_style = {"font": ("Arial", 12), "bg": '#D3D3D3', "fg": '#333333', "borderwidth": 0}  # Modified entry style

name_label = Label(root, text="Medicine Name:", font=("Arial", 12), bg='#707070', fg='white')  # Darker gray background
name_label.place(relx=0.02, rely=0.1)
name_entry = Entry(root, **entry_style)
name_entry.place(relx=0.2, rely=0.1)

quantity_label = Label(root, text="Quantity:", font=("Arial", 12), bg='#707070', fg='white')  # Darker gray background
quantity_label.place(relx=0.02, rely=0.2)
quantity_entry = Entry(root, **entry_style)
quantity_entry.place(relx=0.2, rely=0.2)

expiry_date_label = Label(root, text="Expiry Date:", font=("Arial", 12), bg='#707070', fg='white')  # Darker gray background
expiry_date_label.place(relx=0.02, rely=0.3)
expiry_date_entry = Entry(root, **entry_style)
expiry_date_entry.place(relx=0.2, rely=0.3)

# Adding Purpose field
purpose_label = Label(root, text="Purpose:", font=("Arial", 12), bg='#707070', fg='white')
purpose_label.place(relx=0.02, rely=0.4)
purpose_entry = Entry(root, **entry_style)
purpose_entry.place(relx=0.2, rely=0.4)

# Buttons for actions
button_style = {"bg": '#6C757D', "fg": 'white', "font": ("Arial", 12)}  # Modified button style

insert_button = Button(root, text="Insert Record", command=insert_record, **button_style)  # Gray button
delete_button = Button(root, text="Delete Record", command=delete_record, **button_style)  # Gray button
retrieve_button = Button(root, text="Retrieve Record", command=retrieve_record, **button_style)  # Gray button
update_button = Button(root, text="Update Record", command=update_record, **button_style)  # Gray button

# Log out button
log_out_button = Button(root, text="Log Out", command=log_out, **button_style)
log_out_button.place(relx=0.9, rely=0.02)

# Organize labels, entry boxes, and buttons
insert_button.place(relx=0.02, rely=0.5)
delete_button.place(relx=0.2, rely=0.5)
retrieve_button.place(relx=0.02, rely=0.6)
update_button.place(relx=0.2, rely=0.6)

# Listbox to display records with Scrollbar
listbox_frame = Frame(root)
listbox_frame.place(relx=0.45, rely=0.1, relheight=0.8)

scrollbar = Scrollbar(listbox_frame, orient=VERTICAL)
listbox = Listbox(listbox_frame, width=40, height=20, bg="#595959", fg="white", selectbackground="#AED6F1", borderwidth=0, yscrollcommand=scrollbar.set, font=("Arial", 15))
listbox.pack(side=LEFT, fill=Y)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# View records initially
view_records()

# Run the Tkinter event loop
root.mainloop()
