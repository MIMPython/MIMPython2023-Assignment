#Bài tập 7: (Mật mã Caesar)
def rot_13(message):
    nhap = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    vao = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    result = ""
    for char in message:
        if char in nhap:
            index = nhap.index(char)
            result += vao[index]
        else:
            result += char
    return result
orginal = "python"
encoded = rot_13(orginal)
decoded = rot_13(encoded)

print("Thông điệp mã hóa là:", encoded)
print("Giải mã thông điệp :", decoded)



