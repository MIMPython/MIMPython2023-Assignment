# Bài tập 8

# (1) Half Pyramid
def half_pyramid(n):
    for i in range(n):
        print("*" * (i + 1))

# (2) Inverted Half Pyramid
def inverted_half_pyramid(n):
    for i in range(n):
        print("*" * (n - i))

# (3) Hollow Inverted Half Pyramid
def hollow_inverted_half_pyramid(n):
    print ("*" * n)
    for i in range(n - 2):
        print("*" + " " * (n - 3 - i) + "*")
    print ("*")

# (4) Full Pyramid
def full_pyramid(n):
    for i in range(n):
        print(" " * (n - 1 - i) + "*" + i * " *")

# (5) Inverted Full Pyramid 
def inverted_full_pyramid(n):
    i = n - 1
    while i >= 0:
        print(" " * (n - 1 - i) + "*" + i * " *")
        i -= 1

# (6) Hollow Full Pyramid
def hollow_full_pyramid(n):
    print (" " * (n - 1) + "*")
    for i in range(1, n - 1):
        print (" " * (n - 1 - i) + "*" + " " * 2 * (i - 1) + " *")
    print ("* " * n)


half_pyramid(6)
print('\n')
inverted_half_pyramid(6)
print('\n')
hollow_inverted_half_pyramid(6)
print('\n')
full_pyramid(6)
print('\n')
inverted_full_pyramid(6)
print('\n')
hollow_full_pyramid(6)
            