import pygame, sys, random
from pygame.locals import *
pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')

colors = [[40, 60, 200],[140, 120, 20],[239, 60, 21]]
sizes = [30,30,30]
locs = [[100,100],[140,100],[180,100]]
letters = ['s','a','m']
fontObj = pygame.font.Font(None,30)
textSurfaceObj = fontObj.render(letters[0],True,colors[0],None)

# The main function that controls the game
def main () :
  looping = True
  
  # The main game loop
  while looping :
    # Get inputs
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
    
    # Processing
    # This section will be built out later
    
    
    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    for i in range(len(letters)):
      fontObj = pygame.font.Font(None,sizes[i])
      textSurfaceObj = fontObj.render(letters[i],True,colors[i],None)
      WINDOW.blit(textSurfaceObj,locs[i])
    pygame.display.update()
    fpsClock.tick(FPS)
 
main()









