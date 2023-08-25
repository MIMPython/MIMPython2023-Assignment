# Bài tập 13

from unidecode import unidecode

def convert_name(input):
    convert = unidecode(input)
    input_list = convert.split()
    result = ''.join(input_list)
    return result

input = "Nghệ An"
print(convert_name(input))