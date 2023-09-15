# Bài tập 10:
 
"""
a) Vòng lặp do-while ở C++ cho phép câu lệnh chạy trước rồi mới kiểm tra điều kiện ở while,
trong khi ở Python thì không có cấu trúc vòng lặp đó. Python chỉ có loop while, kiểm tra
điều kiện trước, nếu thỏa mãn thì nó sẽ chạy chương trình.
b) Dưới đây là một đoạn code tương đương giữa java (dùng do-while) và python (dùng while)
dùng để in ra các số từ 1 đến 5 trên 1 dòng:
"""
# Java: 
    int i = 1;
        do {
            System.out.print(i + " ");
            i++;
        } while (i < 6);
        
# Python:
    i = 1
    while (i < 5):
        print (i, end=" ")
        i += 1