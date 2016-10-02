from graph import *
import math
import time
import numpy as np

def main():
    win = SetGraphicwindow()
    drawtimetable(win)
    CloseGraphiccwindow(win)


def SetGraphicwindow():
    win = GraphWin('Face', 1080, 1080, autoflush=False)
    win.setBackground("white")
    setmargins(win)
    drawborder(win)
    return win


def setmargins(win):
    margin = 7
    win.setCoords(-margin, -margin, margin, margin)


def drawborder(win):
    crl = Circle(Point(0, 0), 6)
    crl.setWidth(2)
    crl.draw(win)


def drawtimetable(win):
    numberofsides = 16
    points = SetPoints(numberofsides)
    initialvalue = 2
    finalvalue = 300
    for i in np.arange(initialvalue, finalvalue + 1.5, 1):
        string = "Valor: " + str(i)
        text = Text(Point(5, 5), string)
        text.draw(win)
        lines = setlines(points, i)
        drawlines(win, lines)
        win.update()
        text.undraw()
        clean(lines)


def clean(lines):
    time.sleep(5)
    for i in lines:
        i.undraw()


def GetCoordinates(a):
    increment = 360 / a
    coordinates = []
    number = 0
    multiplier = 6
    while 360 - number >= 0:
        data = math.radians(number)
        rawcoordinates = [math.sin(data), math.cos(data)]
        coordinates.append((i*multiplier for i in rawcoordinates))
        number += increment
    return coordinates


def SetPoints(numberofsides):
    coordinates = GetCoordinates(numberofsides)
    return [Point(a, b) for (a, b) in coordinates]


def setlines(points,timestable):
    mod = len(points)
    lines = []
    for j, i in enumerate(points):
        index = int((j * timestable) % mod)
        lines.append(Line(i, points[index]))
    for i in lines:
        i.setWidth(1)
    return lines


def drawlines(win, lines):
    for i in lines:
        i.draw(win)


def CloseGraphiccwindow(win):
    win.getMouse()
    win.close()

    
main()

