# Author: Kelvin Loh
# Tutorial: https://python-post.blogspot.com/2026/01/mapview.html
# GitHub: https://github.com/Kelvin-Data/MapView/blob/main/map_1.py

from tkinter import *
import ttkbootstrap as tb
import tkintermapview
from ttkbootstrap.dialogs import Messagebox

root = tb.Window(themename='darkly')
root.title('Find My Map')
root.geometry("1200x1200")


### Section 1 - Function to set map position based on user input ###
def set_map_position():
    try:
        lat = float(latitude_entry.get())
        lon = float(longitude_entry.get())
        map_widget.set_position(lat, lon)
    except ValueError:
        Messagebox.show_error(title="Invalid coordinates.", 
                message="Please enter numeric values!!!")
        # Clear the entries after OK is clicked
        clear_entries()
    
def clear_entries():
    latitude_entry.delete(0, END)
    longitude_entry.delete(0, END)


### Section 2 - App Layout ###
# Main header label for the application
header_label = tb.Label(root, text="Where Am I? 🗺️", font=("Helvetica", 24), 
                        bootstyle="success-inverse")
header_label.pack(pady=10)

# Create a frame to contain coordinate input controls
My_frame = tb.Frame(root, bootstyle="info")
My_frame.pack(pady=10, padx=30, fill="x", expand=False)

# Configure grid column weights for equal width distribution across 5 columns
for i in range(6):  # 6 columns (0-5)
    My_frame.columnconfigure(i, weight=1)

# Define a consistent font for input controls
my_font = ("Roboto", 12)

# Latitude label and input field
my_vertical_cordinate = tb.Label(My_frame, text="Latitude:", 
                                 font=my_font,
                                 bootstyle="info-inverse")
my_vertical_cordinate.grid(row=0, column=0, pady=5, padx=5, sticky=EW)

latitude_entry = tb.Entry(My_frame, bootstyle="info")
latitude_entry.grid(row=0, column=1, pady=5, padx=5, sticky=EW)

# Longitude label and input field
my_horizontal_cordinate = tb.Label(My_frame, text="Longitude:",
                                   font=my_font,
                                   bootstyle="info-inverse")
my_horizontal_cordinate.grid(row=0, column=2, pady=5, padx=5, sticky=EW)

longitude_entry = tb.Entry(My_frame)
longitude_entry.grid(row=0, column=3, pady=5, padx=5, sticky=EW)

# Button to set map position using entered coordinates
# Converts string inputs to floats and calls set_position method
set_position_button = tb.Button(My_frame, text="Set Position", 
                                bootstyle=("danger", "outline"),
                                command=set_map_position)
set_position_button.grid(row=0, column=4, pady=5, padx=5, sticky=EW)

# Button to clear the latitude and longitude entry fields
clear_button = tb.Button(My_frame, text="Clear Entries", 
                         bootstyle=("warning", "outline"),
                         command=clear_entries)
clear_button.grid(row=0, column=5, pady=5, padx=5, sticky=EW)


### Section 3 - Map Display Section ###
# LabelFrame container for the map widget
my_label = LabelFrame(root, text="My map")
my_label.pack(pady=20, padx=20, fill="both", expand=True)

# Create map widget with specified dimensions and no rounded corners
map_widget = tkintermapview.TkinterMapView(my_label, width=1100, 
                                           height=1100, corner_radius=0)
map_widget.pack()

# Set initial zoom level (15 is a moderately close view)
map_widget.set_zoom(15)


root.mainloop()

