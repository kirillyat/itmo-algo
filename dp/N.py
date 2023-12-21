def knapsack(weights, n, s):
    dp = [[0 for j in range(s + 1)] for i in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if weights[i - 1] <= j: 
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + weights[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    
    max_weight = dp[n][s]
    items_chosen = []
    j = s
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            items_chosen.append(weights[i - 1])
            j -= weights[i - 1]
    
    return max_weight, items_chosen

n, s = map(int, input().split())
weights = list(map(int, input().split()))

max_mass, chosen_items = knapsack(weights, n, s)

print(max_mass)
print(len(chosen_items))
print(" ".join(map(str, chosen_items)))