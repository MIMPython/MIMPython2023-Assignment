def count_digits(page):
    digit_count = 0
    for i in range(1, page + 1):
        digit_count += len(str(i))
    return digit_count


def find_pages(num_digits):
    pages = 0
    total_digits = 0
    while total_digits < num_digits:
        pages += 1
        total_digits += len(str(pages))
    return pages

if __name__ == '__main__':
    print(count_digits(10)) 
    print(find_pages(11))
