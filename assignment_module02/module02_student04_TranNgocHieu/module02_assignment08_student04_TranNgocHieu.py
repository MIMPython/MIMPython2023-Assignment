def half_pyramid(size):
    # In ra màn hình một hình half-pyramid cỡ là size.
    for i in range(1, size + 1):
        star_str = ''
        for j in range(1, i + 1):
            star_str += '*'
        print(star_str)

half_pyramid(3) 
# *
# **
# ***

def inv_half_pyramid(size):
    # In ra màn hình một hình inverted-half-pyramid cỡ là size.
    for i in range(1, size + 1):
        star_str = ''
        for j in range(1, size - i + 2):
            star_str += '*'
        print(star_str)

inv_half_pyramid(3)
# ***
# **
# *

def hol_inv_half_pyramid(size):
    # In ra màn hình một hình hollow-inverted-half-pyramid cỡ là size.
    for i in range(1, size + 1):
        star_str = ''
        if i == 1 or i == size - 1 or i == size:
            for j in range(1, size - i + 2):
                star_str += '*'
        else:
            for j in range(1, size - i + 2):
                if j == 1 or j == size - i + 1:
                    star_str += '*'
                else: star_str += ' '
        print(star_str)

hol_inv_half_pyramid(5)
# *****
# *  *
# * *
# **
# *

def full_pyramid(size):
    # In ra màn hình một full-pyramid có cỡ là size.
    for i in range(1, size + 1):
        star_str = ''
        for j in range(1, size - i + 1):
            star_str += ' '
        star_str += '*'
        for j in range(1, i):
            star_str += ' *'
        print(star_str)

full_pyramid(5)
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

def inv_full_pyramid(size):
    # In ra màn hình một inverted-full-pyramid có cỡ là size.
    for i in range(1, size + 1):
        star_str = ''
        for j in range(1, i):
            star_str += ' '
        star_str += '*'
        for j in range(1, size - i + 1):
            star_str += ' *'
        print(star_str)

inv_full_pyramid(5)
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

def hol_full_pyramid(size):
    # In ra màn hình một hollow-full-pyramid có cỡ là size.
    for i in range(1, size + 1):
        star_str = ''
        if i == 1 or i == size:
            for j in range(1, size - i + 1):
                star_str += ' '
            star_str += '*'
            for j in range(1, i):
                star_str += ' *'
        else:
            for j in range(1, size - i + 1):
                star_str += ' '
            star_str += '*'
            for j in range(1, i - 1):
                star_str += '  '
            star_str += ' *'
        print(star_str)

hol_full_pyramid(5)
#     *
#    * *
#   *   *
#  *     *
# * * * * *