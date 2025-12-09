
from tkinter import *
#need to install on all machines
from tkmacosx import Button

# the main window
root = Tk()
root.title("Enter Title Here")

# size of window
root.geometry("300x150")
# buttons
yellow_button = Button(root, text="Yellow", background='yellow')
green_button = Button(root, text="Green", background='green')

# label
label = Label(root, text="This is a stoplight")


# Create text widget and specify size.
T = Text(root, height = 5, width = 10)


# Place widgets in window (with pack function!)(order matters)
red_button.pack()
yellow_button.pack()
green_button.pack()
label.pack()
T.pack()


# Start the GUI event loop
root.mainloop()


