class V2:    
    
    def __init__(self, x=0, y=0):
        self.values = [x, y]
    
    def setX(self, x):
        self.values[0] = x
    def setY(self, y):
        self.values[1] = y
        
    def changeX(self, x):
        self.values[0] += x
    def changeY(self, y):
        self.values[1] += y
        
    def getX(self):
        return self.values[0]
    def getY(self):
        return self.values[1]

    def getArray(self):
        return self.values
    
    def __add__(self, other):
        if isinstance(other, V2):
            return V2(self.getX() + other.getX(), self.getY() + other.getY())
        else:
            return V2(self.getX() + other, self.getY() + other)
        
    def __sub__(self, other):
        if isinstance(other, V2):
            return V2(self.getX() - other.getX(), self.getY() - other.getY())
        else:
            return V2(self.getX() - other, self.getY() - other);
        
    def __mul__(self, other):
        if isinstance(other, V2):
            return V2(self.getX() * other.getX(), self.getY() * other.getY())
        else:
            return V2(self.getX() * other, self.getY() * other);
        
    def __div__(self, other):
        if isinstance(other, V2):
            return V2(self.getX() / other.getX(), self.getY() / other.getY())
        else:
            return V2(self.getX() / other, self.getY() / other);
    
    @staticmethod  
    def One():
        return V2(1, 1)

    @staticmethod  
    def Zero():
        return V2(0, 0)
    
    @staticmethod  
    def UnitX():
        return V2(1, 0)
    
    @staticmethod  
    def UnitY():
        return V2(0, 1)