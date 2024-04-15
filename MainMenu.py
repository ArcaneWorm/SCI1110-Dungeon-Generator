import pygame
import sys
from subprocess import call

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dungeon Generator")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Font
font = pygame.font.Font(None, 50)


# Opens DungeonGen
def open_py_file():
        call(["python", "DungeonGen.py"])



def main_menu():
    while True:
        screen.fill(WHITE)
        
        # Draw title
        title_text = font.render("Dungeon Generator", True, BLACK)
        title_rect = title_text.get_rect(center=(screen_width//2, 100))
        screen.blit(title_text, title_rect)
        
        # Draw buttons
        play_button = pygame.Rect(screen_width//2 - 100, 250, 200, 50)
        pygame.draw.rect(screen, RED, play_button)
        play_text = font.render("Generate", True, WHITE)
        play_text_rect = play_text.get_rect(center=play_button.center)
        screen.blit(play_text, play_text_rect)
        
        quit_button = pygame.Rect(screen_width//2 - 100, 350, 200, 50)
        pygame.draw.rect(screen, RED, quit_button)
        quit_text = font.render("Quit", True, WHITE)
        quit_text_rect = quit_text.get_rect(center=quit_button.center)
        screen.blit(quit_text, quit_text_rect)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button.collidepoint(mouse_pos):
                    from subprocess import call
                    open_py_file()
                    print("Dungeon has been generated!!")
                    
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
                    
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()