# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title = "Welcom To Tkinter"

# Set geometry(widthxheight)
root.geometry('800x400')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar

menu = Menu(root)
item = Menu(menu)
item.add_command(label="New")
menu.add_cascade(label="File" , menu=item)
root.config(menu=menu)
# adding a label to the root window
lbl = Label(root , text = "Are you Geek ?")
lbl.grid()

# adding Entry Field
txt = Entry(root , width=10)
txt.grid(column=1 , row=0)

# function to display user text when 
# button is clicked
def clicked():
    res = "You Wrote " + txt.get()
    lbl.configure(text = res)

# button widget with red color text inside
btn = Button(root , text ="Click Me" , 
             fg="red",
             command=clicked)

# Set Button Grid
btn.grid(column=2 , row=0)




# Execute Tkinter
root.mainloop()

