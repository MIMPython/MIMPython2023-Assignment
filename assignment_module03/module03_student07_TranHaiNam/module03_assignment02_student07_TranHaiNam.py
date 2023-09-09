path = 'C:\python\\numbers.txt'
with open (path, 'r') as file:  
    allnumber = file.read().splitlines()

allnumber = [int(i) for i in allnumber]
sum1 = str(sum(allnumber))
sum2 = sum1[0:10]

list = []
for i in sum2:
    list.append(int(i))
print(list) #5, 5, 3, 7, 3, 7, 6, 2, 3, 0


    




