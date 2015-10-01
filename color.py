from Tkinter import *
tk = Tk()
canvas = Canvas(tk, width = 400, height = 400)
canvas.pack()

import random
def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2, fill = fill_color )

color = ['green', 'red', 'blue', 'orange', 'yellow', 'pink', 'purple', 'violet', 'magenta', 'cyan']    
for x in range(0, 100):
	  random_rectangle(400, 400, color[x%10])
	  
a = raw_input("come on:")
print(a)