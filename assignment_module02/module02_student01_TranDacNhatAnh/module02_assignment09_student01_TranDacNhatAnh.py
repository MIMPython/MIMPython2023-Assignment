# Mô tả bài toán
# 1  2  3

# 4  5  6

# 7  8  9

# Mỗi lượt, từng người chơi đánh dấu vào bảng mà không lặp lại các ô đã được đánh dấu (Input: một số tự nhiên trong 
# khoảng 1-9 tương ứng với vị trí được đánh dấu trên "bảng").
# Nếu sau khi một người chơi đánh dấu mà trong các ô được người này đánh dấu có 3 ô thẳng hàng với nhau, thì người đó thắng.

turn = 0 #Lượt chơi: lượt lẻ là của người đi trước, lượt chẵn là của người đi sau.

# Nếu một người chơi chọn được 1 bộ 3 số tương ứng với 3 ô thẳng hàng trên bảng thì người đó thắng.
WinCondition = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
A = []
B = []
while turn<9:
    if turn%2==0:
        a=int(input())
        A.append(a)
        A.sort()
        # Kiểm tra xem người A đã thắng hay chưa
        for lst in WinCondition:
            if a in lst:
                count =0
                for c in lst:
                    if c in A:
                        count +=1
                if count ==3:
                    print('1ST PLAYER WIN')
                    break
    else:
        b=int(input())
        B.append(b)
        # Kiểm tra xem người B đã thắng hay chưa
        for lst in WinCondition:
            if b in lst:
                count =0
                for c in lst:
                    if c in B:
                        count +=1
                if count ==3:
                    print('2ND PLAYER WIN')
                    break
    # Nếu chưa có người thắng, chuyển sang lượt tiếp theo
    if count ==3:
        break
    else:
        turn+=1
# Mỗi ván đấu có thể kéo dài tối đa là 9 lượt, sau đó (nếu vẫn chưa có người thắng) sẽ không còn ô nào để đánh dấu
if turn==9:
    print('TIE')