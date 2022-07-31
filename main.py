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

    def main_menu(self,win):
        pygame.mixer.music.load('music/background_music.wav')
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)
        rect = pygame.Rect(225,300,250,75)
        middle_rect = pygame.Rect(225,420,250,75)
        end_rect = pygame.Rect(225,540,250,75)
        rules_surface = pygame.Surface((width,height))
        game_mode_surface = pygame.Surface((width,height))
        background_colour = (255,97,97)
        rules_surface.fill(background_colour)
        game_mode_surface.fill(background_colour)
        rule_rect = pygame.Rect(100,100,500,600)
        popup_colour = (175,242,255)
        rect_colour=(255,97,97)
        pygame.draw.rect(rules_surface, popup_colour, rule_rect, width == 1, border_radius=10)
        pygame.draw.circle(rules_surface,(255,97,97), (550,150), 30 )
        pygame.draw.rect(game_mode_surface, popup_colour, rule_rect, width == 1, border_radius=10)
        pygame.draw.circle(game_mode_surface,rect_colour, (550,150), 30 )
        game_popup = False

        rules_popup =False

        self.playing = True
        play_button = Button(225,300,250,75,self.win)
        rule_button = Button(225,420,250,75,self.win)
        quit_button = Button(225,540,250,75,self.win)
        music_button = Button(600,10,64,64,self.win)
        rule_exit_button = Button(525,115,60,60,rules_surface)
        play_exit_button = Button(525,115,60,60,rules_surface)
        infinite_button = Button(225,400,250,75,game_mode_surface)
        timed_button = Button(225,500,250,75,game_mode_surface)


        game_title= pygame.image.load('images/game-title.png')
        rules_font = pygame.image.load('images/rules_button.png')
        quit_font = pygame.image.load('images/quit-font.png')
        play_font = pygame.image.load('images/play_button.png')
        infinite = pygame.image.load('images/infinite_button.png')
        timed = pygame.image.load('images/timed_button.png')
        background = pygame.image.load('images/background_still.png')
        control_font = pygame.font.SysFont('agencyfb',100 )
        minor_control_font = pygame.font.SysFont('agencyfb',60 )
        minor_controls_text = control_font.render('Controls',True,rect_colour)
        controls_text =  control_font.render('To move',True,rect_colour)
        while self.playing == True:
            pos = pygame.mouse.get_pos()
            self.clock.tick(60)
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    if self.playing:
                        self.playing = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if play_button.selected(*pos):
                            game_popup = True
                        if quit_button.selected(*pos):
                            self.playing = False
                        if rule_button.selected(*pos):
                            rules_popup = True
                        if music_button.selected(*pos):
                            self.toggle_music()
                        if rule_exit_button.selected(*pos):
                           rules_popup = False
                        if play_exit_button.selected(*pos):
                           game_popup = False
                        if infinite_button.selected(*pos):
                            pass
                        if timed_button.selected(*pos):
                            pass
                        
            
            music_pic = pygame.image.load('images/music_note.png')
            self.win.blit(music_pic,(600,10))

            pygame.draw.rect(self.win,rect_colour, middle_rect, width == 1, border_radius=10)
            pygame.draw.rect(self.win,rect_colour, end_rect, width == 1, border_radius=10)
            self.win.blit(background,(0,0))
            self.win.blit(game_title,(50,100))
            self.win.blit(play_font,(225,300))
            self.win.blit(rules_font,(290,425))
            self.win.blit(quit_font,(290,540))
            game_mode_surface.blit(infinite, (225,400))
            game_mode_surface.blit(timed, (225,500))
            rules_surface.blit(controls_text,(220,100))

            if rules_popup:
                self.win.blit(rules_surface, (0,0))
            if game_popup:
                self.win.blit(game_mode_surface, (0,0))

            pygame.display.flip()
            self.win.fill(0)


    def toggle_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
             pygame.mixer.music.unpause()



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



            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()
        
        self.player.move(keys[pygame.K_RIGHT]|keys[pygame.K_d], keys[pygame.K_LEFT]|keys[pygame.K_a])
        

    def update(self):
        self.player.update(self.dt)
        

    def draw(self):
        self.player.draw(self.win)
        pygame.display.flip()
        self.win.fill(0)



game = Game()

game.new()