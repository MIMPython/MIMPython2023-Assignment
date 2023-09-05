
def count(n):
    a=str(pow(2,n))
    b=str(pow(5,n))
    print(len(a)+len(b))

if __name__ == '__main__':
    count(3)#4 (8125)
    count(4)#5 (16625)
    count(5)#6 (323125)