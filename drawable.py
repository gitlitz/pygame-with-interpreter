from static.tools import spritebatch
class DrawAble():
    def __init__(self,image,position,zIndex=0,enabled=True):
	self.image=image
	self.position=position
	self._zIndex=zIndex
	if enabled:
	    self.enable()
    
    def getZIndex(self):
        return self._zIndex
    
    zIndex=property(getZIndex)

    def disable(self):
	spritebatch.remove(self)

    def enable(self):
        spritebatch.add(self)
