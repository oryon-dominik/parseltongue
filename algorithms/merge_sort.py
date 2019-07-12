#!/usr/bin/env python3
# coding: utf-8

def merge_sort(array):
    """ calculation time, roughly: len(array)* log(len(array)) -> [log base 2 of n]
        Speed@100_000 tries: roughly 2 Seconds
        Is too slow with big numbers compared to Quick / Tim & Radix
     """
    if len(array) > 1:
        half1, half2 = array[:(len(array)//2)], array[(len(array)//2):]

        mergeSort(half1)
        mergeSort(half2)

        i, j, k = 0, 0, 0

        while i < len(half1) and j < len(half2):
            if half1[i] < half2[j]:
                array[k] = half1[i]
                i += 1
            else:
                array[k] = half2[j]
                j += 1
            k += 1

        while i < len(half1):
            array[k] = half1[i]
            i += 1
            k += 1

        while j < len(half2):
            array[k] = half2[j]
            j += 1
            k += 1

    else:
        return array

    return array
