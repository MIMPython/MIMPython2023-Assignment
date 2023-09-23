# Bài tập yêu cầu xây dựng class Line để biểu diễn các đường thẳng trong mặt phẳng Oxy.

#a) y = ax+b không phải là phương trình tổng quát cho một đường thẳng trong mặt phẳng, vì mỗi giá trị của x cho ta không quá 
# 1 giá trị của y. Như vậy, các đường thẳng dạng y = ax + b không biểu diễn được các đường thẳng song song với trục Oy, khi x là 
# cố định còn y có thể nhận bất kì giá trị thực nào.
# Một ví dụ của đường thẳng không biểu diễn được qua phương trình y = ax+b là Oy={(0, y) | y là số thực}

#b) Ở đây ta cần tìm điều kiện của (a, b, c) sao cho tập nghiệm của phương trình ax + by + c = 0 là một đường thẳng.
# Rõ ràng, nếu a=b=0 thì phương trình trên hoặc vô nghiệm (c khác 0), hoặc có tập nghiệm là toàn bộ mặt phẳng (c = 0).
# Trong các trường hợp còn lại (a hoặc b khác 0) tập nghiệm của phương trình là một đường thẳng song song với vectơ (a, b)
# "c" đóng vai trò xác định duy nhất đường thẳng đó. Kết luận: ax + by + c = 0 là phương trình tổng quát của đường thẳng trên mặt phẳng,
# với điều kiện a, b không đồng thời bằng 0.

#c) d)
# class Line:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
# Ý tưởng của việc khởi tạo class Line như trên có lẽ xuất phát từ phương trình tổng quát ax + by + c = 0. Cách làm này không sai, vì từ
# a, b, c ta có thể tương ứng với duy nhất một đường thẳng, tuy nhiên nhược điểm của nó là, chỉ nhìn vào a, b, c sẽ rất khó để hình dung
# về đường thẳng nó mô tả, từ việc nó đi qua những điểm nào, độ dốc ra sao,... (sau khi tính toán thì ta biết được nó đi qua các điểm
# dạng (x, -(by+c)/a) và độ dốc là -b/a, tuy nhiên theo em, đây vẫn là một cách làm thiếu tính trực quan).

# Ví lí do đó, em đề xuất xây dựng class Line như sau:
from module04_assignment02_student01_TranDacNhatAnh import Point
from module04_assignment02_student01_TranDacNhatAnh import Vector
from numpy import Infinity
def ratio(a, b):
    if b == 0:
        if a == 0:
            raise 'Invalid ratio'
        else:
            return Infinity
    else:
        return a / b
class Line:
    def __init__(self, a, b, x, y): # Định nghĩa đường thẳng bằng Vector chỉ phương và một điểm trong Oxy mà nó đi qua
        self.v = Vector(a, b)
        self.p = Point(x, y)
    # Việc tìm giao điểm của 2 đường thẳng vẫn luôn gắn liền với giải hệ phương trình (trong chương trình phổ thông, đó là việc giải hệ gồm
    # phương trình của 2 đường thẳng). Để thực hiện việc đó, em cần tạo ra một hàm giải 2 hệ pt tuyến tính.
    # Mỗi điểm trên đường thẳng có dạng Point(x, y) + Vector(a, b)*t, giải hệ sau:
    #   lineA.p + lineA.v*t1 = lineB.p + lineB.v*t2
    def intersection(self, lineB):
        if ratio((self.v).x, (self.v).y) == ratio((lineB.v).x, (lineB.v).y): # Hai đường thẳng có cùng "hệ số góc" thì song song với nhau
            raise('Paralel line, no intersection.')
        else: # Để lấy được giao điểm, ta chỉ cần tìm t1 hoặc t2 trong hệ phương trình trên
            vec = Point.getVector(self.p, lineB.p) 
            t = Vector.area(vec, lineB.v) / Vector.area(self.v, lineB.v)
            return Point.vectorAdd(self.p, Vector.vecMultiply(self.v, t))
print(Line.intersection(Line(1, 1, -1, 0), Line(-1, 1, 1, 0))) # Point(0.0, 1.0)
# Minh họa:      /\ (chân mỗi đoạn thẳng lần lượt là (-1, 0) và (1, 0), còn giao điểm là đầu 2 đoạn thẳng: (0, 1))

# Tính ra cách giải này hơi bị...ảo :v trước khi viết ra thử em có xây dựng một số hàm với mong muốn làm ngắn gọn hơn các bước tính toán
# Nhưng ngắn gọn được như bài 3 (và cả bài 4) có hơi vượt ngoài mong đợi