import math
from PIL import Image, ImageDraw


class EquilateralTriangle:
    def __init__(self, A: tuple, B: tuple) -> None:
        self.A = A
        self.B = B
        self.C = []

    def solve(self) -> None:
        if self.A == self.B:
            raise Exception("No solution!")
        else:
            c = math.sqrt(3)
            m = self.B[0] - self.A[0]
            n = self.B[1] - self.A[1]
            u1 = (m + n * c) / 2.0
            v1 = (n - m * c) / 2.0
            u2 = (m - n * c) / 2.0
            v2 = (n + m * c) / 2.0
            x1 = u1 + self.A[0]
            y1 = v1 + self.A[1]
            x2 = u2 + self.A[0]
            y2 = v2 + self.A[1]

            self.C = [(x1, y1), (x2, y2)]

    def visualize(self):
        path = "./week02/additionFolder/module02_assignment10_student05_NguyenQuocHieu_image"
        for i, C in enumerate(self.C):
            image = Image.new(mode="RGB", size=(
                100, 100), color=(255, 255, 255))
            drawer = ImageDraw.Draw(im=image)
            drawer.line([self.A, self.B], fill=(255, 0, 0))
            drawer.line([self.A, C], fill=(255, 0, 0))
            drawer.line([self.B, C], fill=(255, 0, 0))
            image.save(path + str(i) + ".png")


if __name__ == "__main__":
    A = (10, 20)
    B = (30, 40)

    triangle = EquilateralTriangle(A=A, B=B)
    triangle.solve()
    triangle.visualize()
