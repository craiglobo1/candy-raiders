import pygame
from typing import List 

class Player:
    def __init__(self, x, y, acc=0, drag=-0.09,max_dx=4) -> None:
        self.x = x
        self.y = y

        self.image = pygame.image.load("images\candy_ship.png")

        self.width, self.height = self.image.get_size()
        self.dx = 0

        self.acc = acc
        self.drag = drag
        self.max_dx = max_dx

        self.RIGHT = False
        self.LEFT = False

        self.projectiles = ProjectilePool(10)

    
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

        self.projectiles.update(dt)
        
    
    def draw(self, win : pygame.Surface):
        win.blit(self.image, (self.x, self.y))
        # pygame.draw.rect(win, (0,0,255), pygame.Rect(self.x, self.y, self.width, self.height))

        self.projectiles.draw(win)

    
    def shoot(self):
        self.projectiles.create(self.x + self.width*0.5, self.y - 10)
    


class Enemy:
    def __init__(self, x, y, image="images\candy_monster.png") -> None:
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.width, self.height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.width*0.3, self.height*0.3))
        self.width, self.height = self.image.get_size()

        self.projectiles = ProjectilePool(10, direction=1)


    def update(self, dt):

        self.projectiles.update(dt)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy 
    
    def draw(self, win : pygame.Surface):
        win.blit(self.image, (self.x, self.y))

        self.projectiles.draw(win)

    
    def shoot(self):
        self.projectiles.create(self.x + self.width*0.5, self.y + self.height + 10)



class EnemySpawner:
    def __init__(self,start_x, end_x , dx = 1) -> None:
        self.start_x = start_x 
        self.end_x = end_x
        
        self.dx = dx
        self.dir = 1
        self.dy = 0
    
    def update(self, dt):
        pass

    def draw(self, win : pygame.Surface):
        pass

    def kill_enemy(self, rect : pygame.Rect):
        pass

class Projectile:
    def __init__(self, speed, direction=-1, active=False, image="images\laser.png") -> None:
        self.x = 0
        self.y = 0
        self.speed = speed
        self.active = active
        self.image = pygame.image.load(image)
        self.direction = direction
    
    def draw(self, win : pygame.Surface):
        if self.active:
            win.blit(self.image, (self.x, self.y))
    
    def update(self, dt):
        if self.active:
            self.y += dt*self.speed*self.direction
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, *self.image.get_size())
    
    def set_pos(self, x, y):
        self.x = x 
        self.y = y 


class ProjectilePool:
    def __init__(self, size : int, rate_of_fire : float = 30, direction = -1) -> None:
        self.size = size
        self.projectiles : List[Projectile] = [Projectile(3,direction) for _ in range(size)]
        self.cur_projectile = 0
        self.rate_of_fire = rate_of_fire
        self.time_till_last_fire = rate_of_fire
    
    def create(self, x, y):
        if self.time_till_last_fire < self.rate_of_fire:
            return

        self.projectiles[self.cur_projectile].set_pos(x,y)
        self.projectiles[self.cur_projectile].active = True
        self.cur_projectile = (self.cur_projectile+1)%self.size
        self.time_till_last_fire = 0

    def destroy(self, cur_projectile : int):
        self.projectiles[cur_projectile].active = False

    def update(self, dt : float):
        self.time_till_last_fire += dt

        for i, p in enumerate(self.projectiles):
            if p.y > 0:
                p.update(dt)
            else:
                self.destroy(i)

    def draw(self, win):
        for p in self.projectiles:
            if p.active:
                p.draw(win)


