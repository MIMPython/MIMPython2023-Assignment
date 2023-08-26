alphabet = "abcdefghijklmnopqrstuvwxyz"
message = str(input(" Từ cần giải mã là: "))
key = 13
new_message= ""

def giai_ma(alphabet,message,key,new_message):
    for char in message:
        if char in alphabet:
            position = alphabet.find(char)
            new_position = (position + key) % 26
            new_char = alphabet[new_position]
            new_message += new_char
    print("mật mã đã giải là:"+new_message)
giai_ma(alphabet,message,key,new_message)


key2= -13
message1= str(input(" Từ cần mã hóa là: "))
new1_message= ""

def ma_hoa(alphabet,message1,key2,new1_message):
    for char1 in message1:
        if char1 in alphabet:
            position1= alphabet.find(char1)
            new1_position= (position1 + key2) % 26
            new1_char= alphabet[new1_position]
            new1_message += new1_char
    print("Mã hóa thành:"+ new1_message)
ma_hoa(alphabet,message1,key2,new1_message)




        