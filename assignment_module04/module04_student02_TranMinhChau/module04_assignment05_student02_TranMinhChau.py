# Bài tập 5: (Morse code)
# Sử dụng một bảng chuyển đổi để ánh xạ từ mã Morse sang các ký tự tương ứng
morse_code_dict = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z", "": " "
}

# Hàm giải mã mã Morse thành văn bản
def decode_morse_code(morse_code):
    # Tách mã Morse thành các từ
    words = morse_code.split(" / ")
    decoded_message = []
    
    for word in words:
        # Tách từ thành các ký tự Morse
        letters = word.split(" ")
        decoded_word = ""
        for letter in letters:
            if letter in morse_code_dict:
                decoded_word += morse_code_dict[letter]
        
        decoded_message.append(decoded_word)

    # Kết hợp các từ để tạo văn bản
    decoded_text = " ".join(decoded_message)
    return decoded_text

# Giải mã đoạn morse
morse_message = ".- .-.. .-.. .. .-- .- -. - - --- ... .- -.-- .. ... -.. --- - -.. --- - ... .--. .- -.-. . -.. --- - -.. .- ... .... -.. --- - -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. --- - -.. .- ... .... ... .--. .- -.-. . -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. --- - -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. .- ... ...."
decoded_message = decode_morse_code(morse_message)
print(decoded_message) #ALLIWANTTOSAYISDOTDOTSPACEDOTDASHDOTDOTSPACEDASHDASHDASHSPACEDOTDOTDOTDASHSPACEDOTSPACEDASHDOTDASHDASHSPACEDASHDASHDASHSPACEDOTDOTDASH
