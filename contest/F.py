n = int(input())
s = []
q = []
for _ in range(n):
    cmd = input().split()
    if cmd[0]=='+':
        q.append(int(cmd[1]))

    if cmd[0]=='-':
        q.pop(0)
