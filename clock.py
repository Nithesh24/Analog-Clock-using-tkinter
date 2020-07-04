import tkinter as tk
import time
from math import sin,cos,radians

clock  = tk.Tk()
clock.title("clock")
icon = tk.PhotoImage(file = "alarm-clock.png")
clock.iconphoto(False, icon)

canvas = tk.Canvas(clock,width = 450 , height = 450)
canvas.pack()

bg = tk.PhotoImage(file = "woodbg.png")
background = canvas.create_image(225, 225, image = bg)


image = tk.PhotoImage(file = "clock_image.png")
clock_image = canvas.create_image(225, 225, image = image)

center = 225

def list_maker(l):
    x = []
    y = []

    for i in range (0,90,6):
        x.append(225 + (l*sin(radians(i))))
        y.append(225 - (l*cos(radians(i))))
    for i in range (0,90,6):
        x.append(225 + (l * cos(radians(i))))
        y.append(225 + (l * sin(radians(i))))
    for i in range (0,90,6):
        x.append(225 - (l * sin(radians(i))))
        y.append(225 + (l * cos(radians(i))))
    for i in range (0,90,6):
        x.append(225 - (l*cos(radians(i))))
        y.append(225 - (l*sin(radians(i))))

    return x, y

def hour_maker(l):
    x = []
    y = []

    for i in range (0,90,30):
        x.append(225 + (l*sin(radians(i))))
        y.append(225 - (l*cos(radians(i))))
    for i in range (0,90,30):
        x.append(225 + (l * cos(radians(i))))
        y.append(225 + (l * sin(radians(i))))
    for i in range (0,90,30):
        x.append(225 - (l * sin(radians(i))))
        y.append(225 + (l * cos(radians(i))))
    for i in range (0,90,30):
        x.append(225 - (l*cos(radians(i))))
        y.append(225 - (l*sin(radians(i))))

    return x, y

hour_x, hour_y  = hour_maker(75)
min_x, min_y = list_maker(165)
sec_x, sec_y = list_maker(125)

try:
    while True:
        t = time.localtime()

        if t.tm_hour >= 12:
            i = t.tm_hour - 12
        else:
            i = t.tm_hour

        j = t.tm_min
        k = t.tm_sec

        hour = canvas.create_line(center, center, hour_x[i], hour_y[i], width = 8, arrow = tk.LAST)
        min = canvas.create_line(center, center, min_x[j], min_y[j], width = 4, arrow = tk.LAST)
        sec = canvas.create_line(center, center, sec_x[k], sec_y[k], width = 1, arrow = tk.LAST)
        canvas.update()
        time.sleep(0.2)
        canvas.delete(hour)
        canvas.delete(min)
        canvas.delete(sec)

    clock.mainloop()

except:
    None

