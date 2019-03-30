import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack()

coords = {"x1":0,"y1":0,"x2":0,"y2":0}
# keep a reference to all lines by keeping them in a list
lines = []

def click(e):
    # define start point for line
    coords["x1"] = e.x
    coords["y1"] = e.y

    # create a line on this point and store it in the list
    lines.append(canvas.create_line(coords["x1"],coords["y1"],coords["x1"],coords["y1"]))

def drag(e):
    # update the coordinates from the event
    x2 = coords["x2"] = e.x
    y2 = coords["y2"] = e.y
    print("x2 = " + str(x2) + " y2 =", str(y2))

    x1 = coords["x1"]
    y1 = coords["y1"]
    print("x1 = " + str(x1) + " y1 =", str(y1))

    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1

    if m <= 1:
        while x1 < x2:
            x1 += 1
            y1 = m * x1 + b

            coords["x2"] = x1
            coords["y2"] = round(y1)
            canvas.coords(lines[0], coords["x1"], coords["y1"], coords["x2"], coords["y2"])

    else:
        while y1 < y2:
            y1 += 1
            x1 = (y1 - b) / m
            coords["x2"] = round(x1)
            coords["y2"] = y1
            canvas.coords(lines[0], coords["x1"], coords["y1"], coords["x2"], coords["y2"])


canvas.bind("<ButtonPress-1>", click)
canvas.bind("<B1-Motion>", drag)

root.mainloop()