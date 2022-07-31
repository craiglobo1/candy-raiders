import pygame
from random import randint
from typing import List 


class HealthBar:
    def __init__(self, x, y, width, height, health=100) -> None:
        self.image = pygame.Surface((width,height))
        self.x = x
        self.y = y
        self.health = 100
    
    def draw(self, win : pygame.Surface):
        self.bar = pygame.Surface((self.health,height))
        self.image.blit()
        win.blit(self.image, (self.x, self.y))


class Player:
    def __init__(self, x, y, acc=0, drag=-0.09,max_dx=4) -> None:
        self.x = x
        self.y = y

        self.image = pygame.image.load("images\candy_ship.png")

        self.width, self.height = self.image.get_size()
        self.dx = 0

        self.health = 100

        self.acc = acc
        self.drag = drag
        self.max_dx = max_dx

        self.RIGHT = False
        self.LEFT = False

        self.projectiles = ProjectilePool(10, direction=1)
        self.health = 100
    
    def move(self, right, left):
        self.RIGHT = right
        self.LEFT = left

    def update(self, dt):
        self.projectiles.update(dt)

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
        win.blit(self.image, (self.x, self.y))
        # pygame.draw.rect(win, (0,0,255), pygame.Rect(self.x, self.y, self.width, self.height))

        self.projectiles.draw(win)
    
    def shoot(self):
        self.projectiles.create(self.x + self.width*0.5, self.y+5)
    
    def damage(self, rect : pygame.Rect, damage : int):
        
        collided = rect.colliderect(self.get_rect())
        if collided:
            self.health -= damage

        return collided
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y,self.width, self.height)
    



class Enemy:
    def __init__(self, x, y, rate_of_fire=150, active=False,image="images\candy_monster.png") -> None:
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.width, self.height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.width*0.3, self.height*0.3))
        self.width, self.height = self.image.get_size()

        self.active = active
        self.rate_of_fire = rate_of_fire 

        self.projectiles = ProjectilePool(10,direction=-1)
        self.time_till_last_proj = rate_of_fire

        self.health = 50


    def update(self, dt):
        if self.active:
            self.time_till_last_proj += dt
            self.projectiles.update(dt)
            

            if self.time_till_last_proj < self.rate_of_fire:
                return
            self.shoot()
            self.time_till_last_proj = 0
    
    def move(self, dx, dy):
        if self.active:
            self.x += dx
            self.y += dy 
    
    def draw(self, win : pygame.Surface):
        if self.active:
            win.blit(self.image, (self.x, self.y))
            self.projectiles.draw(win)
    
    def shoot(self):
        if self.active:
            self.projectiles.create(self.x + self.width*0.5, self.y + self.height + 10)
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    



class EnemySpawner:
    def __init__(self,start_x, end_x, game_height, speed=1, rate_of_fire=180, dx = 1, size=10) -> None:
        self.start_x = start_x
        self.end_x = end_x
        self.speed = speed
        self.rate_of_fire = rate_of_fire
        self.size = size
        self.game_height = game_height
        
        self.dx = dx
        self.dir = 1
        self.dy = 0

        self.enemies = [ Enemy(randint(self.start_x,self.end_x), 0) for i in range(size)]
        self.time_till_last_spawn = 180
        self.cur_enemy : int = 0

        self.health_player=100
    
    def update(self, dt):
        self.time_till_last_spawn  += dt
        for e in self.enemies:
            if e.active:
                e.move(0, self.speed)
                e.update(dt)

                if e.y > self.game_height- e.height:
                    return True

        self.create_enemy()
        return False

    def draw(self, win : pygame.Surface):
        for e in self.enemies:
            if e.active:
                e.draw(win)

    def create_enemy(self):
        if self.time_till_last_spawn < self.rate_of_fire:
            return
        
        self.time_till_last_spawn = 0
        self.enemies[self.cur_enemy].active = True
        self.cur_enemy = (self.cur_enemy+1)%self.size
        

    def damage(self, rect : pygame.Rect, damage : int):
        
        collided=rect.collidelist([e.get_rect() for e in self.enemies])
        if collided != -1:
            self.enemies[collided].health -= damage
            if self.enemies[collided].health <= 0:
                self.enemies[collided].active = False
                self.enemies[collided].x = randint(self.start_x,self.end_x)
                self.enemies[collided].y = 0
                self.enemies[collided].health = 50
        return collided != -1
    


class Projectile:
    def __init__(self, speed, direction, active=False, image="images\laser.png") -> None:
        self.x = 0
        self.y = 0
        self.damage = 25
        self.speed = speed
        self.active = active
        self.image = pygame.image.load(image).convert()
        self.direction = direction
    
    def draw(self, win : pygame.Surface):
        if self.active:
            win.blit(self.image, (self.x, self.y))
    
    def update(self, dt):
        if self.active:
            self.y -= dt*self.speed*self.direction
    
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

    def get_all(self):
        return self.projectiles


class Animator:
    def __init__(self, sprites_path, init_state, scale=0.3) -> None:
        pass