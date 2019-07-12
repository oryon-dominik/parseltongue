#!/usr/bin/env python3
# coding: utf-8

'''
Comparing self implemented search algorithms for efficiency
'''

import random
import copy
import time

from bubble_sort import bubble_sort
from heap_sort import heap_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from radix_LSD_sort import radix_LSD_sort
from selection_sort import selection_sort


def other_sorting_algorithms(array):
    # std_Sort_gcc
    # quickSort3
    # ->  insertionSort
    # shellSort
    # std_stableSort_gcc
    # -> cocktail_shakerSort
    # -> double_selection_sort
    # -> gravity_sort
    # gnomeSort
    # bitonicSort
    # bogoSort
    return array

def build_test_array(size):
    print('Building the test-array ...')
    t_array = []  # deleting old data inside the array
    startBuild = time.time()
    t_array = [random.randint(1, size) for x in range(size)]
    buildTime = time.time() - startBuild
    print(f'Building-Time {buildTime} \n', 'The test-array:\n', t_array[:10] if len(t_array) > 10 else t_array, '...')
    return t_array



print('Testing the speed of different sorting Algorithms \nimplemented in Python')

test_size = 1_000_000

t_array = build_test_array(test_size)

# the test-array has to be copied otherwise it stays ordered when using it again
t_array1 = t_array.copy()
t_array2 = t_array.copy()
t_array3 = t_array.copy()
t_array4 = t_array.copy()
t_array5 = t_array.copy()
t_array6 = t_array.copy()


print('Calculating Selection-Sort ...')  # one of the slower algorithms..
# startSort = time.time()
# selection = selection_sort(t_array1)
print("Skipping Selection-Sort")
# selectionTime = time.time() - startSort
# print(f'Selection-Sort-Time {selectionTime} \n', selection[:10] if len(selection) > 10 else selection)


print('Calculating Bubble-Sort ...')  # BUBBLE SORT IS MUCH TOO SLOW, even for testing purposes..
# startSort = time.time()
# bubble = bubble_sort(t_array2)
print("Skipping Bubble-Sort")
# bubbleTime = time.time() - startSort
# print(f'Bubble-Sort-Time {bubbleTime} \n', bubble[:10] if len(bubble) > 10 else bubble)


print('Calculating Merge-Sort ...')  # even this (kinda fast) version of merge-sort get's sorted out, because it's too slow on 'big data'
# startSort = time.time()
# merge = merge_sort(t_array3)
print("Skipping Merge-Sort")
# mergeTime = time.time() - startSort
# print(f'Merge-Sort-Time {mergeTime} \n', merge[:10] if len(merge) > 10 else merge)


print('Calculating Quick-Sort ...')  # quick sort is fast, but others are faster
# startSort = time.time()
# quick = quick_sort(t_array4)
print("Skipping Quick-Sort")
# quickTime = time.time() - startSort
# print(f'Quick-Sort-Time {quickTime} \n', quick[:10] if len(quick) > 10 else quick)


print('Calculating Radix-Sort ...')  # the fastest implementation yet
startSort = time.time()
radix = radix_LSD_sort(t_array5)
radixTime = time.time() - startSort
print(f'Radix-Sort-Time {radixTime} \n', radix[:10] if len(radix) > 10 else radix)


print('Comparing to Pythons implemented Tim-Sort ... ') # takes 0.6 Seconds for 1_000_000 ! implemented in C
startSort = time.time()
tim = sorted(t_array6)
timTime = time.time() - startSort
print(f'Radix-Sort-Time {timTime} \n', tim[:10] if len(tim) > 10 else tim)


print('Calculating Heap-Sort ...')  # heap-sort is too SLOW
# startSort = time.time()
# heap = heapSort(t_array6)
print("Skipping Heap-Sort")
# heapTime = time.time() - startSort
# print(f'Heap-Sort-Time {heapTime} \n', heap[:10] if len(heap) > 10 else heap)


print('Finished calculating ...')

# print('Do all methods hold equal results?', selection==bubble==merge==quick==radix==heap)  # spoiler: they do
