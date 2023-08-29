A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
print(A)
#a
A[2] = A[2]*A[2]
print(A)
#b
A.pop(2)
print(A)
##A.remove(A[2])
#c
A.append(A[len(A)-1]**2)
print(A)
#d
numberOfElements = len(A)
print(numberOfElements)
#e
sumOfElements = 0
for element in A:
    sumOfElements += element
print(sumOfElements)
#f
s = A[1]+A[2]+A[3]+A[5]
print(s)
#g
#Cách khác: X = A.reverse()
X = []
for i in range(len(A)):
    X.append(A[len(A)-i-1])
print(X)
#h
Y = []
Z = []
for element in A:
    if element%2 ==0:
        Y.append(element)
    else:
        Z.append(element)
print(Y, Z)
#i
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
B = []
for element in A:
    if len(B)==0:
        B.append(element)
    else:
        for i in range(len(B)):
            if element<B[i]:
                if i==len(B)-1:
                    B.append(element)
                else:
                    continue
            else:
                B.insert(i,element)
                break
print(B)
#j
print(len(A)==len(B)) #True
#k
C = A + B
print(C)