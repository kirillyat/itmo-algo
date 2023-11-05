def max_palindrome_length(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    max_length = 1  # Начальное значение максимальной длины палиндрома

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

            max_length = max(max_length, dp[i][j])

    return max_length

# Чтение входных данных
n = int(input())
s = input()

# Вычисление максимальной длины подстроки-палиндрома
result = max_palindrome_length(s)
print(result)
