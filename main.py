from operator import imod
import pygame
from objects import EnemySpawner, Player, Animator
from button import Button
from sound import Sound

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
        pygame.mixer.music.load(r'C:\Users\alyse\OneDrive\Documents\GitHub\candy-raiders\data\images\music\background_music.wav')
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)
        background_colour = (255,97,97)
        rect = pygame.Rect(225,300,250,75)
        middle_rect = pygame.Rect(225,420,250,75)
        end_rect = pygame.Rect(225,540,250,75)
        rules_surface = pygame.Surface((width,height))
        rules_surface.fill(background_colour)
        game_mode_surface = pygame.Surface((width,height))
        game_mode_surface.fill(background_colour)
        rule_rect = pygame.Rect(100,100,500,560)
        popup_colour = (175,242,255)
        rect_colour=(255,97,97)
        A_rect = pygame.Rect(100,100,500,560)
        game_popup = False

        rules_popup =False
        start_play = False

        self.playing = True
        play_button = Button(225,300,250,75,self.win,True)
        rule_button = Button(225,425,250,75,self.win,True)
        quit_button = Button(225,540,250,75,self.win,True)
        music_button = Button(600,10,80,80,self.win,True)
        rule_cancel_button = Button(210,470,280,105,rules_surface,False)
        play_exit_button = Button(525,115,80,80,game_mode_surface,False)
        infinite_button = Button(225,200,275,105,game_mode_surface,False)
        timed_button = Button(225,300,275,90,game_mode_surface,False)

        control_page = pygame.image.load("data/images/rules_popup.png")
        cancel_box = pygame.image.load("data/buttons/cancel_button.png")
        game_title= pygame.image.load("data/images/game_title.png")
        background = pygame.image.load('data/images/background_still.png')
        rules_font = pygame.image.load("data/buttons/rules_button.png")
        quit_font = pygame.image.load('data/buttons/quit_button.png')
        play_font = pygame.image.load('data/buttons/play_button.png')
        infinite = pygame.image.load('data/buttons/infinite_button.png')
        timed = pygame.image.load('data/buttons/timed_button.png')
        mode_background = pygame.image.load('data/images/game_mode_popup.png')
        while self.playing == True:
            pos = pygame.mouse.get_pos()
            self.clock.tick(60)
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    if self.playing:
                        self.playing = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
           
                    if pygame.mouse.get_pressed()[0]:
                        
                       
                            
                            
                        if quit_button.selected(*pos):
                            self.playing = False


                        elif rule_button.selected(*pos):
                            rules_popup = True
                            play_button = Button(225,300,250,75,self.win,False)
                            rule_button = Button(225,420,250,75,self.win,False)
                            quit_button = Button(225,540,250,75,self.win,False)
                            music_button = Button(600,10,80,80,self.win,False)
                            rule_cancel_button = Button(210,470,280,105,rules_surface,True)



                        elif music_button.selected(*pos):
                            self.toggle_music()



                        if rules_popup == True:
                            if rule_cancel_button.selected(*pos):
                                rules_popup = False
                                play_button = Button(225,300,250,75,self.win,True)
                                rule_button = Button(225,420,250,75,self.win,True)
                                quit_button = Button(225,540,250,75,self.win,True)
                                music_button = Button(600,10,80,80,self.win,True)
                                rule_cancel_button = Button(210,470,280,105,rules_surface,False)

                        
                        elif play_button.selected(*pos):
                            game_popup = True
                            if game_popup == True:
                                play_button = Button(225,300,250,75,self.win,False)
                                rule_button = Button(225,420,250,75,self.win,False)
                                quit_button = Button(225,540,250,75,self.win,False)
                                music_button = Button(600,10,80,80,self.win,False)
                                infinite_button = Button(225,200,275,105,game_mode_surface,True)
                                play_exit_button = Button(525,115,80,80,game_mode_surface,True)
                                print(play_button.get_activation())
                            elif timed_button.selected(*pos):
                                timed_button = Button(225,300,275,90,game_mode_surface,True)
                            elif infinite_button.selected(*pos):
                                return
                          
                            elif play_exit_button.selected(*pos):
                                
                                game_popup = False
                                
                                play_button = Button(225,300,250,75,self.win,True)
                                rule_button = Button(225,420,250,75,self.win,True)
                                quit_button = Button(225,540,250,75,self.win,True)
                                music_button = Button(600,10,80,80,self.win,True)
                    
                                play_exit_button = Button(525,115,80,80,game_mode_surface,False)
                                infinite_button = Button(225,200,275,105,game_mode_surface,False)
                                timed_button = Button(225,300,275,90,game_mode_surface,False)
                        
                                
                            
                        




                           
                        
            
            music_pic = pygame.image.load('data/buttons/music_button_toggled.png')
            self.win.blit(music_pic,(600,10))

            pygame.draw.rect(self.win,rect_colour, middle_rect, width == 1, border_radius=10)
            pygame.draw.rect(self.win,rect_colour, end_rect, width == 1, border_radius=10)
            self.win.blit(background,(0,0))
            self.win.blit(game_title,(50,100))
            self.win.blit(play_font,(225,300))
            self.win.blit(rules_font,(225,425))
            self.win.blit(quit_font,(225,540))
            self.win.blit(music_pic,(600,10))
            game_mode_surface.blit(mode_background,(100,50))
            game_mode_surface.blit(infinite, (225,200))
            game_mode_surface.blit(timed, (225,300))
            game_mode_surface.blit(cancel_box,(215,500))
            rules_surface.blit(control_page,(100,30))
            rules_surface.blit(cancel_box,(210,470))
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
        game_background = pygame.image.load('data/images/game_background.png')
        self.win.blit(game_background,(0,0))
        self.enemies.draw(self.win)
        self.player.draw(self.win)

        if self.end_screen:
            blue_colour = (175,242,255)
            button_colour = (52,209,199)
            middle_rect = pygame.Rect(225,420,250,75)
            end_rect = pygame.Rect(225,540,250,75)
            bg_black = pygame.Surface((width,height))
            bg_black.fill(blue_colour)
            title_font = pygame.font.SysFont('agencyfb',150 )
            game_over_text = title_font.render('Game Over!',True,button_colour)
            bg_black.blit(game_over_text,(100,300))
            self.win.blit(bg_black, (0,0))

        pygame.display.flip()
        self.win.fill(0)

    def draw_text(self, win, text, pos, font):
        
        img = font.render(text, True, (255,255,255))
        win.blit(img, pos)


game = Game()

game.new()