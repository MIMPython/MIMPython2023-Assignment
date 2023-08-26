A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

#a
A[2]=A[2]**2
print(A)

#b
A.pop[2]
print(A)

A.remove("7")
print(A)

#c
b=A[len(A)-1]
A.append(b**2)
print(A)

#d              
a=len(A)
print("Số phần tử trong list là:",a)

#e

for i in range(len(A)):
    tong = 0
    tong +=A[i]
print("Tổng các phần tử là:",tong)

#f
B1=[43,7,46,77]
sum1=0
for j in range(len(B1)):
    sum1+=B1[j]
print("Tổng là:",sum1)

#g
A.reverse
print(A)

C=[]
for k in range(1,len(A)+1):
    C[k]=A[-k]
print(C)

#h
list1=[]
list2=[]
for L in A:
    if L%2==0:
        list1.append(L)
    
    else:
        list2.append(L)
        
print(list1)
print(list2)

#i
B=[]
B.append(A.sort())
print(B)

#j
if len(A)== len(B):
    print("Số phần tử bằng nhau")
else:
    print("Số phần tử không bằng nhau")

#k
D=A+B
print(D)    





    





    
    
    