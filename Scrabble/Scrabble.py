from tkinter import *
from tkinter.ttk import *

root = Tk()

#Photo variables 
photoDL = PhotoImage(file = "double letter.png")
photoTL = PhotoImage(file = "triple letter.png")
photoDW = PhotoImage(file = "double word.png")
photoTW = PhotoImage(file = "triple word.png")
photoSTAR = PhotoImage(file = "star.png")
photoBLANK = PhotoImage(file = "blank space.png")

#setting grid 
frame=Frame(root)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)
grid=Frame(frame)
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
Grid.rowconfigure(frame, 7, weight=1)
Grid.columnconfigure(frame, 0, weight=1)

#creating board using grid
for x in range(15):
    for y in range(15):
        btn = Button(frame, image = photoDW)
        btn.grid(column=x, row=y, sticky=N+S+E+W)

for x in range(15):
  Grid.columnconfigure(frame, x, weight=2)

for y in range(15):
  Grid.rowconfigure(frame, y, weight=2)

root.mainloop()

