foo = ('a') 
bar = 'a'
ham = ('a',)
if foo == bar:
    print("Hai chuoi bang nhau")
else:
    print("Hai chuoi khong bang nhau")

foo1 = 'Đà Nẵng'
bar1 = 'Đà Nẵng'
if foo1 == bar1:
    print("Hai chuoi bang nhau")
else:
    print("Hai chuoi khong bang nhau")
'''
Bài học rút ra, khi tạo một tuple nhưng chỉ có 1 phần tử, ta phải thêm dấu
phẩy đằng sau để chắc chắn nó là 1 tuple; khi so sánh chuỗi mà với ngôn ngữ
sử dụng Unicode như Tiếng Việt, ta nên chú ý so sánh các ký tự Unicode, kiểm
tra dấu chữ viết hoa, viết thường
'''