#Tạo hàm biến 1 string thành mật mã theo ROT-13
def rot13(string):
    lst = []
    for i in range(len(string)):
        character = ord(string[i])
        if (character < ord('A')+13) or (ord('a')<character and character<ord('a')+13):
            character += 13
        else:
            character -= 13
        lst.append(chr(character))
    return ''.join(lst)
#Tạo hàm giải mật mã ROT-13 (ngược lại với hàm rot13)
def decoderot13(string):
    lst = []
    for i in range(len(string)):
        temp = ord(string[i])
        if (temp > ord('a')+13) or (ord('a')>temp and temp>ord('A')+13):
            temp -= 13
        else:
            temp += 13
        lst.append(chr(temp))
    return ''.join(lst)
#Test
print(rot13('Python')) #Clguba
print(decoderot13('Clguba')) #Python