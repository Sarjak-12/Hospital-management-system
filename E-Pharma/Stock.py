import sqlite3
from tkinter import *

# Create the main window
root = Tk()
root.config(bg='#C0C0C0')  # Light gray background
root.title("Medicine Database Admin Area")
root.geometry("850x700")
root.resizable(False, False)  # Disable resizing

# To add an icon, call root.iconbitmap("filename.ico") function
root.iconbitmap('img_folder\\download.ico')

# A function to navigate to UI1
def ui():
    root.destroy()
    import ui1

def update_database_schema():
    # Connect to the database
    conn = sqlite3.connect("medicine_database.db")
    cursor = conn.cursor()

    # Add a new column 'purpose' to the 'medicines' table
    cursor.execute("ALTER TABLE medicines ADD COLUMN purpose TEXT")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def view_records():
    conn = sqlite3.connect("medicine_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicines")
    records = cursor.fetchall()
    conn.close()

    draw_table(records)

def draw_table(records):
    # Clear previous drawings
    canvas.delete("all")

    # Draw horizontal lines
    for i in range(len(records) + 1):
        canvas.create_line(50, 50 + 30 * i, 550, 50 + 30 * i, fill="black")

    # Draw vertical lines
    for x in (50, 250, 400, 550):
        canvas.create_line(x, 50, x, 50 + 30 * len(records), fill="black")

    # Draw headers
    headers = ["Medicine Name", "Quantity", "Expiry Date", "Purpose"]
    for i, header in enumerate(headers):
        canvas.create_text(150 * (i+1), 25, text=header, font=("Arial", 10, "bold"))

    # Draw records
    for i, record in enumerate(records):
        for j, value in enumerate(record[1:]):  # Exclude the ID
            canvas.create_text(150 * (j+1), 50 + 30 * i + 15, text=value)

    # Update the canvas size based on the content
    canvas.config(scrollregion=canvas.bbox("all"))

# Entry fields for adding new records
entry_style = {"font": ("Arial", 12), "bg": '#D3D3D3', "fg": '#333333', "borderwidth": 0}  # Modified entry style
labels = ["Medicine Name", "Quantity", "Expiry Date", "Purpose"]
entries = {}

for i, label in enumerate(labels):
    entry_label = Label(root, text=f"{label}:", font=("Arial", 12), bg='#707070', fg='white')
    entry_label.place(x=180, y=120 + 40 * i)
    entries[label] = Entry(root, **entry_style)
    entries[label].place(x=320, y=120 + 40 * i)

# Create a frame to hold the canvas and scrollbars
frame = Frame(root, bd=2, relief=SUNKEN)
frame.place(x=50, y=50)

# Create a canvas within the frame
canvas = Canvas(frame, width=700, height=500, bg="white")
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Bind the mouse wheel to scroll the canvas
canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

# Create a vertical scrollbar on the right side
vsb = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
vsb.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=vsb.set)

# Create another frame to hold the contents of the canvas
table_frame = Frame(canvas, bg="white")
canvas.create_window((0, 0), window=table_frame, anchor=NW)

# Button for going back to the home screen
home_button = Button(root, text="Home", font=("Arial", 12), bg="#3CB371", fg="white", padx=20, command=ui)
home_button.place(x=750, y=10)

# Directly call view_records to show data immediately
view_records()

# Run the Tkinter event loop
root.mainloop()
