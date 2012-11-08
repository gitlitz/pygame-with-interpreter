from drawable import DrawAble
class Pumpkin(DrawAble):
    def __init__(self,position=[0,0]):
	from static import tools
	pumpkin_image=tools.loadImage("foo.png")
	DrawAble.__init__(self,pumpkin_image,position)
