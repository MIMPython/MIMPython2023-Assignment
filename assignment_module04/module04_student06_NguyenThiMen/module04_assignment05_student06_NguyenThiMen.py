# giải mã morse
with open('additionalFolder/module04_assignment05_student06_NguyenThiMen_morse_code.txt', 'r', encoding="utf8") as data:
    lines_list = data.readlines()
morse_dict = {}
for line in lines_list:
    key, value = line.strip().split('\t')
    morse_dict[key] = value

with open('additionalFolder/module04_assignment05_student06_NguyenThiMen_morse_.message.txt', 'r') as t:
    message = t.read()


def decrypt_text(message):
    decoded_text = ''
    chars = message.split()
    for char in chars:
        for key, value in morse_dict.items():
            if char == value:
                decoded_text += key
    return decoded_text


get_message = decrypt_text(message)
print(get_message)


def encrypt_text(result):
    encoded_text = ''
    for char in result:
        for key, value in morse_dict.items():
            if char == key:
                encoded_text += value + ' '
    return encoded_text.strip()


check_variable = encrypt_text(get_message)
if message == check_variable:
    print('OK')
else:
    print('Failed')
