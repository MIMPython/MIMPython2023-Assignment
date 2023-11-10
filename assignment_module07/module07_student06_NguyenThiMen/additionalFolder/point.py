import numpy as np


class Point:
    def __init__(self, x: int, y: int) -> None:
        '''
        Represent the coordinates of a point on the coordinate plane Oxy
        '''
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Point({self.x},{self.y})'

    def calculate_distances(self, other_point, metric='L2'):
        '''
        Calculate teh distance between two points using the L1 norm or L2(the default metric)
        '''
        point1 = np.array([self.x, self.y])
        point2 = np.array([other_point.x, other_point.y])
        if metric == 'L2':
            return np.linalg.norm(point1 - point2)
        elif metric == 'L1':
            return sum(np.absolute(point1 - point2))

    @classmethod
    def reflect_through_origin(cls, point):
        '''
        A function in the Point class finds the point symmetric
        '''
        reflected_x, reflected_y = -point.x, -point.y
        return cls(reflected_x, reflected_y)
