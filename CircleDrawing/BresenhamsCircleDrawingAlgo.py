import tkinter as tk
import math

root = tk.Tk()
root.title("Direct Line Algorithm")
canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack()
coords = {"x1":0,"y1":0}


def click(e):
    # define start point for line
    canvas.delete("all")
    coords["x1"] = e.x
    coords["y1"] = e.y


def drag(e):
    canvas.delete("all")
    x2 = e.x
    y2 = e.y

    centerx = x1 = coords["x1"]
    centery = y1 = coords["y1"]

    print(x1,y1, x2,y2)

    r = int(math.sqrt((x2-x1)**2+(y2-y1)**2))
    print(r)

    canvas.create_rectangle((x1, y1)*2)

    x = 0
    y = r
    d = 3-2*r

    while x <= y:

        canvas.create_rectangle((x+centerx,y+centery)*2)
        canvas.create_rectangle((y+centerx,x+centery)*2)
        canvas.create_rectangle((-y+centerx,x+centery)*2)
        canvas.create_rectangle((-x+centerx,y+centery)*2)
        canvas.create_rectangle((-x+centerx,-y+centery)*2)
        canvas.create_rectangle((-y+centerx,-x+centery)*2)
        canvas.create_rectangle((y+centerx,-x+centery)*2)
        canvas.create_rectangle((x+centerx,-y+centery)*2)

        if d < 0:
            d = d+4*x+6
        else:
            d = d+4*(x-y)+10
            y = y-1
        x = x+1


canvas.bind("<ButtonPress-1>", click)
canvas.bind("<B1-Motion>", drag)
tk.mainloop()