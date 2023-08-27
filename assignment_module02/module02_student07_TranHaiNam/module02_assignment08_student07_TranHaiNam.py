#1
for i in range(6):
    for j in range(i+1):
        print(" * ", end= "")
    print("\n")


#2
for i1 in range(6,0,-1):
    for j1 in range(0,i1):
        print(" * ", end= "")
    print("\n")


#3
for j2 in range(6,0,-1):
    if j2 == 6:
        print( 6 * "*")
    elif 1< j2 <6:
         print('*' + (j2-2)* ' ' + '*' )
    else:
        print("*")
    
#4
for i in range(6):
    for j in range(6-i-1):
        print(" ", end="")
    for j in range(i+1):
        print(" * ",end="")
    print("\n")

#5
for i in range(6,0,-1):     

    for j in range(6-i,0,-1):
        print(" ",end="")
    for j in range(i,0,-1):
        print(" * ",end="")
    print("\n")

#6
for i in range(1,7):
    space0=(6-i)* "  "
    space1=" * "+ (i-2)*"   " + " * "
    if i == 6:
        print(6* " * ")
    elif 1<i<6:
        print( space0 + space1)
    else:
        print( space0 + " * ")
    print()





