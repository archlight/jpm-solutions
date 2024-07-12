"""
Write a function that accept a number and returns the starting position 
of the longest continuous sequence of 1s in its binary format.
"""


def solution(num: int, include_leading_zeros=False):
    bits = bin(num)[2:] if not include_leading_zeros else '{:08b}'.format(num)
    i = j = 0
    max_len = 0
    result = 0
    while j < len(bits):
        if bits[i] == "1" and bits[j] == "1":
            window_len = j - i + 1
            if window_len > max_len:
                max_len = window_len
                result = i + 1
            j += 1
        else:
            i = j
            # if j-th bit is 1, it will reset the moving window
            # to be evaluated in the next iteration
            if bits[j] == "0":
                j += 1        

    return result
