#Bài 2: tìm 10 chữ số đầu trong tổng của 100 số 50 chữ số
import sys

filename = sys.argv[1]
f = open(filename, 'r')
allLines = f.read().splitlines()
f.close()

s=0
for i in allLines:
    s=s+int(i)
str=str(s)
print(str[0:10])#5537376230

#File input: module03_assignment02_student08_DoMinhQuang_data.txt
#Chạy code :python module03_assignment02_student08_DoMinhQuang.py additionalFolder/module03_assignment02_student08_DoMinhQuang_data.txt
