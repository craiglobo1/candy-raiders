import pygame

size = height, width = 700, 700

class Game:
    def __init__(self) -> None:
        pygame.font.init()
        pygame.init()
        self.win = pygame.display.set_mode(size,pygame.SRCALPHA)
        pygame.display.set_caption("Candy Raiders")
        self.clock = pygame.time.Clock()


    def new(self):

        self.run()

    def run(self):
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
        pygame.display.flip()
        self.win.fill(0)


game = Game()

game.new()