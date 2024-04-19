import random
import pygame

TILESIZE = 20               #each grid/tile will be 20 pixels
GRID_W, GRID_H = (58,38)    #resolution of 1160 by 760

class DungeonGen:

    def create_grid(): #creates the grids on the screen
        grid_surface = pygame.Surface((TILESIZE*GRID_W, TILESIZE*GRID_H))
        grid_surface.set_colorkey((2,2,2))
        grid_surface.fill((2,2,2))
        grid = []
        for y in range(GRID_H):
            line = []
            for x in range(GRID_W):
                r = pygame.Rect(x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE)
                line.append(r)
                pygame.draw.rect(grid_surface, pygame.Color("gray82"), r, 1) #the grids are just squares drawn next to each other
            grid.append(line)
        return grid, grid_surface
    

    def gen_room(quadrant, Surface, list=[]): #generates a room in a random quadrant of the screen
        
        #there's going to be 12 quadrants in the screen, 4 (horizontally) by 3 (vertically)
        #quadrant = random.randint(1,12) #picks a random quadrant to generate a room in

        #the height of the screen is 38 grids, so subtracting one space from top and bottom: 36 grids.
        #36 grids / 3 quadrants = 12 grids for each quadrant
        #the width of the screen is 58 grids, minus 2: 56 grids,
        #58 grids / 4 quadrants = 14 grids for each quadrant

        width = 20*(random.randint(4, 8)) #how far "right" the rectangle goes (x1)
        height = 20*(random.randint(3, 7)) #how far "down" the rectangle goes (y1)
        #This width and height is the same for all quadrants

    
        if (quadrant == 1): #LEFTMOST TOP
            left = 20*(random.randint(1, 7)) #left side of width (x0), adds 6 bc (14/2)-1 (minus 1 for space inbetween quadrants)
            top = 20*(random.randint(1, 6)) #top of height (y0), adds 5 bc (12/2)-1 
            color = "blue"

        elif (quadrant == 2): #LEFTMOST MIDDLE
            left = 20*(random.randint(1, 6)) #stays in leftmost part of screen
            top = 20*(random.randint(13, 18)) #max height of quad 1 was 13 (6+7), so it starts there and adds 5
            color = "red" #each one is a diff color for testing sake

        elif (quadrant == 3): #LEFTMOST BOTTOM
            left = 20*(random.randint(1, 6)) #stays in leftmost part of screen
            top = 20*(random.randint(25, 30)) #max height of quad 2 was 25 (18+7), adds 5
            color = "green"

        elif (quadrant == 4): #MIDDLE LEFT TOP
            left = 20*(random.randint(15, 21)) #max width of quad 1 was 15 (7+8), so it starts there and adds 6
            top = 20*(random.randint(1, 6)) 
            color = "orange"

        elif (quadrant == 5): #MIDDLE LEFT MIDDLE
            left = 20*(random.randint(15, 21)) #stays in middle left
            top = 20*(random.randint(13, 18)) #moves down
            color = "magenta"


        elif (quadrant == 6): #MIDDLE LEFT BOTTOM
            left = 20*(random.randint(15, 21)) #stays in middle left
            top = 20*(random.randint(25, 30)) #moves down
            color = "teal"

        elif (quadrant == 7): #MIDDLE RIGHT TOP
            left = 20*(random.randint(29, 35)) #max width of quad 4 was 29 (21+8), so it starts there and adds 6
            top = 20*(random.randint(1, 6)) 
            color = "purple" 

        elif (quadrant == 8): #MIDDLE RIGHT MIDDLE
            left = 20*(random.randint(29, 35)) #stays in middle right
            top = 20*(random.randint(13, 18)) #moves down
            color = "tomato"

        elif (quadrant == 9): #MIDDLE RIGHT BOTTOM
            left = 20*(random.randint(29, 35)) #stays in middle right
            top = 20*(random.randint(25, 30)) #moves down
            color = "crimson" 

        elif (quadrant == 10): #RIGHTMOST TOP
            left = 20*(random.randint(43, 49)) #max width of quad 7 was 43 (35+8), so it starts there and adds 6
            top = 20*(random.randint(1, 6)) 
            color = "darkred" 

        elif (quadrant == 11): #RIGHTMOST MIDDLE
            left = 20*(random.randint(43, 49)) #stays in rightmost
            top = 20*(random.randint(13, 18)) #moves down
            color = "olive"
        
        elif (quadrant == 12): #RIGHTMOST BOTTOM
            left = 20*(random.randint(43, 49)) #stays in rightmost
            top = 20*(random.randint(25, 30)) #moves down
            color = "hotpink"

        dimensions = left, top, width, height
        rect = pygame.Rect(dimensions)
        room = pygame.draw.rect(Surface, "black", rect, 2) #draws the actual rectangle

        list.append(rect) #adds to list of rectangles/rooms generated
        return list 

             
    
    def connect_vertical(x, Surface, list=[]):
        width = 20
        disconnected = True
        counter = 0
        verticals = []
        if (x != 2 and x != 5 and x!= 8 and x != 11):
            rect1 = pygame.Rect.copy(list[x+1])
            rect0 = pygame.Rect.copy(list[x])
            left = (rect0.left+rect0.width)
            top = (rect0.top+rect0.height)
            height = abs(rect1.top-(rect0.top+rect0.height))
            while(disconnected and counter < 20):
                num = 20*(random.randint(0, 8))
                rect = pygame.Rect(left-num, top-20, width, height+40)
                #would then check if this extended rectangle intersects the one below it
                if (rect.colliderect(rect1) and rect.colliderect(rect0)):
                    hall_rect = pygame.Rect(left-num, top, width, height+2)
                    hall = pygame.draw.rect(Surface, "black", hall_rect, 2)
                    #hallway borders/doors
                    hall_border_t = pygame.draw.line(Surface, pygame.Color("darkgray"), (left-num, top-1), (left-num+width, top-1), 5)
                    hall_border_b = pygame.draw.line(Surface, pygame.Color("darkgray"), (left-num, top+height+1), (left-num+width, top+height+1), 5)
                    disconnected = False
                    verticals.append(hall)
                else:
                    counter += 1
        return verticals
                
                 
            
    def connect_horizontal(x, Surface, list=[]):
        height = 20
        disconnected = True
        counter = 0
        horizontals = []
        if (x!=9 and x!=10 and x!=11):
            rect1 = pygame.Rect.copy(list[x+3])
            rect0 = pygame.Rect.copy(list[x])
            left = (rect0.left+rect0.width)
            top = (rect0.top+rect0.height)
            width = abs(rect1.left-(rect0.left+rect0.width))
            while(disconnected and counter < 20):
                num = 20*(random.randint(0, 8))
                rect = pygame.Rect(left-20, top-num, width+40, height)
                if (rect.colliderect(rect1) and rect.colliderect(rect0)):
                    hall_rect = pygame.Rect(left, top-num, width+2, height)
                    hall = pygame.draw.rect(Surface, "black", hall_rect, 2)
                    #hallway borders/doors
                    hall_border_l = pygame.draw.line(Surface, pygame.Color("darkgray"), (left-1, top-num), (left-1, top-num+height), 5)
                    hall_border_r = pygame.draw.line(Surface, pygame.Color("darkgray"), (left+width, top-num), (left+width, top-num+height), 5)
                    disconnected = False
                    horizontals.append(rect)
                else:
                    counter += 1
        return horizontals
                    
    





        






def main(): 
    pygame.init()
    Surface = pygame.display.set_mode((TILESIZE * GRID_W, TILESIZE * GRID_H)) #sets the actual screen
    pygame.display.set_caption("Dungeon Generated")
    clock = pygame.time.Clock()
    grid, grid_surface = DungeonGen.create_grid()
    running = True
    rectangles = []

    Surface.fill("white")
    Surface.blit(grid_surface, (0,0))

    for x in range(12): #generate however many number of rooms (for testing, just manually change it for now)
        rectangles = DungeonGen.gen_room(x+1, Surface, rectangles)
        
    for x in range(11):
        verticals = DungeonGen.connect_vertical(x, Surface, rectangles)
        horizontals = DungeonGen.connect_horizontal(x, Surface, rectangles)
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            clock.tick(60)

    print(rectangles) #just for our own reference
    

if __name__ == '__main__':
    main()





