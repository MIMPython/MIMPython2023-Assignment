'''
a) Đếm số chữ số 0 ở bên phải n!.
b) Xóa đi tất cả chữ số 0 tận cùng bên phải của n!
'''


def factorial_number(n):
    '''
    tính giai thừa của số n
    '''
    factorial = 1
    for i in range(2, n+1):
        factorial *= i
    return factorial


def count_trailing_zeros(n):
    count = 0
    for i in range(5, n+1, 5):
        while i % 5 == 0:
            count = count+1
            i /= 5
    return count


def remove_trailing_zeros(n):
    n = str(n)
    while n.endswith('0'):
        n = n[:-1]
    return int(n)


if __name__ == '__main__':
    n = int(input('Enter n:'))
    number = factorial_number(n)
    print(f'The factorial of {n} is: {number}')
    print(f'{n}! has {count_trailing_zeros(n)} zeros at the end')
    print(
        f'Delete zeros at the end of {n}!, result is {remove_trailing_zeros(number)}')
