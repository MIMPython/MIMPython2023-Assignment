"""
a) Ta chỉ cần đếm các bội của 5 và luỹ thừa của 5 trong mỗi bội ấy là
sẽ được số chữ số 0 trong kết quả của n!
"""

def findMultipleOfFive(n):
    """
    Return the power of 5 in n!
    """
    if n == 0:
        return 0
    else:
        count = 0
        pow = -1
        while 5**pow <= n:
            pow += 1
        pow -= 1
        # pow has the property: 5^pow <= n < 5^(pow + 1)
        for i in range(1, pow + 1):
            count += int(n / 5**i)
        return count
    
print(findMultipleOfFive(100))

"""
b) Ví dụ với n = 27:
Ta quan tâm tới chữ số gần nhất khác 0 khi đi từ phải sang trái của n!, do
vậy ta muốn biết chữ số tận cùng của số n! / 10^k, với k là sỗ chữ số 0
tận cùng của n!. Vì vậy, trong quá trình tính toán, ta mong muốn chia 10
nhiều nhất có thể, và đánh giá chữ số tận cùng của tích các nhân tử 
không tạo ra bội của 10.
Có thể chia dãy 1-27 như sau:
1, 2,..., 4, 5, 
6, 7, ..., 9, 10
...
21, 22, 23, 24, 25,
26, 27
Ta có một số nhận xét:
(1) Mỗi dãy 4 số liên tiếp x1, x2, x3, x4 hay x6, x7, x8, x9 cho ta một tích
có tận cùng là 4.
(2) Tách dãy 5, 10, 15, 20, 25 (gồm các số là bội của 5 ra khỏi dãy ban
đầu), rồi rút nhân tử 5 từ mỗi thừa số ra ngoài. Ta thu được dãy dạng
5^5 (1.2.3.4.5). Ta biết rằng đến cuối cùng phần 5^5 này sẽ được chia
khỏi số n!, nên ta chia luôn nó đi. Muốn vậy ta cần lấy 2^5 từ dãy số
1, 2, 3, 4, 6, 7, 8, 9, 11, ..., 21, 22, 23, 24, 26, 27.
(3) Từ nhận xét (1), không hề khó để tính chữ số tận cùng của tích trên,
do đó khi "chia bớt" 2^5 khỏi tích này, ta vẫn tìm được chữ số tận cùng
của thương, với lưu ý rằng sau khi chia kết quả (dường như) luôn là số
chẵn.
    Các số dạng 2^k có các chữ số tận cùng lặp lại theo quy luật 2, 4
    8, 6, 2, 4, 8, 6, ... Nói riêng, 2^5 có tận cùng là 2.
    Vì A = 1*2*3*4*6*7*...*23*24*26*27 có tận cùng là 8, thương A / 2^5
    sẽ có tận cùng là 4 (vì nó là một số chẵn).
(4) Sau khi có chữ số 4 này, việc còn lại cần làm là:...
Đúng vậy, tính chữ số gần nhất khác 0 của 1.2.3.4.5 (dãy số còn sót
lại từ nhận xét (2), sau khi bỏ các nhân tử 5). Đến đây ta có thể đệ
quy.

Hy vọng là làm được !
"""

def getRightMostDigit(n):
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 6
    if n == 4: return 4
    else:
        m = int(n / 5)
        if m % 2 == 0:
            digit = 6
        else:
            digit = 4
        for i in range(m * 5 + 1, n + 1):
            digit = (digit * (i % 10)) % 10
        remainder = [2, 4, 8, 6]
        index = remainder.index(digit)
        digit = remainder[(index - (m % 4) % 4)]
        return (digit * getRightMostDigit(m)) % 10
    
print(getRightMostDigit(10**23))