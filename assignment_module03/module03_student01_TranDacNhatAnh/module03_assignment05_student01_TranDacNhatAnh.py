#a) 
loopEndCondition = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
while True:
    something = (input('please enter something'))
    if something in loopEndCondition:
        print(f'Program stopped by {something}')
        break
# Em có dự định để input type là 'Any', tuy nhiên khi đó bất kì thứ gì được nhập vào cũng không dừng chương trình lại.
# Vì sao lại thế ạ :v

#b)
inputSet = list[str](['rock', 'paper', 'scissors'])
while 1:
    player1 = str(input('Player 1 to play'))
    player2 = str(input('Player 2 to play'))
    if (player1 in inputSet and player2 in inputSet):
        break

result = inputSet.index(player1) - inputSet.index(player2)
if result%3 == 1: # Nếu lựa chọn của Player 1 "ở bên trái" lựa chọn của Player 2 trong list thì player 1 thắng
    print('Player 1 win')
elif result%3 == 2: # Ngược lại, "ở bên trái" thì Player 2 thắng
    print('Player 2 win')
else:
    print('It is a tie')
# Điều duy nhất "gây bất lợi" cho Player 1 trong chương trình trên là lựa chọn của anh ta sẽ bị Player 2 nhìn thấy, từ đó
# dẫn đến "mất cân bằng" cho game. Điều này có thể được khắc phụ một cách thủ công bằng cách yêu cầu người chơi ghi lại
# lựa chọn của mình ra giấy trước khi chơi :)))

#c)
from getpass import getpass
# Qua tìm hiểu thì đây là hàm giúp ta ẩn đi input của mình trong Terminal, được sử dụng cho những tình huống như tạo/nhập 
# mật khẩu cho tài khoản
# Giờ ta sửa lại chương trình ở trên với input được thay bởi getpass
inputSet = list[str](['rock', 'paper', 'scissors'])
player1 = getpass(prompt='Player 1 to play')
player2 = getpass(prompt='Player 2 to play')
result = inputSet.index(player1) - inputSet.index(player2)
if result%3 == 1: # Nếu lựa chọn của Player 1 "ở bên trái" lựa chọn của Player 2 trong list thì player 1 thắng
    print('Player 1 win')
elif result%3 == 2: # Ngược lại, "ở bên trái" thì Player 2 thắng
    print('Player 2 win')
else:
    print('It is a tie')

#d)
# Có thể hiểu, chỉ cần mỗi người chơi không có thông tin gì về lựa chọn của đối thủ khi đưa ra lựa chọn, hoặc thông tin
# có được không làm thay đổi tỉ lệ thắng-thua của mỗi người chơi (vốn là 50-50), thì trò chơi được coi là "công bằng".