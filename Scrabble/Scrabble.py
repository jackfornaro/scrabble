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

#creating board using grid (15x15 with border)
for x in range(17):
    for y in range(17):
        #Border
        if(x == 0 or y == 0 or x == 16 or y == 16):
            btn = Button(frame, image = photoBLANK)
        #Triple Word
        elif((x == 1 and y ==1) or (x == 8 and y == 1) or (x == 15 and y == 1) or
             (x == 1 and y ==15) or (x == 8 and y == 15) or (x == 15 and y == 15) or
             (x == 1 and y == 8) or (x == 15 and y == 8)):
            btn = Button(frame, image = photoTW)
        #Double Letter
        elif((x == 4 and y ==1) or (x == 12 and y == 1) or (x == 7 and y == 3) or
             (x == 9 and y ==3) or (x == 1 and y == 4) or (x == 8 and y == 4) or
             (x == 15 and y == 4) or (x == 3 and y == 7)or (x == 7 and y == 7) or
             (x == 9 and y == 7) or (x == 13 and y == 7) or(x == 4 and y == 8) or
             (x == 12 and y == 8) or (x == 3 and y == 9) or (x == 7 and y == 9) or
             (x == 9 and y == 9) or (x == 13 and y == 9) or (x == 1 and y == 12) or
             (x == 8 and y == 12) or (x == 15 and y == 12) or (x == 7 and y == 13) or
             (x == 9 and y == 13) or (x == 4 and y == 15) or (x == 12 and y == 15)):
            btn = Button(frame, image = photoDL)
        #Double Word
        #--TODO--
            

        #Triple Letter
        #--TODO--

        #Star
        #--TODO--

            
        #Remaining Tiles
        else:
            btn = Button(frame, image = photoBLANK)
        btn.grid(column=x, row=y, sticky=N+S+E+W)

for x in range(17):
  Grid.columnconfigure(frame, x, weight=2)

for y in range(17):
  Grid.rowconfigure(frame, y, weight=2)

root.mainloop()

