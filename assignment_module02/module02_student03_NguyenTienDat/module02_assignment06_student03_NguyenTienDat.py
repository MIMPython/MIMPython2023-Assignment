# Bài tập 6

def solve_equation(a, b, c):
    # solve equation: a*x^2 + b*x + c = 0.
    if a != 0:
        delta = b**2 - 4*a*c
        if delta > 0:
            # solution 1
            x1 = (-b + delta**0.5)/(2*a)
            # solution 2
            x2 = (-b - delta**0.5)/(2*a)
            print((min(x1, x2), max(x1, x2)))
        elif delta == 0:
            x1 = x2 = -b/(2*a)
            print((x1, ))
        else:
            print (())
    else:
        x1 = -c/b
        print((x1, ))


if __name__ == "__main__":
    solve_equation(1, 1, -2)
    solve_equation(1, 2, 1)

# giải phương trình này chúng ta cần chia ra 2 trường hợp là a = 0 và a != 0
# vì với mỗi trường hợp ta sẽ có cách giải khác nhau, với a = 0 ta sẽ giải
# phương trình bậc nhất 1 ẩn số, còn a != 0 ta sẽ tiến hành giải phương trình
# bậc hai 1 ẩn số.

# nếu a, b, c đều đồng thời bằng 0 thì hiển nhiên phương trình là đúng, không
# cần giải nữa. Việc viết lại một chương trình tương tự để giải phương trình
# nhưng không chia trường hợp là điều không thể vì khi tính nghiệm ta đòi hỏi
# a phải khác 0 và delta phải dương.