import numpy as np

#Kiểm tra UCLN
def euclid_func(a,b):    
    if b == 0:
        return a
    else:
        return euclid_func(b,a%b)


def findP():
    count = 0
    for i in range(10**6):
        random_2number = np.random.randint(10**6,size=2) #Lấy ngẫu nhiên 2 số
        if euclid_func(random_2number[0],random_2number[1]) == 1:
            count += 1
    P = count / 10**6
    print(P)    
findP()
#P xấp xỉ 0,6
