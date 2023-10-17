import cv2
img = cv2.imread("./additionalFolder/module06_assignment04_student04_TranNgocHieu_cake.png")

row = img.shape[0]
column = img.shape[1]

top_left = img[0:int(row/2), int(column/2) + 1:column]
bottom_left = img[0:int(row/2), 0:int(column/2)]
left_half = cv2.vconcat([top_left, bottom_left])

top_right = img[int(row/2) + 1:row, int(column/2) + 1:column]
bottom_right = img[int(row/2) + 1:row, 0:int(column/2)]
right_half = cv2.vconcat([top_right, bottom_right])

new_image = cv2.hconcat([left_half, right_half])
cv2.imwrite("./additionalFolder/module06_assignment04_student04_TranNgocHieu_new_image.png")