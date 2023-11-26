import bisect

n = int(input().strip())
numbers = list(map(int, input().split()))
numbers.sort()
q = int(input().strip())
queries = [list(map(int, input().split())) for _ in range(q)]

for l, r in queries:
    left_index = bisect.bisect_left(numbers, l)
    right_index = bisect.bisect_right(numbers, r)
    print(right_index - left_index, end = ' ')
