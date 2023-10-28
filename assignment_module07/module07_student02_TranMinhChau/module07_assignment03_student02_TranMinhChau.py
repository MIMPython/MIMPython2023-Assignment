# Bài tập 3: (geometrical classes)
from additionalFolder.point import Point
from additionalFolder.line import Line
from additionalFolder.circle import Circle

p1 = Point(1, 2)
p2 = Point(3, 4)
line = Line(p1, p2)
circle = Circle(p1, 5)

print(f"Điểm 1: ({p1.x}, {p1.y})")
print(f"Điểm 2: ({p2.x}, {p2.y})")
print(f"Đoạn Thẳng Đầu: ({line.start.x}, {line.start.y})")
print(f"Đoạn Thẳng Cuối: ({line.end.x}, {line.end.y})")
print(f"Trung Tâm Hình Tròn: ({circle.center.x}, {circle.center.y}), Bán Kính: {circle.radius}")

""" 
The directory structure is as follows:
module07_student02_TranMinhChau/
    additionalFolder/
        point.py
        line.py
        circle.py
"""
