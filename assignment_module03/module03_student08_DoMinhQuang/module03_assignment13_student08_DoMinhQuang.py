"Bài 13: tìm độ dài khi viết 2^n và 5^n cạnh nhau"
def count(n):
    a = str(pow(2,n)) #lấy ra độ dài chuỗi a
    b = str(pow(5,n)) #Lấy ra độ dài chuỗi b
    print(len(a) + len(b))

if __name__ == '__main__':
    count(3)#4 (8125)
    count(4)#5 (16625)
    count(5)#6 (323125)

#Chạy code: python module03_assignment13_student08_DoMinhQuang.py