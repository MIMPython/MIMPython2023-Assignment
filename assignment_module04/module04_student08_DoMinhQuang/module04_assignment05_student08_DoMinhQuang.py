'''Bài 5: Dịch mã Moorse'''
import re

# morse_string = '.- -. .... - ..- -. --. -.. . .--. - .-. .- .. -. .... .- - -- .. -- .--. -.-- - .... --- -.'
morse_string = '.- .-.. .-.. .. .-- .- -. - - --- ... .- -.-- .. ... -.. --- - -.. --- - ... .--. .- -.-. . -.. --- - -.. .- ... .... -.. --- - -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. --- - -.. .- ... .... ... .--. .- -.-. . -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. --- - -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. .- ... ....'
morse_list = morse_string.split(' ')
morse_table = {'.-': 'A','-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'}
#tạo ra 1 bảng mã

'''A L L I W A N T T O S A Y I S D O T D O T S P A C E D O T D A S H D O T D O T S P A C E D A S H D A S H D A S H S P A C E D O T D O T D O T D A S H S P A C E D O T S P A C E D A S H D O T D A S H D A S H S P A C E D A S H D A S H D A S H S P A C E D O T D O T D A S H :))
All i want to say is dot dot space dot dash dot dot space dash dash dash space dot dot dot dash space dot space dash dot dash dash space dash dash dash space dot dot dash  :)))
'''

string = ""
for i in morse_list:
    string = string + morse_table[i] #Cộng dần cac values vào string, trong đó values là các chữ cái

string_1 = string.replace('DOT','.')
string_2 = string_1.replace('DASH','-')
string_3 = string_2.replace('SPACE',' ')#ALLIWANTTOSAYIS.. .-.. --- ...- . -.-- --- ..-
new_morse_code = string_3[15:]

# string = re.sub(r'[DOT]', '.', string)
# string = re.sub(r'[SPACE]', ' ', string)
# string = re.sub(r'[DASH]', ' ', string)  #Bước này em định làm giống bài 13 module02 của anh Hiệu nhưng bị bug

print(new_morse_code)#.. .-.. --- ...- . -.-- --- ..-

new_morse_list = new_morse_code.split(' ')
for i in new_morse_list :
    print(morse_table[i], end = '')#ILOVEYOU

print()


def encrypt(input_string: str):
    upper_string = input_string.upper()
    list_symbol = list(morse_table.keys())
    list_letter = list(morse_table.values())
    zipped = zip(list_letter, list_symbol)
    new_morse_table = dict(zipped)
    string = ""
    for i in upper_string:
        if (i == ' '):
            string = string + ' '
        else:
            string = string + new_morse_table[i]  # Cộng dần cac values vào string, trong đó values là các chữ cái

    print(string)

encrypt('i l o v e y o u')#.. .-.. --- ...- . -.-- --- ..-

#Vậy câu trả lời của em là :
#.- -. .... - ..- -. --. -.. . .--. - .-. .- .. -. .... .- - -- .. -- .--. -.-- - .... --- -. :))


#Chạy code : python module04_assignment05_student08_DoMinhQuang.py