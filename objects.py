import pygame
from typing import List 

class Player:
    def __init__(self, x, y, acc=0, drag=-0.09,max_dx=4) -> None:
        self.x = x
        self.y = y
        self.dx = 0

        self.acc = acc
        self.drag = drag
        self.max_dx = max_dx

        self.RIGHT = False
        self.LEFT = False

        self.projectiles : List[Projectile] = [Projectile(0, 0, 15) for _ in range(5)]
    
    def move(self, right, left):
        self.RIGHT = right
        self.LEFT = left

    def update(self, dt):
        self.acc = 0
        if self.RIGHT:
            self.acc += .3
        if self.LEFT:
            self.acc-= .3

        self.acc += self.dx * self.drag
        self.dx += self.acc*dt

        # limit velocity
        min(-self.max_dx, max(self.dx, self.max_dx))
        if  abs(self.dx) < .1:
            self.dx = 0

        self.x += self.dx * dt + (self.acc * .5) * (dt *dt)
        
    
    def draw(self, win : pygame.Surface):
        pygame.draw.rect(win, (0,0,255), pygame.Rect(self.x, self.y,60, 30))

        for p in self.projectiles:
            p.draw(win)
    
    def shoot(self)


class Projectile:
    def __init__(self, x, y, speed, visible=False, image="images/laser.png") -> None:
        self.x = x
        self.y = y
        self.speed = speed
        self.visible = False
        self.image = pygame.image.load(image).convert()
    
    def draw(self, win : pygame.Surface):
        if self.visible:
            win.blit(self.image, (self.x, self.y))
    
    def update(self, dt):
        self.y -= dt*self.speed
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, *self.image.get_size())
