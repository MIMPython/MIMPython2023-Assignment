import unidecode

def convert_province_name(name):
    result = unidecode.unidecode(name).replace(" ", "")
    return result

if __name__ == '__main__':
    print(convert_province_name('Hà Nội'))
