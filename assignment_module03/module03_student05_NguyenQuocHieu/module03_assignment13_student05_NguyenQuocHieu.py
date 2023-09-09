import math


def countDigitsBase2(n: int) -> int:
    c = math.log(10) / math.log(2)
    return int(n / c) + 1


def countDigitsBase5(n: int) -> int:
    c = math.log(10) / math.log(5)
    return int(n / c) + 1


def main():
    n = int(input("Input a number: "))
    print(countDigitsBase2(n) + countDigitsBase5(n))


if __name__ == "__main__":
    main()

# Mô tả: Đếm số chữ số khi viết 2 số 2^n và 5^n cạnh nhau
# Chạy code: python module03_assignment13_student05_NguyenQuocHieu.py
# Output: 4 (với n = 3)
