import sys

def build_suffix_array(s):
    s = s + chr(0)
    n = len(s)
    alphabet = 256

    count = [0] * max(n, alphabet)
    permutation = [0] * n
    classes = [0] * n

    for ch in s:
        count[ord(ch)] += 1
    for i in range(1, alphabet):
        count[i] += count[i - 1]
    for i in range(n):
        count[ord(s[i])] -= 1
        permutation[count[ord(s[i])]] = i

    num_classes = 1
    classes[permutation[0]] = 0
    for i in range(1, n):
        if s[permutation[i]] != s[permutation[i - 1]]:
            num_classes += 1
        classes[permutation[i]] = num_classes - 1

    npm = [0] * n
    nclasses = [0] * n
    j = 0
    while (1 << j) < n:
        len_shift = 1 << j
        for i in range(n):
            npm[i] = permutation[i] - len_shift
            if npm[i] < 0:
                npm[i] += n
        count[:num_classes] = [0] * num_classes
        for index in npm:
            count[classes[index]] += 1
        for i in range(1, num_classes):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            count[classes[npm[i]]] -= 1
            permutation[count[classes[npm[i]]]] = npm[i]

        nclasses[permutation[0]] = 0
        num_classes = 1
        for i in range(1, n):
            current_tuple = (classes[permutation[i]], classes[(permutation[i] + len_shift) % n])
            previous_tuple = (classes[permutation[i - 1]], classes[(permutation[i - 1] + len_shift) % n])
            if current_tuple != previous_tuple:
                num_classes += 1
            nclasses[permutation[i]] = num_classes - 1
        classes = nclasses[:]
        j += 1

    return permutation[1:], s[:-1] 

def kasai_lcp(s, permutation):
    n = len(permutation)
    rank = [0] * n
    for i, perm in enumerate(permutation):
        rank[perm] = i

    h = 0
    res = [0] * (n - 1)
    for i in range(n):
        if rank[i] > 0:
            j = permutation[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            res[rank[i] - 1] = h
            if h > 0:
                h -= 1
    return res

def main():
    data = input().strip()
    
    suffix_array, s = build_suffix_array(data)
    lcp = kasai_lcp(s, suffix_array)

    print(" ".join(str(x+1) for x in suffix_array))
    print(" ".join(str(x) for x in lcp))

if __name__ == "__main__":
    main()
