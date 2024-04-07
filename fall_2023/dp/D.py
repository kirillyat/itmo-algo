def turtle_path(n, m, coins):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    dp[0][0] = coins[0][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + coins[0][j]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + coins[i][0]
    
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + coins[i][j]
    
    path = []
    i, j = n-1, m-1
    while i > 0 or j > 0:
        if i == 0:
            j -= 1
            path.append('R')
        elif j == 0:
            i -= 1
            path.append('D')
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i -= 1
                path.append('D')
            else:
                j -= 1
                path.append('R')
    return dp[n-1][m-1], ''.join(reversed(path))


N, M = map(int, input().split())
coins = [list(map(int, input().split())) for _ in range(N)]

max_coins, path = turtle_path(N, M, coins)
print(max_coins)
print(path)