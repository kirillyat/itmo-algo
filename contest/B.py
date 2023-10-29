from typing import List
from collections import Counter

def countinvers(arr: List[int]):
    cnts = Counter(arr)
    return [n for n in range(201) for _ in range(cnts[n])]


def main():
    n = int(input())
    arr = map(int, input().split())
    print(countinvers(arr))

main()