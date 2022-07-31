from operator import imod
import pygame
from objects import EnemySpawner, Player, Enemy
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
        self.font_roboto = pygame.font.Font("fonts\Roboto-Regular.ttf", 20)
    
    def new(self):
        self.main_menu(self.win)
        self.new_game()

    def new_game(self):
        self.player = Player(width*0.05, height*0.85)
        self.enemies = EnemySpawner(self.player.image.get_width(), width- self.player.image.get_width(),height)
        self.end_screen = False
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
        rule_rect = pygame.Rect(100,100,500,560)
        popup_colour = (175,242,255)
        rect_colour=(255,97,97)
        pygame.draw.rect(rules_surface, popup_colour, rule_rect, width == 1, border_radius=10)
        pygame.draw.rect(game_mode_surface, popup_colour, rule_rect, width == 1, border_radius=10)
        game_popup = False

        rules_popup =False

        self.playing = True
        play_button = Button(225,300,250,75,self.win)
        rule_button = Button(225,420,250,75,self.win)
        quit_button = Button(225,540,250,75,self.win)
        music_button = Button(600,10,80,80,self.win)
        rule_exit_button = Button(525,115,60,60,rules_surface)
        play_exit_button = Button(525,115,60,60,rules_surface)
        infinite_button = Button(225,400,250,75,game_mode_surface)
        timed_button = Button(225,500,250,75,game_mode_surface)


        game_title= pygame.image.load('images/game-title.png')
        rules_font = pygame.image.load('images/rules_button.png')
        quit_font = pygame.image.load('images/quit_button.png')
        play_font = pygame.image.load('images/play_button.png')
        infinite = pygame.image.load('images/infinite_button.png')
        timed = pygame.image.load('images/timed_button.png')
        background = pygame.image.load('images/background_still.png')
        quit_box = pygame.image.load('images/close_button.png')
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
                        
            

            pygame.draw.rect(self.win,rect_colour, middle_rect, width == 1, border_radius=10)
            pygame.draw.rect(self.win,rect_colour, end_rect, width == 1, border_radius=10)
            self.win.blit(background,(0,0))
            self.win.blit(game_title,(50,100))
            self.win.blit(play_font,(225,300))
            self.win.blit(rules_font,(225,425))
            self.win.blit(quit_font,(225,540))
            music_pic = pygame.image.load('images/music_button_toggled.png')
            self.win.blit(music_pic,(600,10))
            game_mode_surface.blit(infinite, (225,400))
            game_mode_surface.blit(timed, (225,500))
            rules_surface.blit(controls_text,(220,100))
            rules_surface.blit(quit_box,(525,115))

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
                if event.key == pygame.K_ESCAPE and self.end_screen:
                    self.end_screen = False
                    self.new_game()
                    self.playing = False
                if event.key == pygame.K_r and self.end_screen:
                    self.end_screen = False
                    self.main_menu(self.win)
                    self.playing = False

        if not self.end_screen:
            self.player.move(keys[pygame.K_RIGHT]|keys[pygame.K_d], keys[pygame.K_LEFT]|keys[pygame.K_a])
        

    def update(self):
        end_game = self.enemies.update(self.dt)
        if end_game:
            self.end_screen = True

        self.player.update(self.dt)

        for l in self.player.projectiles.get_all():
                if l.active:
                    hit = self.enemies.damage(l.get_rect(), l.damage)
                    if hit:
                        l.active = False
        
        for e in self.enemies.enemies:
            for l in e.projectiles.get_all():
                if l.active:
                    hit = self.player.damage(l.get_rect(), l.damage)
                    if hit:
                        l.active = False
        
        if self.player.health < 0:
            self.end_screen = True
    

    def draw(self):
        self.enemies.draw(self.win)
        self.player.draw(self.win)

        if self.end_screen:
            bg_black = pygame.Surface((width,height))
            bg_black.fill(0)
            self.draw_text(bg_black, 'Press ESC to retry the game', (100,100), self.font_roboto)
            self.draw_text(bg_black, 'Press R to go to the main menu', (100,300), self.font_roboto)
            self.win.blit(bg_black, (0,0))
        pygame.display.flip()
        self.win.fill(0)

    def draw_text(self, win, text, pos, font):
        
        img = font.render(text, True, (255,255,255))
        win.blit(img, pos)


game = Game()

game.new()