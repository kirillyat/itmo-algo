def is_valid_partition(nums, max_sum, k):
    current_sum = 0
    segments = 1
    for num in nums:
        if current_sum + num > max_sum:
            segments += 1
            current_sum = num
        else:
            current_sum += num

        if segments > k:
            return False
    return True


def min_max_sum(nums, k):
    low = max(nums)
    high = sum(nums)
    result = high

    while low <= high:
        mid = (low + high) // 2

        if is_valid_partition(nums, mid, k):
            result = min(mid, result)
            high = mid - 1
        else:
            low = mid + 1

    return result


n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
print(min_max_sum(nums, k))
