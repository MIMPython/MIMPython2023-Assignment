import cv2
import numpy
image = cv2.imread(
    r"module06_student05_NguyenQuocHieu\additionFolder\module06_assignment04_student05_NguyenQuocHieu_SD_mooncake.png")
height, width, channel = image.shape
if width % 2 == 1:
    width -= 1
if height % 2 == 1:
    height -= 1
midWidth = width // 2
midHeight = height // 2
topLeft = image[0: midHeight, 0: midWidth]
topRight = image[0: midHeight, midWidth: width]
bottomLeft = image[midHeight: height, 0: midWidth]
bottomRight = image[midHeight: height, midWidth: width]

firstPart = numpy.concatenate((topRight, bottomRight), axis=1)
secondPart = numpy.concatenate((topLeft, bottomLeft), axis=1)
result = numpy.concatenate((firstPart, secondPart), axis=0)
cv2.imwrite(
    "./module06_student05_NguyenQuocHieu/additionFolder/module06_assignment04_student05_NguyenQuocHieu_output.png", result)
cv2.imshow("Output", result)
cv2.waitKey(0)
