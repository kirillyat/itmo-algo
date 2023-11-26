import bisect

def closest_number(arr, target):
    index = bisect.bisect_left(arr, target)
    if index == 0:
        return arr[0]
    if index == len(arr):
        return arr[-1]
    if abs(arr[index] - target) < abs(arr[index-1] - target):
        return arr[index]
    return arr[index-1]

n, k = map(int, input().split())
array = list(map(int, input().split()))
queries = list(map(int, input().split()))

for query in queries:
    result = closest_number(array, query)
    print(result)
