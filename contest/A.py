from typing import List
from collections import Counter


def countsort(arr: List[int]):
    cnts = Counter(arr)
    return [n for n in range(201) for _ in range(cnts[n])]


def main():
    n = int(input())
    arr = map(int, input().split())
    for i in countsort(arr):
        print(i, end=" ")


main()
