from fGame import Game
from fV2 import V2
import pygame
class Game1(Game):
    
    angle = 0
    pos = V2.One() * 150
    
    def load_content(self):
        self.car = pygame.image.load('images\schnitzelimage.png').convert_alpha()

 
    def update(self, events):
        #self.pos+=4
        self.angle+=1
        rotatedCar=pygame.transform.rotate(self.car,self.angle)
        self.screen.blit(rotatedCar,self.pos.getArray())
        #//if (self.angle % 2 == 0):
        #    self.screen.blit(rotatedCar,self.pos.getArray())
        #else:
        #    self.screen.blit(self.car,self.pos.getArray())
    
