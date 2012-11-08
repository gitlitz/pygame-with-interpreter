import pygame
from static import tools
class SpriteBatch():
    def __init__(self):
	self.draw=set()
    
    def add(self,drawAble):
        a=(drawAble.zIndex,drawAble)
        self.draw.add(a)
        print(self.draw)

    def remove(self,drawAble):
        a=drawAble.zIndex,drawAble
        self.draw.remove(a)

    def drawNow(self):
	c=tools.camera
	screen=tools.screen
	for i in self.draw:
	    #change i to the drawAbleObject
	    i=i[1]
	    pos=i.position[0]-c[0],i.position[1]-c[1]
	    screen.blit(i.image,pos)
