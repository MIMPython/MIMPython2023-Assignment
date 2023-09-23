class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return (f"x coordinate: {self.x}\n"
                f"y coordinate: {self.y}")

    def distance(self, point, metric = "L2"):
        """
        Calculate the distance between two points using two metrics:
        L1 and L2.
        """
        import math
        if metric == "L1":
            distanceL1 = abs(self.x - point.x) + abs(self.y - point.y)
            return distanceL1
        if metric == "L2":
            distanceL2 = round(math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2), 3)
            return distanceL2
        
    def getReflection(self):
        """
        Return the reflection of input point as another class object.
        """
        reflection = self.__class__(-self.x, -self.y)
        return reflection
    
"""
def getReflection(point):
    reflection = Point(-point.x, -point.y)
    return reflection
"""

if __name__ == "__main__":
    # Initiate two points.
    pointA = Point(1, 2)
    pointB = Point(-3, 1)

    # Get pointA's reflection
    A_reflection = pointA.getReflection()
    print(repr(A_reflection))

    # pointA's representation
    print(repr(pointA))




