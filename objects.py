import pygame

class Player:
    def __init__(self, x,y) -> None:
        self.x = x
        self.y = y
        self.dx = 5

        self.RIGHT = False
        self.LEFT = False
    
    def move(self, right, left):
        self.RIGHT = right
        self.LEFT = left

    def update(self, dt):
        if self.RIGHT:
            self.x += self.dx
        if self.LEFT:
            self.x -= self.dx
    
    def draw(self, win : pygame.Surface):
        pygame.draw.rect(win, (0,0,255), pygame.Rect(self.x, self.y,60, 30))
