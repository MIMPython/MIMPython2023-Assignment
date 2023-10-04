
def is_palindrome_number(number):
    if number < 0:
        return False
    origin_number = number
    reverse_number = 0
    while number > 0:
        digit = number % 10
        reverse_number = reverse_number*10 + digit
        number //= 10
    return reverse_number == origin_number


def find_palindrome_square_number():
    n = 1
    list = []
    while True:
        square_number = n*n
        if is_palindrome_number(square_number):
            print(square_number)
            list.append(square_number)
        n += 1


# tồn tại vô hạn số đồng thời là số chính phương và số đảo ngược
find_palindrome_square_number()
