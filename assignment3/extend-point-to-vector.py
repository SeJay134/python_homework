# Task 5

import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, value):
        return isinstance(value, Point) and self.x == value.x and self.y == value.y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def distance(self, value):
        return math.sqrt((self.x - value.x)**2 + (self.y - value.y)**2)
    
class Vector(Point):
    def __str__(self):
        return f"Vector<{self.x}, {self.y}>"
    
    def __add__(self, value):
        if not isinstance(value, Vector):
            return NotImplemented
        return Vector(self.x+value.x, self.y+value.y)
    
if __name__ == "__main__":

    p1 = Point(1, 2)
    p2 = Point(4, 6)

    print("Points:")
    print("p1:", p1)
    print("p2:", p2)

    # Equality
    print("p1 == p2", p1 == p2)
    print("p1 == Point(1,2)", p1 == Point(1, 2))

    # Distance
    print("Distance p1 → p2:", p1.distance(p2))

    print("\nVectors:")
    v1 = Vector(1, 1)
    v2 = Vector(2, 3)

    print("v1:", v1)
    print("v2:", v2)

    # Vector addition
    v3 = v1 + v2
    print("v1 + v2 =", v3)