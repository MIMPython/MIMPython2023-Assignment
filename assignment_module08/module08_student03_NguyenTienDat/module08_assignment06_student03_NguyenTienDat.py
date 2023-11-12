# Bài tập 6

def Longest_Collatz_Sequence(n, memory):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        if n in memory:
            break
        else:
            sequence.append(n)

    # Update memory for all numbers in the sequence
    for i, num in enumerate(reversed(sequence)):
        memory[num] = i + 1 + (memory[n] if n in memory else 0)

    return memory[sequence[0]]

def find_max(upper_limit):
    max_length = 0
    number_with_max_length = 0
    memory = {1: 1}

    for i in range(upper_limit // 2, upper_limit + 1):
        current_length = Longest_Collatz_Sequence(i, memory)
        if current_length > max_length:
            max_length = current_length
            number_with_max_length = i

    return number_with_max_length # output: 837799

print(find_max(10**6)) 
