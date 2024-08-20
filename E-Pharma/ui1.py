from tkinter import *
from tkinter import PhotoImage

# Create the main window
root = Tk()
root.geometry("1000x550")
root.resizable(False, False)

# to add icon we need to call a.iconbitmap("filename.ico") function
root.iconbitmap('img_folder\\download.ico')

# Function to open the about us page
def lg_out():
    root.destroy()
    import Starting_Page

    # Function to navigate to the about us page
def abt_us():
    root.destroy()
    import about_us

# Function to navigate to the admin login page
def adm_log():
    root.destroy()
    import admin_loggin

#Function to navigate to stock page
def stck():
    root.destroy()
    import Stock

#function to navigate to use case page
    
def use_case():
    root.destroy()
    import med_usecase_read



# Adding a background image
img = PhotoImage(file='img_folder\\ui_1.png')
Label(root, image=img, border=0, height=550, width=1000, bg="white").place(x=0, y=0)

# Frame to add the logo and the name of the app
Logo_Bar = Frame(root, width=228, height=69, bg="#282828")
Logo_Bar.place(x=10, y=6)

# Text in the frame
introText = Label(root, text="E-Pharma", fg="#979090", bg="#282828", font=('times', 35, 'bold', 'italic'))
introText.place(x=15, y=6)

# Admin area button
Admin_area = Button(root, text="Admin Login", fg="white", bg="#242424", width=11, font=('times', 18, "underline"),
                    activebackground="#303030", command=adm_log)
Admin_area.place(x=820, y=27)

# Log out button
Log_out = Button(root, text="Log Out", fg="white", bg="#242424", width=11, font=('times', 18, "underline"),
                  activebackground="#303030", command=lg_out)
Log_out.place(x=660, y=27)

# Description frame 1
Desc_Frm_1 = Frame(root, width=254, height=350, bg="#282828")
Desc_Frm_1.place(x=41, y=185)

# Button in the 1st description frame
med_order_btn1 = Button(Desc_Frm_1, text="Use-case of Medicines", fg="white", border=False, bg="#242424", width=17,
                        font=('times', 18, "underline"), activebackground="#404040",command=use_case)
med_order_btn1.place(x=15, y=10)

# Attributes of this feature in the description box using label
Desc_Frm_1_lbl_text = "Here we have listed all \n our medicines  in the stock\n and what they  are generally\n used for jsut so consumers\n  and prescribers will have a \n general idea of when to \n use the medine and what \n to use it for  "
Desc_Frm_1_lbl = Label(Desc_Frm_1, text=Desc_Frm_1_lbl_text, fg="#979090", bg="#282828",
                       font=('times', 16))  # here, bg is background, fg is foreground and anchor w makes it left aligned
Desc_Frm_1_lbl.place(x=3, y=65)

# Description frame 2
Desc_Frm_2 = Frame(root, width=254, height=350, bg="#282828", )
Desc_Frm_2.place(x=371, y=185)

# Button in the 2nd description frame
med_order_btn2 = Button(Desc_Frm_2, text="Our Stock", fg="white", border=False, bg="#242424", width=17,
                        font=('times', 18, "underline"), activebackground="#404040",command=stck)
med_order_btn2.place(x=19, y=10)

# Attributes of this feature in the description box using label
Desc_Frm_2_lbl_text = "   Here, we have listed all the \n medicines we have in stock\n right now, how much amount\n we have available throughout\n the stores\n Note:-Check our medicine\n list for the  "
Desc_Frm_2_lbl = Label(Desc_Frm_2, text=Desc_Frm_2_lbl_text, fg="#979090", bg="#282828", font=('times', 16), width=30,anchor=W)
Desc_Frm_2_lbl.place(x=0, y=60)

# Description frame 3
Desc_Frm_3 = Frame(root, width=254, height=350, bg="#282828")
Desc_Frm_3.place(x=721, y=185)

# Button in the 3rd description frame
med_order_btn3 = Button(Desc_Frm_3, text="About Us", fg="white", border=False, bg="#242424", width=15,
                        font=('times', 18, "underline"), activebackground="#404040",command=abt_us)
med_order_btn3.place(x=25, y=10)

# Attributes of this feature in the description box using label
Desc_Frm_3_lbl_text = "Here, you can see about our\n team and what this project is\n about. And also where to\n contact us"
Desc_Frm_3_lbl = Label(Desc_Frm_3, text=Desc_Frm_3_lbl_text, fg="#979090", bg="#282828", font=('times', 16),anchor=W)
Desc_Frm_3_lbl.place(x=9, y=60)

root.mainloop()
