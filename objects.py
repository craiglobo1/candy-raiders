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

    
    def shoot(self):
        pass


class Projectile:
    def __init__(self, speed, active=False, image="images\laser.png") -> None:
        self.x = 0
        self.y = 0
        self.speed = speed
        self.active = active
        self.image = pygame.image.load(image)
    
    def draw(self, win : pygame.Surface):
        if self.active:
            win.blit(self.image, (self.x, self.y))
    
    def update(self, dt):
        self.y -= dt*self.speed
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, *self.image.get_size())
    
    def set_pos(self, x, y):
        self.x = x 
        self.y = y 


class ProjectilePool:
    def __init__(self, size : int) -> None:
        self.size = size
        self.projectiles : List[Projectile] = [Projectile(3) for _ in range(size)]
        self.cur_projectile = 0
    
    def create(self, x, y):
        self.projectiles[self.cur_projectile].set_pos(x,y)
        self.projectiles[self.cur_projectile].active = True
        self.cur_projectile = (self.cur_projectile+1)%self.size

    def destroy(self, cur_projectile : int):
        self.projectiles[cur_projectile].active = False

    def update(self, dt : float):
        for i, p in enumerate(self.projectiles):
            active = p.active
            if active and p.y > 0:
                p.update(dt)
            else:
                self.destroy(i)

    def draw(self, win):
        for p in self.projectiles:
            if p.active:
                p.draw(win)
    