import pygame

class Player:
    def __init__(self, x,y) -> None:
        self.x = x
        self.y = y
    
    def update(self):
        pass
    
    def draw(self, win : pygame.Surface):
        pygame.draw.rect(win, (0,0,255), pygame.Rect(self.x, self.y,60, 30))
