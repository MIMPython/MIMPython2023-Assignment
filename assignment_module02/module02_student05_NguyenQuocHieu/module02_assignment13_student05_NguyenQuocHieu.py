import re


def convertAccent2NoAccent(word: str) -> str:
    word = re.sub(r'[àáãảạăằắẵẳặâầấẫẩậ]', 'a', word)
    word = re.sub(r'[ÀÁÃẢẠĂẰẮẴẲẶÂẦẤẪẨẬ]', 'A', word)
    word = re.sub(r'[èéẻẽẹêềếểễệ]', 'e', word)
    word = re.sub(r'[ÈÉẺẼẸÊỀẾỂỄỆ]', 'E', word)
    word = re.sub(r'[òóỏõọôồốổỗộơờớởỡợ]', 'o', word)
    word = re.sub(r'[ÒÓỎỠỌÔỒỐỔỖỘƠỜỚỞỠỢ]', 'O', word)
    word = re.sub(r'[ìíỉĩị]', 'i', word)
    word = re.sub(r'[ÌÍỈĨỊ]', 'I', word)
    word = re.sub(r'[ùúủũụưừứửữự]', 'u', word)
    word = re.sub(r'[ÙÚỦŨỤƯỪỨỬỮỰ]', 'U', word)
    word = re.sub(r'[ỳýỷỹỵ]', 'y', word)
    word = re.sub(r'[ỲÝỶỸỴ]', 'Y', word)
    word = re.sub(r'[đ]', 'd', word)
    word = re.sub(r'[Đ]', 'D', word)
    return word


if __name__ == "__main__":
    word = input()
    print(convertAccent2NoAccent(word=word))
