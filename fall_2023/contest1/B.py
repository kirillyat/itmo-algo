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


def merge_sort_count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        mid = len(arr)//2
        left, left_inversions = merge_sort_count_inversions(arr[:mid])
        right, right_inversions = merge_sort_count_inversions(arr[mid:])
        merged, split_inversions = merge_count_split_inversions(left, right)
        return merged, (left_inversions + right_inversions + split_inversions)


def merge_count_split_inversions(left, right):
    merged, split_inversions = [], 0
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            split_inversions += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, split_inversions


def count_inversions(arr):
    _, count = merge_sort_count_inversions(arr)
    print(count)
    return count


def main():
    _ = int(input())
    arr = list(map(int, input().split()))
    count_inversions(arr)


main()