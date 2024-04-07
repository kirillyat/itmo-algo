MOD = 10**9 + 7

K, S = map(int, input().split())

dp = [[0] * (S + 1) for _ in range(K + 1)]
dp[0][0] = 1  

for i in range(1, K + 1):
    for s in range(S + 1):
        for digit in range(10):
            if s - digit >= 0:  
                dp[i][s] = (dp[i][s] + dp[i - 1][s - digit]) % MOD

print(dp[K][S])