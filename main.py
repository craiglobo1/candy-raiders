from operator import imod
import pygame
from objects import Player

size = width, height  = 700, 800

class Game:
    def __init__(self) -> None:
        pygame.font.init()
        pygame.init()
        self.win = pygame.display.set_mode(size,pygame.SRCALPHA)
        pygame.display.set_caption("Candy Raiders")
        self.clock = pygame.time.Clock()

    
    def new(self):
        self.player = Player(100, 100)
        self.run()

    def main_menu(self,win,):
        self.playing = True
        while self.playing == True:
            self.clock.tick(60)
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
            
            pygame.display.flip()



    def run(self):

        self.main_menu(self.win)

        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
        

    def update(self):
        pass
        

    def draw(self):
        self.player.draw(self.win)
        pygame.display.flip()
        self.win.fill(0)


game = Game()

game.new()