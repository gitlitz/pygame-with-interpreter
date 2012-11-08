from static.tools import spritebatch
class DrawAble(object):
    def __init__(self,image,position,zIndex=0,activated=True):
	print("started")
	self.image=image
	self.position=position
	self._zIndex=zIndex
	self.__activated=None
	self.activated=activated


    def __del__(self):
	self.activated=False

#zindex
    def __getZIndex(self):
        return self._zIndex
    
    zIndex=property(__getZIndex)

#enabled

    def _disable(self):
	spritebatch.remove(self)

    def _enable(self):
        spritebatch.add(self)

    def __setActivated(self,b):
	if self.__activated!=b:
	    self.__activated=b
	    if b:
		print("enable")
		self._enable()
	    else:
		print("disable")
		self._disable()

    def __getActivated(self):
	return self.__activated

    activated=property(__getActivated,__setActivated)

