#configured at main->GUI.createPygameWindow
screen=None
interpreter=None
colors={'black':(0,0,0),'white':(255,255,255)}
#configured at init
camera=None
update=None
draw=None
spritebatch=None

import pygame
import gobject
import config

#
def _update():
    for i in update:
        i()
#    camera[0]+=0.5
#    print (camera)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pass
    screen.fill(colors["black"])
    for i in draw:
        i()
    pygame.display.flip()
    return True

def loadImage(imageName):
    return pygame.image.load('images\\'
	    +imageName).convert_alpha()

def init():
    global camera,update,draw,spritebatch
    camera=[0,0]
    update=[]
    draw=[]
    from spritebatch import SpriteBatch
    spritebatch=SpriteBatch()
    draw.append(spritebatch.drawNow)
    gobject.timeout_add(
	    config.TimeBetweenFrames,
	    _update) #timer
    #drawExample()


def drawExample():
    img=loadImage('foo.png')
    pos=0,0
    from drawable import DrawAble
    global d
    d=DrawAble(img,pos)
    
def drawExample2():
    img=loadImage('foo.png')
    pos=30,30
    from drawable import DrawAble
    d=DrawAble(img,pos)
