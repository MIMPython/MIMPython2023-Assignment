import cv2
import numpy
import skimage
import matplotlib.pyplot as plt
obj_image = cv2.imread(
    r"module06_student05_NguyenQuocHieu\additionFolder\module06_assignment11_student05_NguyenQuocHieu_object.jpg")
background = cv2.imread(
    r"module06_student05_NguyenQuocHieu\additionFolder\module06_assignment11_student05_NguyenQuocHieu_background.jpg")


def preprocess(obj_image: numpy.ndarray, background: numpy.ndarray) -> tuple:
    lab = cv2.cvtColor(obj_image, cv2.COLOR_BGR2LAB)
    A = lab[:, :, 1]
    ret, thresh = cv2.threshold(A, 100, 255, cv2.THRESH_BINARY)

    lower_h = -1
    upper_h = -1
    lower_w = -1
    upper_w = -1
    height, width = thresh.shape
    H, W, C = background.shape
    for h in range(height):
        if numpy.sum(thresh[h]) >= 255:
            lower_h = h
            break
    for h in range(height):
        if numpy.sum(thresh[height - 1 - h]) >= 255:
            upper_h = height - 1 - h
            break
    for w in range(width):
        if numpy.sum(thresh[:, w]) >= 255:
            lower_w = w
            break
    for w in range(width):
        if numpy.sum(thresh[:, width - 1 - w]) >= 255:
            upper_w = width - 1 - w
            break
    obj_region = thresh[lower_h: upper_h + 1, lower_w: upper_w + 1]
    obj = obj_image[lower_h: upper_h + 1, lower_w: upper_w + 1]
    new_h = upper_h - lower_h
    new_w = upper_w - lower_w
    assert new_w < W, "Out of range"
    if new_h > H:
        ratio = 2
        obj_region = cv2.resize(
            obj_region,
            (int((upper_w - lower_w) * H / ratio / (upper_h - lower_h)), int(H / ratio)))
        obj = cv2.resize(
            obj,
            (int((upper_w - lower_w) * H / ratio / (upper_h - lower_h)), int(H / ratio)))
    points = []
    h1, w1 = obj_region.shape
    for h in range(h1):
        for w in range(w1):
            if obj_region[h][w] == 255:
                points.append((h, w, obj[h][w]))
    return points


def insertAt(x: int, y: int, points: tuple, background: numpy.ndarray) -> numpy.ndarray:
    for point in points:
        h, w, value = point
        assert y + h < background.shape[0], "Out of range"
        background[y + h][x + w] = value
    return background


if __name__ == "__main__":
    points = preprocess(obj_image=obj_image, background=background)
    image = insertAt(x=200, y=150, points=points, background=background.copy())
    cv2.imshow("Output", image)
    cv2.waitKey(0)
