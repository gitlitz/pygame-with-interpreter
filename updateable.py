from static import tools
class UpdateAble(object):
    def __init__(self):
	tools.update.add(self.update)
    def update(self):
	raise NotImplementedError()
    def __del__(self):
	tools.update.remove(self.update)
