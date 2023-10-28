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
    
    def isCollinear(self, point1, point2):
        """
        Check if current point and two other points are collinear.
        ~ Check if current point lies on the line connecting two given
        points (can also be implemented in class Line).
        """
        a1, a2 = point1.x, point1.y
        b1, b2 = point2.x, point2.y
        return abs((a2 - b2)*(self.x - b1) + (b1 - a1)*(self.y - b2)) == 0