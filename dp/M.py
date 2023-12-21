def can_achieve_exact_weight(n, s, weights):
    dp = [False] * (s + 1)
    dp[0] = True
    for weight in weights:
        for j in range(s, weight - 1, -1):
            if dp[j - weight]:
                dp[j] = True
                
    return dp[s]

n, s = map(int, input().split())
weights = list(map(int, input().split()))

result = can_achieve_exact_weight(n, s, weights)

print("YES" if result else "NO")