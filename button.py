# Button Class
import pygame
class Button:
    def __init__(self, x, y, width, height,win) -> None:
        self.continue_game = True
        self.win = win
        self.rect = pygame.Rect(x,y,width,height)
    def selected(self,x,y):
        position = (x,y)
        return self.rect.collidepoint(position)
