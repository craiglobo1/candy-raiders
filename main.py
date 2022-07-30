from operator import imod
import pygame
from objects import Player
from button import Button

size = width, height  = 700, 800
FPS = 60

class Game:
    def __init__(self) -> None:
        pygame.font.init()
        pygame.init()
        self.win = pygame.display.set_mode(size,pygame.SRCALPHA)
        pygame.display.set_caption("Candy Raiders")
        self.clock = pygame.time.Clock()

    
    def new(self):
        self.player = Player(width*0.05, height*0.9)
        self.run()

<<<<<<< HEAD
<<<<<<< HEAD
    def main_menu(self,win,):
        self.playing = True
        pos = pygame.mouse.get_pos()
        play_button = Button(225,300,250,75,self.win)
        quit_button = Button(225,420,250,75,self.win)
        while self.playing == True:
            self.clock.tick(60)
            bg_colour= (153, 204, 255)
            background= pygame.image.load('images/background.png')
            self.win.blit(background,(0,0))
            rect_colour=(255, 102, 178)
            rect = pygame.Rect(225,300,250,75)
            middle_rect = pygame.Rect(225,420,250,75)
            end_rect = pygame.Rect(225,540,250,75)
            pygame.draw.rect(self.win,rect_colour, rect, width == 0)
            pygame.draw.rect(self.win,rect_colour, middle_rect, width == 0)
            pygame.draw.rect(self.win,rect_colour, end_rect, width == 0)
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    if self.playing:
                        self.playing = False
                if event.type == pygame.mouse.get_pressed():
                    if play_button.selected(pos):
                        return
                    if quit_button == pygame.mouse.get_pressed():
                        if quit_button.selected(pos):
                            self.playing = False

=======
    def main_menu(self,win,):
        self.playing = True
        while self.playing == True:
            bg_colour= (3, 244, 252)
            self.win.fill(bg_colour)
            ellipsis_colour=(245, 78, 200)
            pygame.draw.rect
            rect = pygame.Rect(50,100,600,400)
            pygame.draw.ellipse(self.win,ellipsis_colour, rect, width == 0)
            font = pygame.font.SysFont('Corbel',60,bold=pygame.font.Font.bold)
            font_colour = (237, 192, 225)
            game_title = pygame.font.Font.render(font,'Candy Raiders', True, font_colour)
            self.win.blit(game_title,(100,400))
            pygame.font.get_fonts()
>>>>>>> 3befc4c61cc2be535397db33eb4148d014aeb2d2
            
            pygame.display.flip()


<<<<<<< HEAD
=======
    def main_menu(self):
        pass
>>>>>>> 5befa1f90ae391928160e901873cce479ffc656c
=======
>>>>>>> 3befc4c61cc2be535397db33eb4148d014aeb2d2

    def run(self):

        self.main_menu(self.win)

        self.playing = True
        while self.playing:
<<<<<<< HEAD
            self.dt = self.clock.tick(FPS) * .001 * FPS
=======
            self.dt = self.clock.tick(120)
>>>>>>> 3befc4c61cc2be535397db33eb4148d014aeb2d2
            self.events()
            self.update()
            self.draw()

    def events(self):
        pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
<<<<<<< HEAD


=======
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()
>>>>>>> 5befa1f90ae391928160e901873cce479ffc656c
        
        self.player.move(keys[pygame.K_RIGHT]|keys[pygame.K_d], keys[pygame.K_LEFT]|keys[pygame.K_a])
        

    def update(self):
        self.player.update(self.dt)
        

    def draw(self):
        self.player.draw(self.win)
        pygame.display.flip()
        self.win.fill(0)



game = Game()

game.new()