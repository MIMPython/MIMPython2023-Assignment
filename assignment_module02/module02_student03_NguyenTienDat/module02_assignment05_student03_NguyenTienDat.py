# Bài tập 5

# (a)
def test_a(A):
    A[2] = A[2]**2
    print(A) 


# (b) way 1
def test_b_1(A):
    A.pop(2)
    print(A)


# (b) way 2
def test_b_2(A):
    del A[2]
    print(A)


# (c)
def test_c(A):
    A.append(A[-1]**2)
    print(A)


# (d)
def test_d(A):
    print(len(A))


# (e)
def test_e(A):
    total = 0
    for i in range(len(A)):
        total += A[i]
    print(total)


# (f)
def test_f(A):
    total = 0
    for i in {1, 2, 3, 5}:
        total += A[i]
    print(total)


# (g) way 1
def test_g_1(A):
    new_array = []
    new_array.extend(A[::-1])
    print(new_array)


# (g) way 2
def test_g_2(A):
    new_array = []
    for i in range(len(A) - 1, -1, -1):
        new_array.append(A[i])
    print(new_array)


# (h)
def test_h(A):
    odd_arr = []
    even_arr  = []
    for i in range(0, len(A)):
        if A[i] % 2 == 0:
            even_arr.append(A[i])
        else:
            odd_arr.append(A[i])
    print(f'Odd of number is {odd_arr}')
    print(f'Even of number is {even_arr}')


# (i)
def test_i(A):
    A.sort(reverse=True)
    B = A.copy()
    print(B)


# (j)
def test_j(A):
    A.sort(reverse=True)
    B = A.copy()
    if len(A) == len(B):
        print('the length of the list does not change after sorting !')


# (k)
def test_k(A):
    A.sort(reverse=True)
    B = A.copy()
    C = A + B
    print(C)


if __name__ == "__main__":
    A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    print ("(a):")
    test_a(A)
    print('\n')
    print ("(b) way 1:")
    test_b_1(A)
    print('\n')
    print ("(b) way 2:")
    test_b_2(A)
    print('\n')
    print ("(c):")
    test_c(A)
    print('\n')
    print ("(d):")
    test_d(A)
    print('\n')
    print ("(e):")
    test_e(A)
    print('\n')
    print ("(f):")
    test_f(A)
    print('\n')
    print ("(g) way 1:")
    test_g_1(A)
    print('\n')
    print ("(g) way 2:")
    test_g_2(A)
    print('\n')
    print ("(h):")
    test_h(A)
    print('\n')
    print("(i)")
    test_i(A)
    print('\n')
    print ("(j)")
    test_j(A)
    print('\n')
    print ("(k)")
    test_k(A)
    print('\n')
