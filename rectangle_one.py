from Tkinter import *
tk= Tk()
canvas = Canvas(tk, width = 500, height = 500)
canvas.pack()
canvas.create_line(0, 0, 500, 500)

import random
def random_rectangle(width, height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2)
    
for x in range(0, 50):
	  random_rectangle(400, 400)
	  
root.mainloop()

