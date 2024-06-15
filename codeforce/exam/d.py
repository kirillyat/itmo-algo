def longest_good_segment(n, heights, updates):
    left = [1] * n
    right = [1] * n

    # Initialize left array
    for i in range(1, n):
        if heights[i] > heights[i - 1]:
            left[i] = left[i - 1] + 1

    # Initialize right array
    for i in range(n - 2, -1, -1):
        if heights[i] > heights[i + 1]:
            right[i] = right[i + 1] + 1

    results = []

    for x, y in updates:
        idx = x - 1
        heights[idx] = y

        # Update left array
        if idx > 0:
            if heights[idx] > heights[idx - 1]:
                left[idx] = left[idx - 1] + 1
            else:
                left[idx] = 1
        
        # Update right array
        if idx < n - 1:
            if heights[idx] > heights[idx + 1]:
                right[idx] = right[idx + 1] + 1
            else:
                right[idx] = 1

        # Find the maximum length of the valid segment
        max_length = 0
        for i in range(n):
            max_length = max(max_length, left[i] + right[i] - 1)

        results.append(max_length)

    return results

# Example usage
n = int(input().strip())
heights = list(map(int, input().strip().split()))
m = int(input().strip())
updates = [tuple(map(int, input().strip().split())) for _ in range(m)]

results = longest_good_segment(n, heights, updates)
for result in results:
    print(result)

