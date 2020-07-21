from tkinter import*
from math import*
from random import*
from PIL import Image, ImageDraw


canvasEdge = 1000

master = Tk()
w = Canvas(master, width=canvasEdge, height=canvasEdge,bd=0,highlightthickness=0)
w.configure(bg="#172033")
w.pack()

listOfPoints = []

R = randint(10,70)
r = randint(100,400)
d = randint(100,400)
magicNumber = randint(1,3)
magicNumber2 = randint(1,2)
magicNumber3 = randint(1,2)
magicNumber4 = randint(1,2)

#R = 20
#r = 200
#d = 100

def rgb2hex(r,g,b):
    hex = "#{:02x}{:02x}{:02x}".format(r,g,b)
    return hex


image = Image.new("RGB", (canvasEdge, canvasEdge), "#172033")
draw = ImageDraw.Draw(image)
color = 0

for angle in range(0,3600*5):
    angle = angle/10
    y = (R/magicNumber3-r*magicNumber4)*sin(radians(angle)) - d*sin(((R-r)*angle)/r)*(magicNumber2*0.2) + canvasEdge/2
    x = (R*magicNumber3-r)*cos(radians(angle)) + d*cos(((R-r)*angle)/r*magicNumber)*(sin(radians(angle))) + canvasEdge/2
    color = "#76E4EE"
    listOfPoints.append([x,y,color])



for counter in range(1,len(listOfPoints)):
    point = listOfPoints[counter]
    x,y = point[0], point[1]
    prevPoint = listOfPoints[counter-1]
    prevX,prevY = prevPoint[0], prevPoint[1]
    w.create_line(prevX,prevY,x,y, fill=color,width=1)
    draw.line([prevX,prevY,x,y], point[2])

#image.save("desktop/image.jpg")

master.mainloop()
