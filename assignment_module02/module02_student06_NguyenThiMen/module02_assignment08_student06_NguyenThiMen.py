# half pyramid
def print_half_pyramid(rows):
    for i in range(rows + 1):
        for j in range(i):
            print('*', end ='')
        print()

# inverted half pyramid
def print_inverted_half_pyramid(rows):
    for i in range(0, rows + 1):
        print('*'*(rows - i))

# full pyramid
def print_full_pyramid(rows):
    for i in range(rows):
        for j in range(rows-i-1):
            print(" ", end = "")
        for k in range(i+1):
            print("*", end = " ")
        print()

# inverted full pyramid
def print_inverted_pyramid(rows):
    for i in range(rows):
        for j in range(i):
            print(" ", end="")
        for k in range(rows-i):
            print("*", end=" ")
        print()

if __name__ =='__main__':
    print_half_pyramid(6)
    print()
    print_inverted_half_pyramid(6)
    print()
    print_full_pyramid(6)
    print()
    print_inverted_pyramid(6)
    print()
