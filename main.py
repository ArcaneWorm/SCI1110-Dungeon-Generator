import math
import random
from PIL import Image, ImageDraw

#This is the background:
img = Image.new("RGB", (600, 600)) 

room_num = int(input("Enter number of rooms:"))

for x in range(room_num):
    #random size within certain limits:
    x0 = random.randint(10, 300)
    x1 = x0 + random.randint(100, 290)
    y0 = random.randint(10, 300)
    y1 = y0 + random.randint(100, 290)
        
    #This is the size of the rectangle:
    shape = [(x0, y0), (x1, y1)] 

    #This draws the shape on the background and then the actual rectangle
    img1 = ImageDraw.Draw(img)   
    img1.rectangle(shape, fill ="white", outline ="blue")

#This is how we show the picture :)
img.show() 