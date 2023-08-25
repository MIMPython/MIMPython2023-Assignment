def encoder_13C(string):
    encoded_str = ''
    str_length = len(string)
    for i in range(0, str_length):
        if ord(string[i]) >= 65 and ord(string[i]) <= 77:
            encoded_str += chr(ord(string[i]) + 13)
        else:
            encoded_str += chr(ord(string[i]) - 13)
    return encoded_str

print(encoder_13C('MIMPYTHON'))   # ZVZCLGUBA
print(encoder_13C('ZVZCLGUBA'))   # MIMPYTHON

"""
Vì ta chỉ làm trong trường hợp các ký tự được in hoa, nên có đúng 26
ký tự được sử dụng. Do đó, ánh xạ trên và ánh xạ ngược của nó là trùng
nhau. Nói cách khác, việc giải mã hoặc mã hoá một chuỗi ký tự sẽ cho 
cùng một kết quả.
"""