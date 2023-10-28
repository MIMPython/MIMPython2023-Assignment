# Bài tập yêu cầu viết một chương trình giải quyết một bài toán Hình học cơ bản

"""
Orthocenter Theorem (Định lí về trực tâm của tam giác):
Let ABC be a triangle in the real plain. Show that the heights of the triangle corresponding to its vertices are concurrent
"""

from .additionalFolder.Geometry import Vector, Point, Line

def orthocenterTheoremCheck(A: Point, B: Point, C: Point) -> bool:
    if A == B or B == C or C == A:
        raise ValueError(f'Invalid triangle')

    BC = Line(vec=B.getVector(C), pt=B)
    CA = Line(vec=C.getVector(C), pt=C)
    AB = Line(vec=A.getVector(C), pt=A)
    if BC == CA or CA == AB or AB == BC:
        raise ValueError(f'Invalid triangle')

    ha = BC.getPerpendicular(A)
    hb = CA.getPerpendicular(B)
    hc = AB.getPerpendicular(C)

    H = ha.intersection(hb)
    if ha.intersection(hc) == H:
        return True
    return False

