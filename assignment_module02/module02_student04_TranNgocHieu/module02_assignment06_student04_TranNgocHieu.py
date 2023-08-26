import math
a, b, c = input("Nhập 3 số thực không đồng thời bằng 0: ").split()

def eqn_solver(a, b, c):
    """
    Đầu vào là các hệ số của phương trình ax^2 + bx + c = 0.
    Đầu ra là tập nghiệm của phương trình dưới dạng tuple.
    """
    a = float(a)
    b = float(b)
    c = float(c)
    if a == 0:
        if b == 0 and c != 0: return ()
        elif b != 0: return (round(-c/b, 2), )
    else:
        delta = b*b - 4*a*c
        if delta < 0: return ()
        elif delta == 0: return (round(-b/(2*a), 2), )
        else: 
            root_1 = round((-b - math.sqrt(delta))/(2*a), 2)
            root_2 = round((-b + math.sqrt(delta))/(2*a), 2)
            return (root_1, root_2)

print(eqn_solver(1, 1, -2))    # (-2.0, 1.0)
print(eqn_solver(1, 2, 1))    # (-1.0,)
print(eqn_solver(1, 0, 1))    # ()
print(eqn_solver(a, b, c))

"""
Trả lời câu hỏi:
Khi a = b = c = 0, phương trình cần giải nhận mọi số thực làm nghiệm, 
do đó không thể in ra một tuple là tập nghiệm của bài toán. Ta có thể 
xét thêm trường hợp này trong hàm và trả về một tuple rỗng chẳng hạn.
"""