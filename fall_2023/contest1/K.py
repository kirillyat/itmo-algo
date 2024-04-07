def is_enough_time(mid, n, x, y):
    total_copies = mid // x + mid // y
    return total_copies >= n


def min_time_to_copy(n, x, y):
    if x > y:
        x, y = y, x

    low = x
    high = x * n

    while low < high:
        mid = (low + high) // 2
        if is_enough_time(mid - x, n - 1, x, y):
            high = mid
        else:
            low = mid + 1

    return low


n, x, y = map(int, input().split())


print(min_time_to_copy(n, x, y))
