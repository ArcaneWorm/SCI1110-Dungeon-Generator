import math
import random
from PIL import Image, ImageDraw

#This is the background:
img = Image.new("RGB", (600, 600)) 

room_num = int(input("Enter number of rooms:"))


for x in range(room_num):
    #random size within certain limits:
    if x == 0:
        #Top Left Quadrant:
        x0 = random.randint(10, 130)
        x1 = random.randint(150, 290)
        y0 = random.randint(10, 130)
        y1 = random.randint(150, 290)

    if x == 1:
        #Bottom Left Quadrant
        x0 = random.randint(10, 130)
        x1 = random.randint(150, 290)
        y0 = random.randint(310, 430)
        y1 = random.randint(450, 590)

    if x == 2:
        #Top Right Quadrant
        x0 = random.randint(310, 430)
        x1 = random.randint(450, 590)
        y0 = random.randint(10, 130)
        y1 = random.randint(150, 290)

    if x == 3:
        #Bottom Right Quadrant
        x0 = random.randint(310, 430)
        x1 = random.randint(450, 590)
        y0 = random.randint(310, 430)
        y1 = random.randint(450, 590)


    #This is the size of the rectangle:
    shape = [(x0, y0), (x1, y1)] 

    #This draws the shape on the background and then the actual rectangle
    img1 = ImageDraw.Draw(img)   
    img1.rectangle(shape, fill ="white", outline ="blue")

#This is how we show the picture :)
img.show() 