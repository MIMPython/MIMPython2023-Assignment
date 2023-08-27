A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

def a(A):
    B=A.copy()
    B[2] = B[2] * B[2]
    print(B)

def b1(A):
    B = A.copy()
    B.pop(2)
    print(B)

def b2(A):
    B = A.copy()
    del B[2]
    print(B)

def c(A):
    B = A.copy()
    B.append(B[-1] ** 2)
    print(B)

def d(A):
    print(len(A))

def e(A):
    sum=0
    for i in A:
        sum=sum+i
    print(sum)

def f(A):
   print( A[1]+A[2]+A[3]+A[5])

def g1(A):
    list=A.copy()
    list.reverse()
    print(list)

def g2(A):
    B=A.copy()
    for i in range(len(B)//2):
        temp=B[i]
        B[i]=B[len(B)-1-i]
        B[len(B)-1-i]=temp
    print(B)


def h(A):
    even=[]
    odd=[]
    for i in A:
        if i%2==0:
            even.append(i)
        elif i%2!=0:
            odd.append(i)
    print(even)
    print(odd)

def i(A):
    B=A.copy()
    B.sort(reverse=True)
    return B

B=i(A)
print(len(A)==len(B))

def k(A,B):
    C=A+B
    print(C)


a(A)

b1(A)

b2(A)

c(A)

d(A)

e(A)

(f(A))

g1(A)

g2(A)

h(A)

print(i(A))

k(A,B)





