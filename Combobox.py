#Create a combobox- Import from library.
import tkinter as tk
from tkinter import ttk

#Create a function that happens on an event.
def on_select(event):

    #create an item object that obtain the value of the selected item.
    selected_item = event.widget.get()
    print("Selected item:", selected_item)

#Create a root windown.
root = tk.Tk()
root.title("Diego C")

#Create an array with a number of items.
items = ["Car 1", "Car 2", "Car 3", "Car 4", "Car 5"]
#Create the combo box object, put the object in the root window and populate values.
combo_box = ttk.Combobox(root, values=items)

#The bind fucntion will tie the selected item to the on_selected fucntion.
combo_box.bind("<<ComboboxSelected>>", on_select)

#Pack the object in the screen with Geometry manager.
combo_box.pack()

#Main loop fuction keeps the root window visible.
root.mainloop()