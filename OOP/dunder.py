class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y 

    def __str__(self):
        return f"Vector({self.x}, {self.y}"
    
    def __repr__(self):
        return f"x={self.x}, y={self.y}"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
vec1=Vector(3,4)
vec2=Vector(3,5)

print(str(vec1))          # Calls __str__
print(repr(vec1))         # Calls __repr__
print(vec1 == vec2)      # Calls __eq__
