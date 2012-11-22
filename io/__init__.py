from drawable import DrawAble
from updateable import UpdateAble
class Pumpkin(DrawAble,UpdateAble):
    def __init__(self,position=[0,0]):
	from static import tools
	pumpkin_image=tools.loadImage("foo.png")
	DrawAble.__init__(self,pumpkin_image,position)
	UpdateAble.__init__(self)
	
    def update(self):
	self.position[0]+=1
