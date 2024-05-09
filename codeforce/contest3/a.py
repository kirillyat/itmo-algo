S = input()
N = int(input())
for _ in range(N):
    l1, r1, l2, r2 = map(int, input().split())
    l1-=1
    l2-=1
    if r1 - l1 != r2 - l2:
        print("No")
        continue
    if l1 == l2 and r1 == r2:
        print("Yes")
        continue

    if S[l1:r1] != S[l2:r2]:
        print("No")
    else:
        print("Yes")
