paragraph = '''Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you'll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.'''
# (a) Kiểm tra xem các từ khóa Python, contains, experience, difficult có tồn tại 
# trong đoạn văn trên hay không?
keywords=[ "Python","contains","experience","difficult"]
for word in keywords:
    print(f'{word} in paragraph: {paragraph.find(word) != -1} ')

# (b) Đếm số lần xuất hiện của từ khóa Python trong đoạn văn.
print(paragraph.count("Python"))

# (c) Tính số từ trong đoạn văn trên.
array_word_of_paragraph = paragraph.split(" ")
for filterWord in array_word_of_paragraph:
    if filterWord.isalpha()==False:
        array_word_of_paragraph.remove(filterWord)
print(len(array_word_of_paragraph))

# (d) Viết lại đoạn văn trên, trong đó viết hoa tất cả các chữ cái trong câu đầu tiên của đoạn văn.
sentences = paragraph.split(". ")
sentences[0] = sentences[0].upper()
print('.'.join(sentences))
