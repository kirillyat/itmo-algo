def prefix_function(s):
    n = len(s)
    pi = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

def kmp_search(p, t):
    pi = prefix_function(p + '#' + t)
    m = len(p)
    res = []
    for i in range(m + 1, len(pi)):
        if pi[i] == m:
            res.append(i - 2*m+1)
    return res

# Считываем входные данные
p = input().strip()
t = input().strip()

# Находим вхождения строки p в строку t
positions = kmp_search(p, t)

# Выводим результат
print(len(positions))
print(" ".join(map(str, positions)))