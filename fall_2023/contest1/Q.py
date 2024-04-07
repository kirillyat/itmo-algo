def find_kth_sum(a, b, k):
    def count_pairs_smaller_or_equal_to_x(x):
        count, j = 0, len(b) - 1
        for i in range(len(a)):
            while j >= 0 and a[i] + b[j] > x:
                j -= 1
            count += j + 1
        return count

    left, right = a[0] + b[0], a[-1] + b[-1]
    while left < right:
        mid = (left + right) // 2
        if count_pairs_smaller_or_equal_to_x(mid) < k:
            left = mid + 1
        else:
            right = mid
    return left


n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))



print(find_kth_sum(sorted(a), sorted(b), k))
