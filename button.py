# Button Class
import pygame
class Button:
    def __init__(self, x, y, width, height,win,activation) -> None:
        self.activation = activation
        self.continue_game = True
        self.win = win
        self.rect = pygame.Rect(x,y,width,height)
    def selected(self,x,y):
        position = (x,y)
        if not self.activation:
            return False
        else:
            return self.rect.collidepoint(position)
    def get_activation(self):
        return self.activation
