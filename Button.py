#import the function from library
import tkinter as tk

#Write a function for button
def buttom_click():
    print("Button Clicked")
#Create a root function 
root = tk.Tk()
root.title("Buttom Example")

#Create the object of the button
#3 differents arguments 
button = tk.Button(root, text="Click Me!", command=buttom_click)
#Adjust how the button it's shows in the screen 
button.pack()
#keeps it window visible
root.mainloop()



