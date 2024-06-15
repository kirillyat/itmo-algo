
def main():
    s = input().strip()
    t = input().strip()
    hash_pos = len(s)
    s = s + "#" + t + "$"
    n = len(s)
    m = n
    p, c = [], [0]*n
    
    # k = 0
    a = [[] for _ in range(28)]
    alpha = "$abcdefghijklmnopqrstuvwxyz#"
    
    for i in range(n):
        pos = alpha.find(s[i])
        a[pos].append(i)
    
    for i in range(28):
        for j in range(len(a[i])):
            p.append(a[i][j])
            if i + j == 0:
                c[p[0]] = 0
            else:
                c[p[-1]] = c[p[-2]] + (j == 0)
    
    k = 0
    while (1 << k) < n:
        a = [[] for _ in range(n)]
        for j in range(n):
            i = (p[j] - (1 << k) + n) % n
            a[c[i]].append((c[p[j]], i))
        
        p = []
        for i in range(n):
            for j in range(len(a[i])):
                p.append(a[i][j][1])
                if i + j == 0:
                    c[p[0]] = 0
                else:
                    c[p[-1]] = c[p[-2]] + (j == 0 or a[i][j][0] != a[i][j-1][0])
        k += 1
    
    k = 0
    lcp = [0] * n
    for i in range(n - 1):
        pos = c[i]
        j = p[pos - 1]
        while s[i + k] == s[j + k]:
            k += 1
        lcp[pos] = k
        k = max(k - 1, 0)
    
    res = 0
    s_res = ""
    
    fc = [False] * n
    for i in range(n):
        fc[i] = p[i] < hash_pos
    
    for i in range(2, n):
        if fc[i] != fc[i-1]:
            if res < lcp[i]:
                res = lcp[i]
                s_res = s[p[i]:p[i]+lcp[i]]
    
    print(s_res)


if __name__ == "__main__":
    main()