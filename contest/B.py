from typing import List

def countinvers(arr: List[int]):
    count = 0
    k = 0
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            if count == 0:
                count = 1
            k+=1
            count *= k
    
    return count


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(countinvers(arr))


main()