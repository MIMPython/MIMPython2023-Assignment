#Bài tập 6:
import math
def tim_nghiem_thuc(a, b, c):
    if a == 0 and b == 0 and c == 0:
        print("Phương trình vô số nghiệm")
    elif a == 0 and b == 0:
        print(())
    elif a == 0:
        print((-c /b))
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print(())
        elif delta == 0:
            print((-b /2*a))
        elif delta > 0:
            x1 = (-b - math.sqrt(delta)) / (2*a)
            x2 = (-b + math.sqrt(delta)) / (2*a)
            print((x1, x2))

print(tim_nghiem_thuc(0, 0, 1))

#Câu hỏi nâng cao:
"""Điều kiện ba số a, b, c không đồng thời bằng 0 là để đảm bảo phương 
trình có dạng a*x**2+b*x+c=0. Nếu ba số này đều bằng 0, thì phương trình sẽ
trở thành 0=0, tức là vô số nghiệm. Nếu chỉ có a và b bằng 0, thì phương
trình sẽ trở thành c=0, tức là vô nghiệm hoặc vô số nghiệm tùy theo giá
trị của c. Nếu chỉ có a bằng 0, thì phương trình sẽ trở thành bx+c=0, tức 
là phương trình bậc nhất có một nghiệm duy nhất."""

def tim_nghiem_thuc(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print()
    elif delta == 0:
        if a == 0 and b == 0:
            print(()) 
        else:
            print((-b /2*a))
    else:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print((x1, x2))

print(tim_nghiem_thuc(0, 0, 1))


