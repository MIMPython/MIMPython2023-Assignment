# class Point
import numpy as np

class Point:
    '''
    biểu diễn các điểm trong tọa độ Oxy
    '''

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.getter
    def y(self, y):
        self._y = y

    def calculate_distances(self, other_point, metric='L2'):
        '''
        tính khoảng cách 2 điểm theo chuẩn L1 hoặc L2 với metric mặc định là L2
        '''
        point1 = np.array([self._x, self._y])
        point2 = np.array([other_point._x, other_point._y])
        if metric == 'L2':
            return np.linalg.norm(point1 - point2)
        elif metric == 'L1':
            return sum(np.absolute(point1 - point2))

    def reflect_through_origin(self):
        '''
        tạo 1 hàm thuộc class Point tìm điểm đối xứng qua gốc tọa độ
        '''
        reflected_x, reflected_y = -self._x, -self._y
        return self.__class__(reflected_x, reflected_y)

    def __repr__(self):
        return f'({self._x},{self._y})'


if __name__ == '__main__':

    point1 = Point(2, 4)
    point2 = Point(8, 9)
    print(point1)
    print(point2)
    distance_L2 = point1.calculate_distances(point2)
    distance_L1 = point1.calculate_distances(point2, 'L1')
    print(f'L1 distance between{point1} and {point2} is {distance_L1}')
    print(f'L2 distance between {point1} and {point2} is {distance_L2}')
