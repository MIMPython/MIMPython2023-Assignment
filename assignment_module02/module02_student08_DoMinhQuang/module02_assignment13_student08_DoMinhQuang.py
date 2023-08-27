import unicodedata
def foo(s):

    s = s.replace(' ', '')
    s = s.replace('đ', 'd')
    s=s.replace('Đ',"D")
    s = ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
    return s

print(foo("Hà Nội"))#HaNoi
print(foo("Đà Nẵng"))#DaNang
print(foo("Nam Định"))#NamDinh