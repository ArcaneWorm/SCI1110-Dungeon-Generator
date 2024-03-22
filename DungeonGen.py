import random
import pygame

TILESIZE = 20               #each grid/tile will be 20 pixels
GRID_W, GRID_H = (58,38)    #screen resolution of 1160 by 760

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
                pygame.draw.rect(grid_surface, pygame.Color("grey"), r, 1) #the grids are just squares drawn next to each other
            grid.append(line)
        return grid, grid_surface
    

    def gen_room(Surface, list = []): #generates a room in a random quadrant of the screen, 
                           #there's going to be 12 quadrants in the screen, 4 (horizontally) by 3 (vertically)

        quadrant = random.randint(1,3) #set from 1-3 rn bc i've only coded for three quadrants on the leftmost side

        #For Quadrants 1-3:
            #The min height is 1 grid (20 pixels) and the max is 12 grids (240 pixels). 
            #This max is because the resolution height is 36 (38 - 1 space from top and 1 from bottom) and is divided into three sections
            #The min width is 1 grid (20 pixels) and the max is 12 grids (240 pixels)
            #This max is because it's the highest max the height can have
        
        if (quadrant == 1): #LEFT(1) TOP
            left = 20*(random.randint(1, 6)) #left side of width (x0), adds 5 bc (12/2)-1
            top = 20*(random.randint(1, 6)) #top of height (y0)
            width = 20*(random.randint(3, 7)) #how far "right" the rectangle goes (x1), starts at 2 to ensure room is at least 2 grid2 big
            height = 20*(random.randint(3, 7)) #how far "down" the rectangle goes (y1)
            dimensions = left, top, width, height
            rect = pygame.draw.rect(Surface, "blue", pygame.Rect(dimensions), 2) #draws the actual rectangle, 
            list.append(rect) 

        if (quadrant == 2): #LEFT(1) MIDDLE
            left = 20*(random.randint(1, 6)) #stays in leftmost part of screen
            top = 20*(random.randint(13, 18)) #max height of quad 1 was 13 (6+7), so it starts there and adds 5
            width = 20*(random.randint(3, 7)) 
            height = 20*(random.randint(3, 7)) 
            dimensions = left, top, width, height
            rect = pygame.draw.rect(Surface, "red", pygame.Rect(dimensions), 2) #each quadrant rect is a different color for sake of testing where they actually generate
            list.append(rect)

        if (quadrant == 3): #LEFT(1) BOTTOM
            left = 20*(random.randint(1, 6)) #stays in leftmost part of screen
            top = 20*(random.randint(25, 30)) #max height of quad 1 was 25 (18+7)
            width = 20*(random.randint(3, 7))
            height = 20*(random.randint(3, 7)) 
            dimensions = left, top, width, height
            rect = pygame.draw.rect(Surface, "green", pygame.Rect(dimensions), 2)
            list.append(rect)
        return list #returns the list of rectangles generated


    #def check_collide(Rect, list=[]):
    #     if (pygame.Rect.collidelist(self.Rect,list) != -1):



def main(): 
    pygame.init()
    Surface = pygame.display.set_mode((TILESIZE * GRID_W, TILESIZE * GRID_H)) #sets the actual screen
    clock = pygame.time.Clock()
    grid, grid_surface = DungeonGen.create_grid()
    running = True
    rectangles = []

    Surface.fill("white")
    Surface.blit(grid_surface, (0,0))

    for x in range(3): #generate however many number of rooms (for testing, just manually change it for now)
        rectangles = DungeonGen.gen_room(Surface)
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            clock.tick(60)

    print(rectangles) #just for our own reference
    

if __name__ == '__main__':
    main()





