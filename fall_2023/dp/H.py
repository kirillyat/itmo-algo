def levenshtein_distance(s1, s2):
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    
    for i in range(len(s1) + 1):
        dp[i][0] = i
    for j in range(len(s2) + 1):
        dp[0][j] = j
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            substitution_cost = 0 if s1[i-1] == s2[j-1] else 1
            
            dp[i][j] = min(
                dp[i-1][j] + 1,                  
                dp[i][j-1] + 1,                  
                dp[i-1][j-1] + substitution_cost 
            )
    
    return dp[-1][-1]

s1 = input()
s2 = input()

print(levenshtein_distance(s1, s2))