#!/usr/bin/env python3
# coding: utf-8

"Towers of Hanoi (Lucas' Tower), recursive solution"

def hanoi(n, source: list, aux: list, target: list):  # n, source, auxiliary, target
    if not n: return
    hanoi(n -1, source, target, aux)
    assert len(target) == 0 or (len(source) > 0 and source[-1] < target[-1])
    target.append(source.pop())
    hanoi(n-1, aux, source, target)

discs = 7
src = list(reversed([i for i in range(1, discs + 1)]))
aux, target = [], []

print(f"The Tower moves: {src, aux, target}", end='')
hanoi(discs, src, aux, target)
result = src, aux, target
print(f" ====> {result}", end='\n')
