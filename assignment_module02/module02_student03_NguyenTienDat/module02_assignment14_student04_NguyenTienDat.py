# Bài tập 14


# 1.
def main(page_count):
    digits_used = 0
    for page_number in range(1, page_count + 1):
        digits_used += len(str(page_number))
    return digits_used

print(main(10)) # output: 11


# 2.
def main1(digits_used):
    page_number = 1
    while digits_used > 0:
        digits_used -= len(str(page_number))
        page_number += 1
    return page_number - 1

print(main1(192)) # output: 100