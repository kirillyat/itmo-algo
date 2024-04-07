def count_sequences(N):

    if N == 1:
        return 2 
    dp = [[0, 0] for _ in range(N)]
    
    dp[0][0] = 1
    dp[0][1] = 1

    for i in range(1, N):
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
        dp[i][1] = dp[i - 1][0]
    
    return dp[N - 1][0] + dp[N - 1][1]

N = int(input())

print(count_sequences(N))