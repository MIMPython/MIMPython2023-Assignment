#a: Viết một chương trình chạy vô hạn sử dụng vòng lặp while.
while 1:
    0

#b: Viết một chương trình chạy vô hạn sử dụng vòng lặp for và không dùng vòng lặp while.  
list = ['Doraemon']
for i in list:
    print(i)
    list.append("Nobita")

#c: Viết một chương trình chạy vô hạn sử dụng vòng lặp for mà đối tượng được duyệt (sau từ khóa in) không phải là một list, tuple, set, hay dictionary
def main():
    while 1:
        yield "MIM"

def another_main():
    for i in main():
        print(i)

another_main()