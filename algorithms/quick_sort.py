#!/usr/bin/env python3
# coding: utf-8

def quick_sort(array):
    """ worst case n², best case: n * log n
    Speed@100_000 tries: 1.5 Seconds
    """

    pivot = len(array) // 2
    less, equals, greater = [], [], []

    for i in range(len(array)):
        if array[i] < array[pivot]:
            less.append(array[i])
        elif array[i] > array[pivot]:
            greater.append(array[i])
        else:
            equals.append(array[i])

    if len(less) > 1:
        less = quickSort(less)
    if len(greater) > 1:
        greater = quickSort(greater)

    return less + equals + greater
