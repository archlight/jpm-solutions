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
        else:
            i = j
        j += 1

    """
    this edge case only occurs with leading zeros and num=1
    """
    if bits[i] == "1" and len(bits)-i > max_len:
        result = i + 1
    return result
