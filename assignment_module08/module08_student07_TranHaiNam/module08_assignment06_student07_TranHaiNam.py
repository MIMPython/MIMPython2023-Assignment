def Howmany_chains(n):
    count = 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            count += 1
        else:
            n = 3*n + 1
            count += 1
    return count

def num_longest_chain(n):
    longest_chain = 0
    n = n - 1
    while n > 100000:
        n -= 2
        current_chains = Howmany_chains(n)
        if longest_chain < current_chains:
            longest_chain = current_chains
            num_of_longest = n
    return num_of_longest,longest_chain
print(num_longest_chain(1000000)) # 525,837799

            




