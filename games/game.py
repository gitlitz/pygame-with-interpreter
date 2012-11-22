from updateable import UpdateAble
from static import tools
import pygame

class Game(UpdateAble):
    def __init__(self):
        tools.init()
	UpdateAble.__init__(self)
	tools.draw.append(self.draw)
	tools.update.append(self._update_keys)

    def _update_keys(self):
	for event in pygame.event.get():
	    if event.type == pygame.locals.KEYUP:
		self.on_key_up(event)
    

    def on_key_up(self,key):
	pass

    def draw(self):
	raise NotImplementedError()
