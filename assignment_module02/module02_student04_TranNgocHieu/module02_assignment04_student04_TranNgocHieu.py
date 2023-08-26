# a)
sample_str = """
    Python was designed to be easy to understand and fun to 
    use (its name came from Monty Python so a lot of its  
    beginner tutorials reference it). Fun is a great  
    motivator, and since you’ll be able to build  
    prototypes and tools quickly with Python, many find  
    coding in Python a satisfying experience. Thus, Python  
    has gained popularity for being a beginner-friendly  
    language, and it has replaced Java as the most popular  
    introductory language at Top U.S. Universities.
"""

def word_check(string, word):
    # Kiểm tra xem một từ nào đó có xuất hiện trong một văn bản không.
    word_length = len(word)
    string_length = len(string)
    i = 0
    for i in range(string_length - word_length + 1):
        if string[i:(i + word_length)] == word:
            return True
    return False


print(word_check(sample_str, 'Python'))    # True
print(word_check(sample_str, 'contains'))    # False
print(word_check(sample_str, 'experience'))    # True
print(word_check(sample_str, 'difficult'))    # False

# b)
def word_count(string, word):
    # Đếm số lần xuất hiện một từ trong một văn bản.
    word_length = len(word)
    string_length = len(string)
    count = 0
    for i in range(string_length - word_length + 1):
        if string[i:(i + word_length)] == word:
            count += 1
    return count

print(word_count(sample_str, 'Python'))    # 5

# c)
def num_of_words(string):
    """
    Đếm số từ trong một văn bản bằng cách
    tạo list các từ của văn bản với hàm split.
    Hàm này cũng có thể sử dụng được ngay từ đầu cho các câu trước.
    """
    string_list = string.split()
    return len(string_list)

print(num_of_words(sample_str))    # 78

# d)
def find_period(string):
    # Tìm vị trí của dấu chấm câu đầu tiên.
    string_length = len(string)
    for i in range(string_length + 1):
        if string[i] == '.':
            break
    return i

def make_cap(string):
    # In hoa câu đầu của một đoạn văn.
    string_length = len(string)
    period_num = find_period(string)
    new_string = ''
    for i in range(period_num + 1):
        new_string = new_string + string[i].upper()
    for i in range(period_num + 1, string_length):
        new_string = new_string + string[i]
    return new_string

print(make_cap(sample_str))    # Đoạn văn yêu cầu

