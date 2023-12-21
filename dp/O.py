def min_items_for_exact_weight(n, s, weights):
    dp = [[float('inf')] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = 0 

    for i in range(1, n + 1):
        for j in range(s + 1):
            if weights[i - 1] <= j:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + 1)
            else:
                dp[i][j] = dp[i - 1][j]

    min_items = dp[n][s] if dp[n][s] != float('inf') else 0

    return min_items

n, s = map(int, input().split())
weights = list(map(int, input().split()))

min_items = min_items_for_exact_weight(n, s, weights)

print(min_items)