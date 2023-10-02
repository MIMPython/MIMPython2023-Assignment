'''Bài 5: Viết hàm tạo vòng lặp vô hạn có sử dụng while, không sử dụng while, và đối tượng lặp không phải là kiểu
          list, tuple, dicionary hay set'''

import itertools

#a)
def infinite_loop1():
    while 1: #1 sẽ ứng với True, 0 ứng với False, nên điều kiện luôn đúng
        print('This is an infinite loop')

#b)
def infinite_loop2(): #Gọi đệ quy
    for i in range(2):
        print('This is an infinite loop')
    infinite_loop2()


def infinite_loop3():
    # Tạo một đối tượng lặp lại vô hạn
    infinite = iter(lambda: True, False)

    # Sử dụng vòng lặp for để duyệt qua đối tượng này
    for i in infinite:
        print("This is an infinite loop")

def infinite_loop4():
    for i in itertools.count(): #Do tò mò nên em thử dùng itertools.count() mà không truyền tham số để xem nó đếm cái gì, và kết quả
        print('This is an infinite loop')              #là một vòng lặp vô hạn

#c)
# def infinite_generator(): #Trong khi tìm hiểu các hàm có thể sinh ra vô hạn phần tử, em đã biết đến một khái
#     while True:           #niệm là generator, do em chưa hiểu rõ về nó nên em sẽ comment lại ý c) ở đây
#         yield 1
#
# for x in infinite_generator():
#     print(x)

if __name__ == '__main__':
    infinite_loop1()
    # infinite_loop2()
    # infinite_loop3()
    # infinite_loop4()

#chạy code: python module05_assignment05_student08_DoMinhQuang.py
