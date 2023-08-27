from math import sqrt
import matplotlib.pyplot as plt



def Cramer(a,b,c,d,e,f):
    detA=a*e-d*b
    detA1=c*e-f*b
    detA2=c*d-f*a
    x=detA1/detA
    y=detA2/detA    
    print(x,y)

def Solution(x1,y1,x2,y2):
    a=x2-x1
    b=y2-y1 # tim vecto phap tuyen cua pt trung truc AB
    d=sqrt(a*a+b*b) # tinh khoang cach giua AB
    x0=(x1+x2)*0.5
    y0=(y1+y2)*0.5 # tim toa do trung diem AB
    c=-a*x0-b*y0
    d1=0.5*sqrt(3)*d*sqrt(a*a+b*b)+b*x0-a*y0
    d2=-0.5*sqrt(3)*d*sqrt(a*a+b*b)+b*x0-a*y0 # muc dich di viet phuong trinh ax+by+d=0 cach phuong trinh AB 1 doan a/2*sqrt(3)
    Cramer(a,b,-c,-b,a,-d1)
    Cramer(a,b,-c,-b,a,-d2)

Solution(-4,0,4,0)
x=[-4,0,4]
y=[0,6.928203230275509,0]
x2=[-4,4]
y2=[0,0]
plt.plot(x2,y2)
plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Title')

plt.show()


    

