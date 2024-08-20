from tkinter import *
from PIL import Image, ImageTk
# Create the main window
root = Tk()
root.config(bg='#C0C0C0')  # Light gray background
root.title("Medicine Types")
root.geometry("400x500")
root.resizable(False, False)  # Disable resizing

# to add icon we need to call a.iconbitmap("filename.ico") function
root.iconbitmap('img_folder\\download.ico')


class MouseWheel:
    def __init__(self, root, canvas):
        root.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas = canvas

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


def go_back():
    root.destroy()
    import ui1


# Sample data organized by type
medicine_data = {
    "Pain and Fever": ["Acetaminophen (Tylenol)", "Ibuprofen (Advil, Motrin)", "Naproxen (Aleve)"],
    "Cough and Cold": ["Dextromethorphan (Robitussin DM)", "Guaifenesin (Mucinex)",
                       "Phenylephrine or pseudoephedrine (Sudafed)", "Chlorpheniramine (Chlor-Trimeton)",
                       "Diphenhydramine (Benadryl)"],
    "Allergies": ["Cetirizine (Zyrtec)", "Loratadine (Claritin)", "Fexofenadine (Allegra)",
                  "Nasal corticosteroid sprays (e.g., Flonase, Nasacort)"],
    "Acid Reflux and Indigestion": ["Antacids (e.g., Tums, Maalox)", "H2 blockers (e.g., ranitidine, famotidine)",
                                    "Proton pump inhibitors (e.g., omeprazole, lansoprazole)"],
    "Diarrhea": ["Loperamide (Imodium)", "Bismuth subsalicylate (Pepto-Bismol)"],
    "Constipation": ["Fiber supplements (e.g., Metamucil)", "Stool softeners (e.g., Colace)",
                     "Laxatives (e.g., Dulcolax)"],
    "Topical Analgesics": ["Hydrocortisone cream (anti-itch)", "Topical NSAIDs (e.g., diclofenac gel)",
                          "Lidocaine patches (for localized pain relief)"],
    "First Aid": ["Hydrogen peroxide (for wound cleaning)", "Antiseptic ointment (e.g., Neosporin)",
                  "Adhesive bandages", "Sterile gauze and medical tape"],
    "Motion Sickness": ["Dimenhydrinate (Dramamine)", "Meclizine (Bonine)"],
    "Eye Care": ["Artificial tears", "Antihistamine eye drops (e.g., Visine-A, Zaditor)",
                 "Lubricating eye ointment"],
    "Sleep Aids": ["Diphenhydramine (Benadryl)", "Doxylamine (found in some sleep aids)",
                   "Melatonin supplements"],
    "Nasal Care": ["Saline nasal spray", "Decongestant nasal sprays (for short-term use)"],
    "Oral Health": ["Antiseptic mouthwash (e.g., Listerine)", "Pain-relieving oral gels (e.g., Orajel)"],
    "Antifungal Medications": ["Clotrimazole (for yeast infections)", "Terbinafine (for athlete's foot, ringworm)"]
}



# Scrollable frame
canvas = Canvas(root, bg='#C0C0C0', highlightthickness=0)
scroll_y = Scrollbar(root, orient="vertical", command=canvas.yview)
scroll_y.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.configure(yscrollcommand=scroll_y.set)

# Frame to contain the medicine types and names
frame = Frame(canvas, bg='#C0C0C0')
canvas.create_window((0, 0), window=frame,width=8000, anchor="nw")

# Heading label
heading_label = Label(frame, text="Medicine Types", font=("Arial", 20), bg='#6C757D', fg='white', padx=10, pady=10)
heading_label.grid(row=0, column=0, columnspan=2, sticky="ew")


# Populate the frame with medicine types and names
row_num = 1
for medicine_type, medicine_names in medicine_data.items():
    type_label = Label(frame, text=medicine_type, font=("Arial", 15), bg='#707070', fg='white', padx=10, pady=5)
    type_label.grid(row=row_num, column=0, columnspan=2, sticky="ew")
    row_num += 1

    for medicine_name in medicine_names:
        name_label = Label(frame, text=medicine_name, font=("Arial", 12), bg='#D3D3D3', fg='#333333', padx=10, pady=5)
        name_label.grid(row=row_num, column=1, sticky="ew")
        row_num += 1

# Update scroll region
canvas.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Back button
home_btn = Button(frame, text="Back", font=("Arial", 12), bg="#00008b", cursor='hand2',fg='#57a1f8',underline=True,bd=0, command=go_back)
home_btn.place(x=0,y=0  )

# Enable scroll wheel functionality
MouseWheel(root, canvas)

# Run the Tkinter event loop
root.mainloop()
