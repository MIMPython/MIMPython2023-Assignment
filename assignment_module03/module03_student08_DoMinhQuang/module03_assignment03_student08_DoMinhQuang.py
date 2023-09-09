'''Bài 3:Tính tổng điểm của các tên trong danh sách theo quy tắc sau:
    Ứng với mỗi chữ cái của tên, tìm số thứ tự của mỗi chữ cái rồi tính tổng
    Nhân tổng đó với vị trí của tên trong danh sách, ta được điểm tương ứng
    Tính tổng điểm của tất cả ten trong danh sách'''

import sys

filename = sys.argv[1]
f = open(filename, 'r')
names = f.read().split(",")
f.close()
names.sort()


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def findScore(str):
    s = 0
    for letter in str:
        index = int(alphabet.find(letter) + 1)#Tiìm vị trí của chữ cái
        s += index
    return s

def findPosition(str):#Hàm tìm vị trí của tên trong danh sách
    for i in range(len(names)):
        if names[i] == str:
            return i + 1


if __name__ == '__main__':
    result = 0
    for i in range(len(names)):
        result += findScore(names[i]) * findPosition(names[i])

    print(result)#871198282


#File input: module03_assignment03_student08_DoMinhQuang_data.txt"
#Chạy code :python module03_assignment03_student08_DoMinhQuang.py additionalFolder/module03_assignment03_student08_DoMinhQuang_data.txt
