def swirl(num):
    """
    Đầu vào là một số nguyên dương. Đầu ra là các số từ 1 đến n
    được in theo hình xoáy. Phương pháp là mở rộng bảng thành bảng
    vuông rồi tạo bảng từ số lớn nhất về 1. Khi in thì chỉ in những số
    không quá đầu vào.
    """
    import math
    size = math.ceil(math.sqrt(num))
    table = [["" for i in range(size)] for j in range(size)]
    i = size
    count = size ** 2
    if i % 2 == 1:
        while i > 0:
            for j in range(int((i + 1) / 2)):
                table[size - j - 1][j] = count
                count -= 1
                for k in range(1, i):
                    table[size - j - 1 - k][j] = count
                    count -= 1
                for k in range(1, i):
                    table[size - j - i][j + k] = count
                    count -= 1
                for k in range(1, i):
                    table[size - j - i + k][j + i - 1] = count
                    count -= 1
                for k in range(1, i - 1):
                    table[size - j - 1][j + i - 1 - k] = count
                    count -= 1
                i -= 2
    else:
        while i > 0:
            for j in range(int(i / 2)):
                table[j][size - j - 1] = count
                count -= 1
                for k in range(1, i):
                    table[j + k][size - j - 1] = count
                    count -= 1
                for k in range(1, i):
                    table[j + i - 1][size - j - 1 - k] = count
                    count -= 1
                for k in range(1, i):
                    table[j + i - 1 - k][size - j - i] = count
                    count -= 1
                for k in range(1, i - 1):
                    table[j][size - j - i + k] = count
                    count -= 1
                i -= 2

    # In bảng đã tạo.
    index = len(str(num))
    for i in range(size):
        for j in range(size):
            if (table[i][j] <= num):
                print(str(table[i][j]).rjust(index, " "), end = " ")
            else:
                print(" " * index, end = " ")
        print()

swirl(100)