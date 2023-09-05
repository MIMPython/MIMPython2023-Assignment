import itertools

#a
def GCD(a,b):
    if a == 0 or b == 0:
        return 0
    else:
        while a != b:
            if(a>b):
                a = a - b
            else:
                b = b - a
    return a

print(GCD(3,3))#3
print(GCD(16,4))#4



#b
n=4
numberList = list(range(1,n+1))
total = 0.5*n*(n-1)
cList = itertools.combinations(numberList,2)
count = 0
for i,d in cList:
    if GCD(i,d) == 1:
        count+= 1
print(count)
print(count/total)



