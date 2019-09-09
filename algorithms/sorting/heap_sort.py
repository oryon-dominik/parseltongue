#!/usr/bin/env python3
# coding: utf-8

import math

def heap_sort(array):
    """ Speed@100_000 tries: SLOW (with 10_000 it takes 32 Seconds, copared to radix, that takes 0.08 Seconds """
    # building complete binary tree
    level = lambda x: int(math.log(x, 2))  # x > 0 !
    max_level = level(len(array))  # beginning from 0
    tree = [[] for x in range(max_level + 1)]
    for index, number in enumerate(array):
        l = level(index + 1)
        tree[l].append(number)
    array = []

    while len(tree) > 0:
        # transforming the heap
        for idx, lev in enumerate(reversed(tree)):
            current = (len(tree) - 1) - idx
            if current > 0:
                parent_tree = current - 1
            else:
                array.insert(0, tree[0][0])
                break
            for ix, n in enumerate(lev):
                parent_id = ix // 2
                if n > tree[parent_tree][parent_id]:
                    tree[current][ix], tree[parent_tree][parent_id] = tree[parent_tree][parent_id], tree[current][ix]

        # get last element of tree and swap with first, remove from heap after
        tree[0][0], tree[-1][-1] = tree[-1][-1], tree[0][0]
        del tree[-1][-1]

        # erase empty nodes
        for i, le in enumerate(tree):
            if len(le) == 0:
                del tree[i]

    return array
