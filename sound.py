# sound effect class
import pygame
class Sound:
    def __init__(self, address):
        self.continue_game = True
        self.address = address

    def play_sound(self):
        pygame.mixer.Sound(self.address)

