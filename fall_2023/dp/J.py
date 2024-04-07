def find_largest_square(matrix):
    n, m = len(matrix), len(matrix[0])
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_side = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if matrix[i - 1][j - 1] == 1:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])
    
    return max_side

N, M = map(int, input().split())
troops = [list(map(int, input().split())) for _ in range(N)]

max_square_side = find_largest_square(troops)


print(max_square_side)