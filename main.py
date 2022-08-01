from operator import imod
import pygame
from objects import EnemySpawner, Player, Animator
from button import Button
import os, time
 
size = width, height  = 700, 800
FPS = 60
class Game:
    def __init__(self) -> None:
        pygame.font.init()
        pygame.init()
        pygame.mixer.init()

        self.win = pygame.display.set_mode(size,pygame.SRCALPHA)
        pygame.display.set_caption("Candy Raiders")
        icon_surf = pygame.image.load("data\images\cr_icon.png")
        pygame.display.set_icon(icon_surf)

        self.clock = pygame.time.Clock()
        self.font_roboto = pygame.font.Font("fonts\Roboto-Regular.ttf", 64)
        self.backround_music = pygame.mixer.Sound('music/background_music.wav')
        self.backround_music.set_volume(1)
        self.music_channel = self.backround_music.play(-1)
    
    def new(self):
        self.main_menu()
        self.new_game()
 
    def new_game(self):
        self.player = Player(width*0.05, height*0.85)
        self.enemies = EnemySpawner(self.player.animator.get_size()[0], width- self.player.animator.get_size()[1],height, speed=0.8, rate_of_fire=300)
        self.end_screen = False
        self.times_enemy_damaged = 0
        self.frame_count = 60*60

        self.run()
 
    def main_menu(self):
        background_colour = (255,97,97)
        rules_surface = pygame.Surface((width,height))
        rules_surface.fill(background_colour) 
        rules_popup =False
 
        self.playing = True
 
        background = pygame.image.load('data/images/background_still.png')
        game_title = pygame.image.load("data/images/game_title.png")

        play_font = pygame.image.load('data/buttons/play_button.png')
        rules_font = pygame.image.load("data/buttons/rules_button.png")
        quit_font = pygame.image.load('data/buttons/quit_button.png')

        cancel_box = pygame.image.load("data/buttons/cancel_button.png")
        control_page = pygame.image.load("data/images/rules_popup.png")

        play_button = Button(225,300,*play_font.get_size(),self.win,True)
        rule_button = Button(225,425,*rules_font.get_size(),self.win,True)
        quit_button = Button(225,540,*quit_font.get_size(),self.win,True)
        music_button = Button(600,10,80,80,self.win,True)
        rule_cancel_button = Button(210,470,280,105,rules_surface,False)
        while self.playing == True:
            pos = pygame.mouse.get_pos()
            self.clock.tick(60)
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    if self.playing:
                        os._exit(0)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
           
                    if pygame.mouse.get_pressed()[0]:
                            
                        if quit_button.selected(*pos):
                            os._exit(0)
 
                        if rule_button.selected(*pos):
                            play_button.activation = False
                            rule_button.activation = False
                            quit_button.activation = False
                            music_button.activation = False
                            rule_cancel_button.activation = False
                            rules_popup = True



                        if music_button.selected(*pos):
                            self.toggle_music()


                        if rules_popup == True:
                            if rule_cancel_button.selected(*pos):
                                rules_popup = False
                                play_button.activation = True
                                rule_button.activation = True
                                quit_button.activation = True
                                music_button.activation = True
                                rule_cancel_button = Button(210,470,280,105,rules_surface,False)
                                
                            rule_cancel_button.activation = True
 
                        
                        if play_button.selected(*pos):
                            self.new_game()
                            os._exit(0)                        
                
            
            music_pic = pygame.image.load('data/buttons/music_button_toggled.png')
            self.win.blit(music_pic,(600,10))
 
            background.set_alpha(180)
            self.win.blit(background,(0,0))
            self.win.blit(game_title,(50,100))
            self.win.blit(play_font,(225,300))
            self.win.blit(rules_font,(225,425))
            self.win.blit(quit_font,(225,540))
            self.win.blit(music_pic,(600,10))
            rules_surface.blit(control_page,(100,30))
            rules_surface.blit(cancel_box,(210,470))
            if rules_popup:
                self.win.blit(rules_surface, (0,0))
            pygame.display.flip()
            self.win.fill(0)
 
    def toggle_music(self):
        if self.music_channel.get_busy():
            self.backround_music.stop()
        else:
             self.backround_music.play(-1)



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
                if event.key == pygame.K_r and self.end_screen:
                    self.end_screen = False
                    self.new_game()
                    self.playing = False
                if event.key == pygame.K_ESCAPE and self.end_screen:
                    self.end_screen = False
                    self.new()
                    self.playing = False
                if event.key == pygame.K_m:
                    self.toggle_music()
 
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
                    if hit and not end_game:
                        self.times_enemy_damaged += 1
                        l.active = False
                        l.y = 0

        
        for e in self.enemies.enemies:
            for l in e.projectiles.get_all():
                if l.active:
                    hit = self.player.damage(l.get_rect(), l.damage)
                    if hit:
                        l.active = False
                        l.y = 0
        
        if self.player.health.get_health() <= 0:
            self.end_screen = True


            
        
        
        self.total_seconds = 120 - (self.frame_count // FPS)
        if self.total_seconds < 0:
            self.total_seconds = 0
        self.frame_count+=1

        if self.total_seconds <= 0:
            self.end_screen = True


    def draw(self):
        game_background = pygame.image.load('data/images/game_background.png')
        game_background.set_alpha(100)
        self.win.blit(game_background,(0,0))
        self.enemies.draw(self.win)
        self.player.draw(self.win)
        



        output_string = f"{self.total_seconds//60:02}:{self.total_seconds%60:02}"
        font = pygame.font.Font(None, 35)
        text = font.render(output_string, True, (255,255,255))
        pad = 15
        timer_bg = pygame.Surface((text.get_width()+pad, text.get_height()+pad))
        timer_bg.fill((106, 196, 142))
        timer_bg.set_alpha(200)
        timer_bg.blit(text, (pad//2,pad//2))
        self.win.blit(timer_bg, (width//2-timer_bg.get_width()//2, 0))


        if self.end_screen:
            for l in self.player.projectiles.get_all():
                l.active = False
            end_screen_surf = pygame.image.load("data\images\End Screen.png")
            self.win.blit(end_screen_surf, (0,0))
            text_score = self.font_roboto.render(f"{self.times_enemy_damaged*50}", True, (0,0,0))
            self.win.blit(text_score, (width*.5-text_score.get_width()*.5, height*0.35))
            
           
        pygame.display.flip()
        self.win.fill(0)

        
         



game = Game()
 
game.new()
