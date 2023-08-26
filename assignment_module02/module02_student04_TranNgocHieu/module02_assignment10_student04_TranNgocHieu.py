"""
Để tiện cho việc vẽ hình, toạ độ các đỉnh nên nằm trong khoảng (-8, 8).
"""
import numpy
from math import sqrt
from matplotlib import pyplot

def equilateral_triangle_completion(list):
    """
    Đầu vào là một list có 4 phần tử DẠNG FLOAT, chứa toạ độ của hai 
    điểm cho trước theo thứ tự 
    [Hoành độ 1, Tung độ 1, Hoành độ 2, Tung độ 2]. 
    Đầu ra là toạ độ của điểm thứ ba lập với hai điểm còn lại một tam 
    giác đều. 
    Có hai trường hợp:
    - Trường hợp 1: Không tồn tại điểm cần tìm. Trả về list 0.
    - Trường hợp 2: Tồn tại điểm cần tìm. Khi đó, luôn có hai điểm 
    thoả mãn. Đầu ra là một list gồm 2 tuple, mỗi tuple xác định một
    điểm thoả mãn yêu cầu.
    """
    if list[0] == list[2] and list[1] == list[3]:
        return [0]
    else: 
        length_AB = sqrt((list[0] - list[2]) ** 2 
                         + (list[1] - list[3]) ** 2)
        if list[1] == list[3]:
            x_c = (list[0] + list[2])/2
            y1 = list[1] + length_AB * sqrt(3) / 2
            y2 = list[1] - length_AB * sqrt(3) / 2
            return [(round(x_c, 3), round(y1, 3)), 
                    (round(x_c, 3), round(y2, 3))]
        else:
            const = ((length_AB * sqrt(3)) 
                      / (2 * sqrt(1 + ((list[0] - list[2]) 
                                        / (list[1] - list[3])) ** 2)))
            x1 = (list[0] + list[2]) / 2 + const
            x2 = (list[0] + list[2]) / 2 - const
            y1 = ((x1 - (list[0] + list[2]) / 2) 
                  * ((list[2] - list[0]) / (list[1] - list[3]))
                  + (list[1] + list[3]) / 2)
            y2 = ((x2 - (list[0] + list[2]) / 2) 
                  * ((list[2] - list[0]) / (list[1] - list[3]))
                  + (list[1] + list[3]) / 2)
            return [(round(x1, 3), round(y1, 3)),
                    (round(x2, 3), round(y2, 3))]
    
print("Nhập toạ độ của điểm A.\n"
      "Cú pháp: [Hoành độ (số thực)] [Tung độ (số thực)]\n"
      "Ví dụ: 1 2 -- Hoành độ là 1, Tung độ là 2")
A1, A2 = input().split()

print("Nhập toạ độ của điểm B:")
B1, B2 = input().split()

str_coord_list = [A1, A2, B1, B2]
fl_coord_list = [round(float(i), 3) for i in str_coord_list]
C_coords = equilateral_triangle_completion(fl_coord_list)

if C_coords == [0]: 
    print("Hai điểm đã chọn trùng nhau. "
          "Không tồn tại điểm thứ ba thoả mãn.")
    
# Vẽ đồ thị:
else:
    # Danh sách các hoành độ. Sự lặp lại phục vụ cho việc nối các điểm
    # với nhau.
    x = [
        fl_coord_list[0], fl_coord_list[2], 
        C_coords[0][0], fl_coord_list[0],
        C_coords[1][0], fl_coord_list[2]
    ]
    
    # Danh sách các tung độ
    y = [
        fl_coord_list[1], fl_coord_list[3],
        C_coords[0][1], fl_coord_list[1],
        C_coords[1][1], fl_coord_list[3]
    ]

    # Chưa biết để làm gì, nhưng cần thiết !
    fig, ax = pyplot.subplots()

    # Vẽ biểu đồ đường với các điểm đã cho, '-o' để hiện dấu chấm cho các điểm.
    ax.plot(x, y, '-o') 

    # Giới hạn hai trục tung, hoành, độ chia trên các trục.
    # Set identical scales for both axes
    ax.set(xlim=(-10, 10), ylim=(-10, 10), aspect = 'equal')

    # Set bottom and left spines as x and y axes of coordinate system.
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    # Remove top and right spines.
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Create 'x' and 'y' labels placed at the end of the axes
    ax.set_xlabel('x', size=10, labelpad=-8, x=1)
    ax.set_ylabel('y', size=10, labelpad=-5, y=0.98, rotation=0)

    # Remove (0, 0) tick labels, and ticks customization
    x_ticks = numpy.arange(-10, 10, 1)
    y_ticks = numpy.arange(-10, 10, 1)
    x_ticks = x_ticks[x_ticks != 0]
    y_ticks = y_ticks[y_ticks != 0]
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)
    ax.set_xticklabels(x_ticks, fontsize = 5)
    ax.set_yticklabels(y_ticks, fontsize = 5)

    # make arrows
    ax.plot((1), (0), ls="", marker=">", color="k",
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot((0), (1), ls="", marker="^", color="k",
            transform=ax.get_xaxis_transform(), clip_on=False)
    
    # annotate
    ax.annotate('A', xy = (fl_coord_list[0], fl_coord_list[1]))
    ax.annotate('B', xy = (fl_coord_list[2], fl_coord_list[3]))
    ax.annotate('C1', xy = (C_coords[0][0], C_coords[0][1]))
    ax.annotate('C2', xy = (C_coords[1][0], C_coords[1][1]))
    pyplot.show()
