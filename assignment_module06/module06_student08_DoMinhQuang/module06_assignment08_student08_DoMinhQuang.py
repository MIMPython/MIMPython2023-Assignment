'''Bài 8: mô phỏng Conway’s game of life'''


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Tạo ma trận ngẫu nhiên gồm các số 0 và 1 với kích thước 10 x 10
matrix = np.random.randint(2, size = (50, 50))

# fig, ax = plt.subplots()

im = plt.imshow(matrix)

# Hàm khởi tạo
def init():
    im.set_data(matrix)
    return im

def rule(matrix):#hàm này vẫn chưa hoàn chỉnh do em chưa xét các phần tử ở rìa ma trận
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            alive = np.sum(matrix[row - 1:row + 2, col - 1:col + 2]) - matrix[row, col]
            #tính tổng các giá trị của hàng xóm xung quanh và trừ đi giá trị của matrix[row, col] do đang xét trên các ô vuông 3 x 3 bao gồm cả matrix[row, col]

            if matrix[row, col] == 1:
                if alive < 2 or alive > 3:
                    matrix[row, col] = 0
                elif 2 <= alive <= 3:
                    matrix[row, col] = 1

            else:
                if alive == 3:
                    matrix[row, col] = 1
    return matrix

# Hàm cập nhật
def animate(i): #nếu tham số của hàm trống thì chương trình sẽ đứng yên nên em để 1 tham số tùy ý ở đây
    new_matrix = rule(matrix)

    # Cập nhật đối tượng imshow với ma trận mới
    im.set_data(new_matrix)#Hàm im.set_data(new_matrix) có tác dụng cập nhật đối tượng imshow với ma trận mới. Nó sẽ hiển thị ma trận mới lên màn hình. Hàm này được sử dụng trong các ứng dụng liên quan đến xử lý hình ảnh và video.
    return im

    # plt.imshow(new_matrix) #nếu dùng doòng code này thay cho 2 dòng trên thì chương trình vẫn chạy nhưng càng ngày càng chậm

# Tạo animation
ani = animation.FuncAnimation(plt.gcf(), animate ,init_func = init, interval = 50)

#khi tạo subplot thì ta thay plt.gcf() = fig, lí do vì sao thì em chưa biết

# Hiển thị animation
plt.show()
# print(matrix)
#
# print(rule(matrix))