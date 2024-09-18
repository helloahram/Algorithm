# Quick Sort
from typing import MutableSequence

def qSort(a: MutableSequence, left: int, right: int) -> None:
    pl = left
    pr = right
    x = a[(left+right)//2]

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qSort(a, left, pr)
    if pl < right: qSort(a, pl, right)

def QuickSort(a: MutableSequence) -> None:
    qSort(a, 0, len(a)-1)

if __name__ == "__main__":
    num = int(input())
    x = [None] * num

    for i in range(num):
        x[i] = int(input())

    QuickSort(x)

    for i in range(num):
        print(x[i])