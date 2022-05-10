from turtle import *
from math import *
# Tmanaño del monitor
# from screeninfo import get_monitors
# for m in get_monitors():
#     print(str(m))

root = Screen()
hideturtle()
root.bgcolor("black")
root.setup(1000, 580, -400)
color("white","white")

def moon():
    pensize(10)
    speed(2)
    rmay = 140;  rmen = 110
    angulomen = 180
    angulomay = round(acos(-(((2*rmen)**2 - rmay**2 - rmay**2)/(2*rmay*rmay)))*180/pi)-1
    penup()
    goto(0, -50)
    pendown()
    begin_fill()
    left(25)
    circle(rmen, -angulomen)
    left(40)
    circle(rmay, angulomay)
    end_fill()
    root.mainloop()

def intCircle():
    speed(30)
    rad_wh = 150;  angle = 30
    posX = -100;  posY = -150
    penup()
    goto(posX, posY)
    left(180)
    pendown()

    x = 0; y = 0
    interse = list()
    while x != posX or y != posY:
        circle(rad_wh, -angle)
        circle(rad_wh, angle/2)
        x = round(xcor())
        y = round(ycor())
        penup()
        left(30)
        pendown()
        interse.append((x, y))

    color("yellow")
    for rad in interse:
        lefff = 0
        for i in range(6):
            if i == 1:
                circle(rad_wh+20, -angle)
            penup()
            goto(rad)
            left(lefff-15)
            pendown()
        left(30)

    for xmin, ymin, meter in [(15, 10, 10), (35, 16, 20), (68, 30, 50), (74, 40, 60)]:
        newposX = posX - round((rad_wh/xmin))
        newposY = posY - round((rad_wh/ymin))
        color("orange")
        rad_wh += int(rad_wh/meter)
        penup()
        goto(newposX, newposY)
        pendown()
        x = 0; y = 0
        while x != newposX or y != newposY:
            circle(rad_wh, -angle)
            circle(rad_wh, angle/2)
            x = round(xcor())
            y = round(ycor())
            penup()
            left(30)
            pendown()

    root.mainloop()

intCircle()
# moon()