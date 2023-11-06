
def main():
   s = []
   for _ in range(int(input())):
       cmd, v = list(map(int, input().split()))
       if cmd == 1: #max
           while s:
               if s[-1][0](v, s[-1][1]) == v:
                  s.pop()
               else:
                  break
           else:
               s.append((max, v))
       elif cmd == 2: #min
           while s:
               if s[-1][0](v, s[-1][1]) == v:
                  s.pop()
               else:
                  break
           else:
               s.append((min, v))
       elif cmd == 3:
           for f, a in s:
               v = f(v, a)
           print(v)
main()