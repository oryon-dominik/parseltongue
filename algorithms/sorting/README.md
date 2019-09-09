# sort algorithms

Comparing self implemented search algorithms for efficiency and runtime. \
Visualized in this [video](https://www.youtube.com/watch?v=kPRA0W1kECg)

You can testrun the algorithms yourself, by using the [compare script](compare_sort_algorithms.py).

TODO: let the algos run several thousand times and build visual charts on the results
TODO: complete the descriptions for the algorithms
TODO: add more sorting-algorithms

The Big-O [Bachman-Landau notation](https://en.wikipedia.org/wiki/Big_O_notation) measures the speed (=asymptotic growth rate) of sorting for lists of lenght n.

## Content

1. [Bubble Sort](#bubble-sort)
2. [Heap Sort](#heap-sort)
3. [Merge Sort](#merge-sort)
4. [Quick Sort](#quick-sort)
5. [Radix-LSD Sort](#radix-LSD-sort)
6. [Selection Sort](#selection-sort)
7. [Tim Sort](#tim-sort)

### Bubble Sort

Best case: O(n) \
Worst case: O(n²) \
Average: 1/4 * (n²-n)

Compare every element of the list with its neighbor, if its larger, swap them.\
Pop the last element to beginnging of a result list.\
Iterate over the remaining list again.

BUBBLE SORT IS MUCH TOO SLOW, even for testing purposes..

Speed@100_000 tries: 2 Hours, 9 Minutes 5 Seconds \
MUCH TOO SLOW, will not test with bubblesort anymore..

[Bubble Sort](bubble_sort.py)

### Heap Sort

Best case: O(n log n) \
Average: O(n log n)

heap-sort is too SLOW

Speed@100_000 tries: SLOW (with 10_000 it takes 32 Seconds, copared to radix, that takes 0.08 Seconds

[Heap Sort](heap_sort.py)

### Merge Sort

calculation time, roughly: len(array)* log(len(array)) -> [log base 2 of n]

Speed@100_000 tries: roughly 2 Seconds \
Is too slow with big numbers compared to Quick / Tim & Radix \
even this (kinda fast) version of merge-sort get's sorted out, because it's too slow on 'big data

[Merge Sort](merge_sort.py)

### Quick Sort

worst case n², best case: n * log n
Speed@100_000 tries: 1.5 Seconds

quick sort is fast, but others are faster

[Quick Sort](quick_sort.py)

### Radix-LSD Sort

the fastest implementation yet

Fastest self-written sort algorithm \
Speed@100_000 tries: ~ 1 Second \
Speed@100_000_000 tries: 34 Minutes, 43 Seconds (compared to 2 Minutes 52 Seconds for python_C_implemented TIM) \
with base '10' - other bases need a generated bucketlist, and can directly be put inside that generated index, depending on base

[Radix-LSD Sort](radix_LSD_sort.py)

### Selection Sort

[Selection Sort](selection_sort.py)

one of the slower algorithms..

calculation time, roughly: len(array)**2 -> [n²] \
Speed@100_000 tries: 19 Minutes 40 Seconds

### Tim Sort

Comparing to Pythons implemented Tim-Sort ... takes 0.6 Seconds for 1_000_000 ! implemented in C
