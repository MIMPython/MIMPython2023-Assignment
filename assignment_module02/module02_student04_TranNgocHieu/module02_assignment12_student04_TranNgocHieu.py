foo = ('a'),
bar = 'a',
ham = ('a', )

print(f'{foo} {type(foo)}\n{bar} {type(bar)}\n{ham} {type(ham)}')
"""
Output:
('a',) <class 'tuple'>
('a',) <class 'tuple'>
('a',) <class 'tuple'>

Bài học: 
1. ('a') và 'a' là một, đều chỉ string 'a'.
2. Nếu khai báo giá trị của biến kèm theo dấu phẩy, python sẽ hiểu đó là
một tuple. 
3. Cũng liên quan đến dấu phẩy trong khai báo, nếu đó là dấu phẩy sau
tên biến, biến đó sẽ được hiểu là phần tử của tuple chứa một phần tử.
>>> foo, = 'a',
>>> print(f'{foo} {type(foo)}')
a <class 'str'>

Xem thêm về khai báo nhiều biến trên một dòng:
https://stackoverflow.com/questions/6967632/unpacking-extended-unpacking-and-nested-extended-unpacking
"""

#-----------------------------------------------------------------------

var1 = 'Đà Nẵng'
var2 = "Đà Nẵng"
var3 = ("Đà Nẵng")

print(f'{var1} {type(var1)}\n{var2} {type(var2)}\n{var3} {type(var3)}')
"""
Output:
Đà Nẵng <class 'str'>
Đà Nẵng <class 'str'>
Đà Nẵng <class 'str'>

Bài học: Dữ liệu đặt trong dấu nháy kép "" hay nháy đơn '' đều được
hiểu là kiểu string, do đó trong thực hành nên thống nhất một loại, để
phục vụ cho các công việc nhóm sau này.
Tuy nhiên, trong một số trường hợp đặc biệt như sau, ta chỉ dùng được
một trong hai:
>>> print("I'm hungry")
I'm hungry
>>> print('Sure, you are so "clever"...')
Sure, you are so "clever"...
Nếu muốn in ra một câu có cả hai dấu này, ta có thể dùng dấu gạch chéo
(\). Khi đó, python sẽ hiểu đây là một phần của câu:
>>> print('He said "I\'m hungry"')
He said "I'm hungry"

Nguồn: https://www.reddit.com/r/learnpython/comments/5w55jz/should_i_use_or_in_python/?rdt=60725
"""

"""
Bổ sung:
Về nguyên bản bài tập, hai string cùng có bề ngoài là 'Đà Nẵng' nhưng lại khác nhau.
----------------------
# ă --- u0103
# ~ --- u0303
# ẵ --- u1eb5

print(u"\u0103" + u"\u0303")    # ẵ
print(u"\u1eb5")    # ẵ

print(len("ẵ"))    # 2
print(len("ẵ"))    # 1
----------------------
Ký tự 'ẵ' trong biến thứ nhất là ghép của hai ký tự 'ă' và '~', trong khi ký tự sau là 'ẵ' luôn.
"""
