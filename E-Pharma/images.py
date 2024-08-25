import os
import tkinter as tk

root = tk.Tk()

# Provide the absolute path to the download.ico file
icon_path = r"C:\path\to\your\file\download.ico"  # replace with your file's actual location
root.iconbitmap(icon_path)

root.mainloop()
