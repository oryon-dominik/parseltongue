#!/usr/bin/env python3
# coding: utf-8

def bubble_sort(array):
    """ /Speed@100_000 tries: 2 Hours, 9 Minutes 5 Seconds
    MUCH TOO SLOW, will not test with bubblesort anymore..
    """
    switch = True
    while switch:
        switch = False
        for index, number in enumerate(array):
            if index + 1 < len(array):
                if number > array[index + 1]:
                    array[index], array[index + 1] = array[index + 1], array[index]
                    switch = True
    return array
