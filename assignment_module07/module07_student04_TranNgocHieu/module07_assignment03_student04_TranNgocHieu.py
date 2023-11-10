"""
Làm một bài toán hình học nào đó.
Phép biến đổi Morbius (hay phép biến đổi phân tuyến tính) 
là một phép biến đổi trên mặt phẳng phức có dạng
z --> (az + b)/(cz + d)
trong đó a, b, c, d là các số phức. Nó có nhiều tính chất đẹp, và mô tả
tổng quát nhất của nó là hợp thành của các phép tịnh tiến, quay quanh tâm,
đối xứng qua trục thực và nghịch đảo. Sau đây ta sử dụng hình vẽ để thấy
rằng đây là một phép nghịch đảo, tức là biến một đường thẳng (nói chung)
thành một đường tròn (và ngược lại), cho một hàm cụ thể là
z --> (z + 1)/(2z - 1)
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.patches
from additionalFolder import Point
from additionalFolder import Line
from additionalFolder import Circle

def Morbius(tup):
    z = tup[0] + tup[1] * 1j
    image = (z + 1)/(2*z - 1)
    return Point(image.real, image.imag)

# a = random.uniform(1, 10)
# print(a)
# random_line = Line(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
random_point = (
    round(random.uniform(-1, 1), 2), 
    round(random.uniform(-1, 1), 2)
    )
random_vector = (
    round(random.uniform(-1, 1), 2), 
    round(random.uniform(-1, 1), 2)
    )

# Tạo 3 điểm bất kỳ khác trên đường thẳng đã cho.
(t1, t2, t3) = [round(random.uniform(-5 ,5), 2) for i in range(3)]
P1 = (
    random_point[0] + t1 * random_vector[0], 
    random_point[1] + t1 * random_vector[1]
    )
P2 = (
    random_point[0] + t2 * random_vector[0], 
    random_point[1] + t2 * random_vector[1]
    )
P3 = (
    random_point[0] + t3 * random_vector[0], 
    random_point[1] + t3 * random_vector[1]
    )


z0 = Morbius(random_point)
z1 = Morbius(P1)
z2 = Morbius(P2)
z3 = Morbius(P3)
z_Circle = Circle(z1, z2, z3)
print(z_Circle.center)
print(z_Circle.radius)

fig, ax = plt.subplots()
ax.plot([random_point[0], P1[0], P2[0], P3[0]],
        [random_point[1], P1[1], P2[1], P3[1]],
        "-o"
    )
ax.add_artist(matplotlib.patches.Circle(
    (z_Circle.center.x, z_Circle.center.y),
    z_Circle.radius,
    fill = False
))
ax.plot([z0.x, z1.x, z2.x, z3.x], [z0.y, z1.y, z2.y, z3.y], "ro")

ax.set(xlim = (-3, 3), ylim = (-3, 3), aspect = "equal")
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()