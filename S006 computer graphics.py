import pygame 
from pygame.locals import * 
pygame.init() 
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sejal S006")
window.fill((255, 255, 255)) 
pygame.draw.line(window, (0, 0, 0), [100, 300], [500, 300], 5)
pygame.display.update()

import pygame 
from pygame.locals import * 
pygame.init() 
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sejal S006")
window.fill((255, 255, 255)) 
pygame.draw.circle(window, (0, 255, 0), [300, 300], 170, 0)
pygame.display.update()
