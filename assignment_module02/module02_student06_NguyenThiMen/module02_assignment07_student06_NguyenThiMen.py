def encrypt_text(text, distance):
    encoded_text = ''
    for char in text:
        if char.isalpha():
            if ord(char) + distance > ord('Z'):
                encoded_text += chr(ord(char) + distance - 26)
            else:
                encoded_text += chr(ord(char) + distance)
    return encoded_text


def decrypt_text(text, distance):
    decoded_text = ''
    for char in text:
        if char.isalpha():
            if ord(char) - distance < ord('A'):
                decoded_text += chr(ord(char) - distance + 26)
            else:
                decoded_text += chr(ord(char) - distance)
    return decoded_text

if __name__ == '__main__':
    message1 = encrypt_text('HELLO', 13)
    print(message1)
    message2 = decrypt_text('URYYB', 13)
    print(message2)
