def vi_to_lat_convert(string):
    vi_to_lat = {
        'a': 'aàáảãạâầấẩẫậăằắẳẵặ', 'A': 'AÀÁẢÃẠÂẦẤẨẪẬĂẰẮẲẴẶ',
        'e': 'eèéẻẽẹêềếểễệ', 'E': 'EÈÉẺẼẸÊỀẾỂỄỆ',
        'i': 'iìíỉĩị', 'I': 'IÌÍỈĨỊ',
        'y': 'yỳýỷỹỵ', 'Y': 'YỲÝỶỸỴ',
        'o': 'oòóỏõọôồốổỗộơờớởỡợ', 'O': 'OÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢ',
        'u': 'uùúủũụưừứửữự', "U": 'UÙÚỦŨỤƯỪỨỬỮỰ',
        'd': 'dđ', 'D': 'DĐ'
    }
    new_str = ''
    for i in string:
        if i == ' ': 
            continue
        count = 0
        for key in vi_to_lat.keys():
            if i in vi_to_lat[key]:
                new_str += key
                count = 1
                break
        if count == 0:
            new_str += i
    return new_str

"""
(Không cần thiết)
Lấy tên các tỉnh trên wiki làm input
"""

import requests
from bs4 import BeautifulSoup

url = "https://vi.wikipedia.org/wiki/Tỉnh_thành_Việt_Nam"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

province_table = soup.find_all("tbody")[2]
province_table_rows = province_table.find_all("tr")[1:63]

province_list = []
for row in province_table_rows:
    province = row.find_all("td")[1].text.strip()
    province_list.append(province)

for i in province_list:
    print(vi_to_lat_convert(i), '\n')

