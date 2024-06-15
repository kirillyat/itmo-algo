def count_palindromic_substrings(s):
    def preprocess(s):
        t = '#'.join(f'^{s}$')
        return t

    t = preprocess(s)
    n = len(t)
    p = [0] * n
    center = right = 0

    for i in range(1, n - 1):
        if i < right:
            p[i] = min(right - i, p[2 * center - i])

        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1

        if i + p[i] > right:
            center, right = i, i + p[i]

    count = 0
    for k in p:
        count += (k + 1) // 2

    return count


s = input()
print(count_palindromic_substrings(s)-len(s))

