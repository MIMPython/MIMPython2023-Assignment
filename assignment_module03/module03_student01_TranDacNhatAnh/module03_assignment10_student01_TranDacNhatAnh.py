#a)
# Như đã bình luận ở câu 9, khác biệt duy nhất giữa 2 cách viết này nằm ở chỗ: nếu ở lần thực hiện đầu tiên điều kiện 
# đã không đúng, thì while-do sẽ dừng ngay, còn do-while có 1 lần thực hiện.

#b) 
# Đề xuất: thực hiện "thủ công" nội dung trong vòng lặp ở bước đầu tiên, sau đó mới sử dụng while.
# Ví dụ, một đoạn code C++ in ra số nguyên thuộc đoạn [1, 5] khi i thay đổi trong vòng lặp như sau:
'''
#include <iostream>

using namespace std;

int main() {
    int i = 6; 
    do {
        cout << i << " ";
        i--;
    }
    while (1<=i && i<=5);
    return 0;
}
'''
# Rõ ràng không thể bê nguyên văn sang Python là while 1<=i and i<=5: print(i) \ i -= 1 được, vì kết quả sẽ là không
# có số nào. Tuy nhiên cách làm dưới đây có thể mang lại hiệu quả tương đương do-while:
i = 6
print(i, end=' ', flush= True) 
# Việc kết thúc "print" bằng ' ' có tác dụng ngăn xuống dòng (thay vào đó là dấu cách) nhằm đạt hiệu quả tương tự 
# việc in bằng "cout" của C++ 
i -= 1
while (1<=i and i<=5):
    if i>1:
        print(i, end=' ', flush= True)
    else:
        print(i)
    i -= 1
# 6 5 4 3 2 1