def fibonacci(n: int) -> int:
    data = [0, 1]
    for index in range(2, n + 1):
        data.append(data[index - 1] + data[index - 2])
    return data[n]


if __name__ == "__main__":
    print(fibonacci(10000))

# Tính số Fibonacci
# Chạy code: python module03_assignment04_student05_NguyenQuocHieu.py
# Output: 354224848179261915075 (số Fibonacci thứ 100)
