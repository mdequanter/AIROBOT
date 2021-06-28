# Eenvoudige Pygame setup

# Importeren en initialiseren pygame
import pygame
# Import Robotlib
from robotlib import Robot
import time

pygame.init()

# setup van scherm
screen = pygame.display.set_mode([1900, 1080])


robot1 = Robot("robot1",True)
robot2 = Robot("robot2",True)

robot1.setcolor((0, 0, 255))  # blauw
robot2.setcolor((255, 0, 255))



# Lopen zolang het scherm niet wordt afgesloten
running = True
move=0
while running:

    move = move+5
    screen.fill((255, 255, 255))
    robot1.forward(move,screen)
    robot2.backward(move,screen)    
    time.sleep(0.5)
    screen.fill((255, 255, 255))
    robot1.left(move,screen)
    robot2.right(move,screen)
    time.sleep(0.5)
    screen.fill((255, 255, 255))
    robot2.left(move,screen)
    robot1.right(move,screen)
    time.sleep(0.5)
    screen.fill((255, 255, 255))
    robot2.forward(move,screen)
    robot1.backward(move,screen)
    time.sleep(0.5)




    # Kijken wanneer er iemand op sluit kruisje klikt.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# Done! Time to quit.
pygame.quit()