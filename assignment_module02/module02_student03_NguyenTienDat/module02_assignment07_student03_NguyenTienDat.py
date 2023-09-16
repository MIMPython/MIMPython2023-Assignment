# Bài tập 7: 
# Decoding Caesar cipher.
# ROT-13

import string

# Decode
def  decode_4_word(word): # Decode the word
    all_letters = list(string.ascii_uppercase)
    # create a list containing characters from 2 alphabet sets
    data = all_letters + all_letters

    # create a list containing characters of input
    char_of_input = []
    for char in word:
        char_of_input.extend(char.upper())

    index = 0
    i = 0
    while index < len(char_of_input):
        if char_of_input[index].isalpha(): 
            if char_of_input[index] == data[i]: 
                char_of_input[index] = data[i + 19]
                index += 1
                i = 0
            else:
                i += 1
        else:
            char_of_input[index] = char_of_input[index]
            index += 1
    result = ''.join(char_of_input)
    return (result)


def decode_4_sentence(input): # Decode the sentence 
    data = input.split()
    for i in range(0, len(data)):
        data[i] = decode_4_word(data[i])
    result = ' '.join(data)
    print(result)


# Encode
def encode_4_word(word): # Encode the word
    all_letters = list(string.ascii_uppercase)
    # create a list containing characters from 2 alphabet sets
    data = all_letters + all_letters

    # create a list containing characters of input
    char_of_input = []
    for char in word:
        char_of_input.extend(char.upper())
    
    index = len(char_of_input) - 1 
    i = len(data) - 1
    while index >= 0:
        if char_of_input[index].isalpha():
            if char_of_input[index] == data[i]: 
                char_of_input[index] = data[i - 19]
                index -= 1
                i = 0
            else:
                i -= 1
        else:
            char_of_input[index] = char_of_input[index]
            index -= 1
    result = ''.join(char_of_input)
    return (result)


def encode_4_sentence(input): # Encode the sentence
    data = input.split()
    for i in range(0, len(data)):
        data[i] = encode_4_word(data[i])
    result = ' '.join(data)
    print(result)


if __name__ == "__main__":
    input1 = "Hello, I have successfully solved the problem."
    decode_4_sentence(input1)
    input2 = "AXEEH, B ATOX LNVVXLLYNEER LHEOXW MAX IKHUEXF."
    encode_4_sentence(input2)