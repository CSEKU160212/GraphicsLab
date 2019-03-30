import tkinter as tk

root = tk.Tk()
root.title("Bresenham's Line Algorithm")

canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack()

coords = {"x1":0,"y1":0,"x2":0,"y2":0}

#lines = []


def click(e):
    canvas.delete("all")
    # define start point for line
    coords["x1"] = e.x
    coords["y1"] = e.y

    # create a line on this point and store it in the list
    #lines.append(canvas.create_line(coords["x1"],coords["y1"],coords["x1"],coords["y1"]))
    canvas.create_rectangle((coords["x1"], coords["y1"]) * 2)


def drag(e):
    canvas.delete("all")
    # update the coordinates from the event
    x2 = coords["x2"] = e.x
    y2 = coords["y2"] = e.y

    x = x1 = coords["x1"]
    y = y1 = coords["y1"]

    dx = x2 - x1
    dy = y2 - y1
    dT = 2 * (dy - dx)
    dS = 2 * dy
    d = dS - dx

    m = dy / dx

    if m < 1:
        if x < x2:
            while x < x2:
                x += 1
                if d < 0:
                    d += dS
                else:
                    y += 1
                    d += dT
                coords["x2"] = x
                coords["y2"] = y
                canvas.create_rectangle((coords["x2"], coords["y2"]) * 2)
                #canvas.coords(lines[0], coords["x1"], coords["y1"], coords["x2"], coords["y2"])
        else:
            while x > x2:
                x -= 1
                if d < 0:
                    d -= dS
                else:
                    y += 1
                    d += dT
                coords["x2"] = x
                coords["y2"] = y
                canvas.create_rectangle((coords["x2"], coords["y2"]) * 2)

    else:
        if y <y2:
            while y < y2:
                y += 1
                if d < 0:
                    d = d + 2 * dx
                else:
                    x += 1
                    d = d + (2 * (dx - dy))
                coords["x2"] = x
                coords["y2"] = y
                canvas.create_rectangle((coords["x2"], coords["y2"]) * 2)
                #canvas.coords(lines[0], coords["x1"], coords["y1"], coords["x2"], coords["y2"])
        else:
            while y > y2:
                y -= 1
                if d > 0:
                    d = d + 2 * dx
                else:
                    x = 1
                    d = d - (2 * (dx - dy))
                coords["x2"] = x
                coords["y2"] = y
                canvas.create_rectangle((coords["x2"], coords["y2"]) * 2)


canvas.bind("<ButtonPress-1>", click)
canvas.bind("<B1-Motion>", drag)

root.mainloop()