path = 'C:\python\\names.txt'
with open(path, 'r') as f:
    Names = f.read().split('","')
#Sắp xếp lại theo alphabet
Names.sort()

#Hàm tính tổng vị trí theo alphabet
def valueOFchar(name):
    sum_char = 0
    for i in name:
        i1 = ord(i) - 64
        sum_char += i1
    return sum_char


def sumAll(allname):
    sumOFall=0
    for j in range(len(allname)):
        position = j + 1
        value = position * valueOFchar(Names[j])
        sumOFall += value
    return sumOFall

print(sumAll(Names)) #871205488

