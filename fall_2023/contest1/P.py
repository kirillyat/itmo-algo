def solve(n, k):
    start, end = 0, n * n
    while start < end:
        mid = (start + end) // 2
        count = sum(min(mid // i, n) for i in range(1, n + 1))
        if count < k:
            start = mid + 1
        else:
            end = mid
    return start

n, k = list(map(int, input().split()))
print(solve(n, k))
