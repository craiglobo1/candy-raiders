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

            
            pygame.display.flip()



    def run(self):

        self.main_menu(self.win)

        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) * .001 * FPS
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


        
        self.player.move(keys[pygame.K_RIGHT]|keys[pygame.K_d], keys[pygame.K_LEFT]|keys[pygame.K_a])
        

    def update(self):
        self.player.update(self.dt)
        

    def draw(self):
        self.player.draw(self.win)
        pygame.display.flip()
        self.win.fill(0)



game = Game()

game.new()