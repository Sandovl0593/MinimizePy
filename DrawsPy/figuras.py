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
    while x != posX or y != posY:
        circle(rad_wh, -angle)
        circle(rad_wh, angle/2)
        x = round(xcor())
        y = round(ycor())
        penup()
        left(30)
        pendown()

    color("orange")
    n = 0;  m = 0
    for _ in range(2):
        for xmin, ymin, meter in [(20, 15, 65), (25, 20, 70), (30, 25, 75), (35, 30, 80)]:
            newposX = posX - round((rad_wh/(xmin+n)))
            newposY = posY - round((rad_wh/(ymin+n)))
            Rad = rad_wh - int(rad_wh/(meter+m))
            penup()
            goto(newposX, newposY)
            pendown()
            x = 0; y = 0
            while x != newposX or y != newposY:
                circle(Rad, -angle)
                circle(Rad, angle/2)
                x = round(xcor())
                y = round(ycor())
                penup()
                left(30)
                pendown()
        n += 72;  m += 30
    root.mainloop()

intCircle()
# moon()