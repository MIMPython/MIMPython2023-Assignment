# Bài tập 10

import numpy
import matplotlib.pyplot as plt


def find_c(A, B):
    # vector AB
    AB = numpy.array(B) - numpy.array(A) 
    # M là trung điểm đoạn AB
    M = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
    # n là vector pháp tuyến của AB có độ dài bằng AB
    n = (-AB[1], AB[0])
    # C1 and C2 là 2 điểm cần tìm
    C1 = tuple(numpy.array(M) + numpy.array(n))
    C2 = tuple(numpy.array(M) - numpy.array(n))
    return C1, C2


# vẽ hình
A = (1, 1)
B = (3, 3)
C1, C2 = find_c(A, B)
plt.text(A[0], A[1], "A")
plt.text(B[0], B[1], "B")
plt.text(C1[0], C1[1], "C1")
plt.text(C2[0], C2[1], "C2")
plt.plot([A[0], B[0]], [A[1], B[1]])
plt.plot([C1[0], C2[0]], [C1[1], C2[1]])
plt.plot([A[0], C1[0]], [A[1], C1[1]])
plt.plot([A[0], C2[0]], [A[1], C2[1]])
plt.plot([B[0], C1[0]], [B[1], C1[1]])
plt.plot([B[0], C2[0]], [B[1], C2[1]])
plt.show()