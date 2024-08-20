from tkinter import *

# Create the main window
root = Tk()
root.title("About Me")
root.geometry("1000x700")  # Increased height
root.resizable(False, False)
root.config(bg='#E6E6FA')  # Lavender background color

# to add icon we need to call a.iconbitmap("filename.ico") function
root.iconbitmap('img_folder\\download.ico')


# Import Ui
def ui():
    root.destroy()
    import ui1

# Function to create  frame with content label
def create_frame(content, row, col, rowspan=1, columnspan=1):
    frame = Frame(root, bg='#E6E6FA', padx=20, pady=20, bd=1, relief=SOLID)  # Add border
    frame.grid(row=row, column=col, padx=10, pady=10, rowspan=rowspan, columnspan=columnspan)
    
    label = Label(frame, text=content, font=("Arial", 14), justify=LEFT, bg='#E6E6FA')
    label.pack()

# Big title at the top-middle
big_title = Label(root, text="About Us", font=("Arial", 40, "bold", "underline"), bg='#E6E6FA')
big_title.grid(row=0, column=0, pady=20, padx=50, columnspan=2)  # Move a bit to the left

# Content for each label
label1_content = """
Hello! We are Computing(Hons) students,
  in softwarica college. Making our first semester 
   project. Our project is about 
         
           "Pharmacy Management System" 
                  (E-Pharma)
"""

label2_content = """
Goal:
- To make a system that can manage the medicines in
 pharmacy digitally and more efficiently

Attributes:
- User friendly admin pannel
- Database connecting both admin and user veiws
"""

label3_content = """

Connect with Us:
- GitHub: github.com/yourusername
- LinkedIn: linkedin.com/in/yourname
"""

# Create  frame with content labels
create_frame(label1_content, 1, 0)
create_frame(label2_content, 1, 1)
create_frame(label3_content, 2, 0, rowspan=1, columnspan=2)


home_button = Button(root, text="Home",  font=("Arial", 12), bg="#3CB371", fg="white", padx=20,command=ui)
home_button.place(x=900, y=10)

root.mainloop()
