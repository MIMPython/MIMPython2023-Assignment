# Đọc văn bản
passage = 'Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.'
# List các đối tượng cần kiểm tra
wordList = ['Python', 'contains', 'experience', 'difficult']
# Hàm kiểm tra xem 1 từ có xuất hiện trong đoạn
def wordCheck(word):
    if word in passage:
        return f"The word {word} is in the passage"
    else:
        return f"The word {word} is not in the passage"
# Hàm đếm số lần xuất hiện của 1 từ trong đoạn
def wordCounter(passage, word):
    lst = str(passage).split(' ')
    count = 0
    for w in lst:
        if word == w:
            count +=1
    return f"There are {count} '{word}' in the passage"
# Hàm đếm số từ có trong đoạn
def length(passage):
    lst = (passage).split()
    count = len(lst)
    return f"There are {count} words in the passage"
# Hàm biến câu đầu tiên của đoạn văn thành in hoa
def upperFirstSentence(passage):
    lst = (passage).split()
    for i in range(len(lst)):
        lst[i]=lst[i].upper()
        if '.' in lst[i]:
            break
    passage = ' '.join(lst)
    return passage
# Test
for word in wordList:
    print(wordCheck(word))
    
print(wordCounter(passage, 'Python'))
print(length(passage))
print(upperFirstSentence(passage))
