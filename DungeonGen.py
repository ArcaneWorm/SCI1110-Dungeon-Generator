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
    

    def gen_room(Surface, list=[]): #generates a room in a random quadrant of the screen

        #there's going to be 12 quadrants in the screen, 4 (horizontally) by 3 (vertically)
        quadrant = random.randint(1,12) #picks a random quadrant to generate a room in

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
            color = "plum" 

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

        room = pygame.draw.rect(Surface, color, pygame.Rect(dimensions), 2) #draws the actual rectangle, 
        list.append(room) #adds to list of rectangles/rooms generated
        return list 


    def is_intersecting(Rect, list=[]): #returns true if rectangles are intersecting
         #if there's no intersections in the list, it returns an empty list (which is considered false)
         if (pygame.Rect.collidelistall(Rect,list)):
             return False
         else:
             return True
             
            
    #def connect_rooms(list=[]):
         





def main(): 
    pygame.init()
    Surface = pygame.display.set_mode((TILESIZE * GRID_W, TILESIZE * GRID_H)) #sets the actual screen
    clock = pygame.time.Clock()
    grid, grid_surface = DungeonGen.create_grid()
    running = True
    rectangles = []

    Surface.fill("white")
    Surface.blit(grid_surface, (0,0))

    for x in range(10): #generate however many number of rooms (for testing, just manually change it for now)
        rectangles = DungeonGen.gen_room(Surface, rectangles)
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            clock.tick(60)

    #print(rectangles) #just for our own reference
    

if __name__ == '__main__':
    main()





