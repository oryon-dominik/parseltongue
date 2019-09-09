#!/usr/bin/env python3
# coding: utf-8

def radix_LSD_sort(array):
    """
    Fastest self-written sort algorithm
    Speed@100_000 tries: ~ 1 Second
    Speed@100_000_000 tries: 34 Minutes, 43 Seconds (compared to 2 Minutes 52 Seconds for python_C_implemented TIM)

    # with base '10' - other bases need a generated bucketlist, and can directly be put inside that generated index, depending on base
    """

    maxdigits = 10  # important setting, this is the biggest number! 64-bit = 19 digits , 32-bit = 10 digits
    array = [str(n).rjust(maxdigits, '0') for n in array]
    for i in range(-1, -(maxdigits + 1), -1):
        bucket0, bucket1, bucket2, bucket3, bucket4, bucket5, bucket6, bucket7, bucket8, bucket9 = [], [], [], [], [], [], [], [], [], []
        for digit in array:
            if digit[i] == '0':
                bucket0.append(digit)
            elif digit[i] == '1':
                bucket1.append(digit)
            elif digit[i] == '2':
                bucket2.append(digit)
            elif digit[i] == '3':
                bucket3.append(digit)
            elif digit[i] == '4':
                bucket4.append(digit)
            elif digit[i] == '5':
                bucket5.append(digit)
            elif digit[i] == '6':
                bucket6.append(digit)
            elif digit[i] == '7':
                bucket7.append(digit)
            elif digit[i] == '8':
                bucket8.append(digit)
            elif digit[i] == '9':
                bucket9.append(digit)
        array = bucket0 + bucket1 + bucket2 + bucket3 + bucket4 + bucket5 + bucket6 + bucket7 + bucket8 + bucket9
    return [int(n) for n in array]
