from game import Game
import pygame.locals as k
from io import Pumpkin
class Game1(Game):
    def __init__(self):
	Game.__init__(self)
    def update(self):
	pass
    def draw(self):
	pass
    def on_key_up(self,event):
	print(event)
	if event.key==k.K_SPACE:
	    Pumpkin([0,0])
