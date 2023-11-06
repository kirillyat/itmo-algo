t = int(input().strip())
for _ in range(t):
   n = int(input().strip())
   p = list(map(int, input().strip().split()))
   stack = []
   for i in range(n-1, -1, -1):
       while stack and stack[-1] < p[i]:
           stack.pop()
       if stack and stack[-1] == p[i]:
           stack.insert(0, p[i])
       else:
           stack.append(p[i])
   print(' '.join(map(str, stack)))
