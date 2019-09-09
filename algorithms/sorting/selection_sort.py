#!/usr/bin/env python3
# coding: utf-8

def selection_sort(array):
    """ calculation time, roughly: len(array)**2 -> [n²]
        Speed@100_000 tries: 19 Minutes 40 Seconds
    """
    for index, number in enumerate(array):
        smallest = number
        position = 0
        for idx, num in enumerate(array[index:]):
            if num < smallest:
                smallest, position = num, idx
        array[index], array[position + index] = array[position + index], array[index]
    return array
