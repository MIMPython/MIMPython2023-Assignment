import math

def score(tx,gk,ck):
    total = 0.2*tx+0.2*gk+0.6*ck
    if total>=9:
        print("A+")
    elif total>=8.5:
        if 9-total<=0.05:
            print("A+")
        else:
            print("A")
    elif total>=8:
        if 8.5-total<=0.05:
            print("A")
        else:
            print("B+")
    elif total>=7:
        if 8-total<=0.05:
            print("B+")
        else:
            print("B")
    elif total>=6.5:
        if 7-total<=0.05:
            print("B")
        else:
            print("C+")
    elif total>=5.5:
        if 6.5-total<=0.05:
            print("C+")
        else:
            print("C")
    elif total>=5:
        if 5.5-total<=0.05:
            print("C")
        else:
            print("D+")
    elif total>=4:
        if 5-total<=0.05:
            print("D+")
        else:
            print("D")
    else:
        print("F")

score(9,9,8) #B+
score(4,4,9) #B
score(10,8.5,4.8)#C+

