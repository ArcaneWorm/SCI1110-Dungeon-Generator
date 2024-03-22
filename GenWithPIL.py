import math
import random
from PIL import Image, ImageDraw

#This is the background:
img = Image.new("RGB", (3300, 2550), "WHITE") 

room_num = int(input("Enter number of rooms:"))


for x in range(room_num):
    #random size within certain limits:
    if x == 0:
        #Top Left Quadrant:
        x0 = random.randint(40, 200)
        x1 = random.randint(400, 600)
        y0 = random.randint(40, 250)
        y1 = random.randint(450, 800)

    if x == 1:
        #Bottom Left Quadrant
        x0 = random.randint(40, 200)
        x1 = random.randint(400, 600)
        y0 = random.randint(1000, 1240)
        y1 = random.randint(1440, 1790)

    if x == 2:
        #Top Right Quadrant
        x0 = random.randint(1000, 1200)
        x1 = random.randint(1400, 1800)
        y0 = random.randint(40, 250)
        y1 = random.randint(450, 800)

    if x == 3:
        #Bottom Right Quadrant
        x0 = random.randint(1000, 1200)
        x1 = random.randint(1400, 1800)
        y0 = random.randint(1000, 1240)
        y1 = random.randint(1440, 1790)
    
    if x == 4:
        x0 = random.randint(2000, 2200)
        x1 = random.randint(2400, 2800)
        y0 = random.randint(1990, 2230)
        y1 = random.randint(2430, 2780)


    #This is the size of the rectangle:
    shape = [(x0, y0), (x1, y1)] 

    #This draws the shape on the background and then the actual rectangle
    img1 = ImageDraw.Draw(img)   
    img1.rectangle(shape, fill ="white", outline ="blue", width = 5)

#This is how we show the picture :)
img.show() 