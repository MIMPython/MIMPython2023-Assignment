#a
for i in range(6):
    for j in range(i+1):
        print("*", end="")
    print()


#b
for i in range(6):
    for j in range(6-i):
        print("*", end="")
    print()


#c
for i in range(6):
    for j in range(6-i):
        if i == 0 or i == 6-1 or j == 0 or j == 6-i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#d
n = 6
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print("* ", end="")
    print()


#e
for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print("* ", end="")
    print()
#f

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        if i == 0 or i == n-1 or j == 0 or j == i:
            print("* ", end="")
        else:
            print("  ", end="")
    print()