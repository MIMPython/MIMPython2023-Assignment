morse_code = """.- .-.. .-.. .. .-- .- -. - - --- ... .- -.-- .. ... -.. --- - -.. --- - ... .--. .-
-.-. . -.. --- - -.. .- ... .... -.. --- - -.. --- - ... .--. .- -.-. . -.. .- ... ....
-.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. --- - -.. .-
... .... ... .--. .- -.-. . -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. --- - -..
.- ... .... -.. .- ... .... ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .-
... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. .- ... ...."""

# Get morse list
morse_line = morse_code.split("\n")
morse_list = []
for line in morse_line:
    morse_list += line.split(" ")

# Morse code dictionary
# Credits: GeeksForGeeks
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# Get word string
string = ""
for letter in morse_list:
    for key in MORSE_CODE_DICT.keys():
        if MORSE_CODE_DICT[key] == letter:
            string += key
# print(string)

# Remove nonsense at the beginning of string
num = string.find("DOT")
first_string = string[:num]
second_string = string[num:]

# Turn nightmarish script to morse list
second_string = second_string.replace("DOT", ".")
second_string = second_string.replace("DASH", "-")
new_morse_list = second_string.split("SPACE")

# Final message
message = first_string
for letter in new_morse_list:
    for key in MORSE_CODE_DICT.keys():
        if MORSE_CODE_DICT[key] == letter:
            message += key

print(message)