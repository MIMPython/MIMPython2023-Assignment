'''Bài 10:Thiết kế vòng lặp do while trong Python'''


'''a) Vòng lặp do-while trong C++ khác vòng lặp while trong Python ở chỗ nó chạỵ các lệnh
trong khối do trước rồi mới kiểm tra điều kiện lặp, còn vòng lặp while trong Python sẽ kiểm tra
điều kiện rồi mới thực hiện câu lệnh trong khối while'''

'''b) Biến đổi tương đương vòng lặp do while trong C++ sang đoạn code sử dụng while trong Python bằng
cách:
    -Khởi tạo 1 vòng lặp vô hạn While True chứa 1 khối lệnh
    -Kiểm tra điều thoát kiện bằng if, nếu điều kiện sai thì break
    
    VD:     while True:
                (your code goes here)
                if not condition:
                    break

                                 '''
i = 0
while True:
    print(i)
    if not i > 0:
        break

''' Đoạn code trên sẽ tương đương đoạn code sau trong C++
    
    do{
        print(i)
    } while(i>0)     '''

