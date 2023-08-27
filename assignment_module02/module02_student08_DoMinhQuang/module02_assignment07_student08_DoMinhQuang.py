


alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
def Caesar(str):
    list=[]
    for letter in str:
        list.append(letter)
    for i in range(len(str)):
        index=int(alphabet.find(list[i]))

        list[i]=alphabet[index+13]
    for i in range(len(list)):
        print(list[i],end='')

Caesar("PYTHON")#CLGUBA
print()
Caesar("MIMGO")#ZVZTB
print()
Caesar("MODELING")#ZBQRYVAT





        

