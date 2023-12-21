MOD = 10**9 + 7

def count_numbers(K, S):

    dp = [[0] * (S+1) for _ in range(K+1)]

    dp[0][0] = 1

    for i in range(1, K+1):
        for j in range(S+1):

            for k in range(0, min(j, 9)+1):
                dp[i][j] += dp[i-1][j-k]
                dp[i][j] %= MOD

    return dp[K][S]

K, S = map(int, input().split())

print(count_numbers(K, S))