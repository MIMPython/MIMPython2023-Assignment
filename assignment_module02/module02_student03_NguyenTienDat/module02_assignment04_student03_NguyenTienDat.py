# Bài tập 4

data_string = """
Python was designed to be easy to understand and fun to use (its name came
from Monty Python so a lot of its beginner tutorials reference it). Fun is
a great motivator, and since you’ll be able to build prototypes and tools
quickly with Python, many find coding in Python a satisfying experience.
Thus, Python has gained popularity for being a beginner-friendly language,
and it has replaced Java as the most popular introductory language at Top
U.S. Universities.
"""

# (a)
def test_a(data_string):
    print('Python' in data_string)
    print('contains' in data_string)
    print('experience' in data_string)
    print('difficult' in data_string)


# (b)
def test_b(data_string):
    count = 0
    data_array = data_string.split()
    key_word = "Python"
    for key_word in data_array:
        count += 1
    print(f"The frequency of occurrences of 'Python' in the dataset is {count}")


# (c)
def test_c(data_string):
    count = 0 
    for char in data_string:
        if char != '\n' and char != ' ':
            count += 1
    # result :
    print(count)


# (d)
def test_d(data_string):
    # find index the final dot of first sentence.
    index  = 0
    for char in data_string:
        index += 1
        if char == '.':
            break
    result = data_string[0: index].upper() + data_string[index:]
    print (result)


if __name__ == "__main__":
    print ("(a)")
    test_a(data_string)
    print ("(b)")
    test_b(data_string)
    print ("(c)")
    test_c(data_string)
    print ("(d)")
    test_d(data_string)