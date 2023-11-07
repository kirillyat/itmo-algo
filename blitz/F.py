

def main():
    s = []
    for _ in range(int(input())):
        cmd, v = list(map(int, input().split()))
        s.append(((lambda x,y: x), ))
        a = True
        if cmd == 1: #max
            while s:
                if s[-1][0] == max and s[-1][1] <= v:
                    s.pop()
                if s[-1][0] == min and s[-1][1] <= v:
                    s.clear()
                    s.append(((lambda x,y: y), v))
                    a = False
                    break
                if s[-1][0] == min and s[-1][1] > v:
                    break
                if s and s[-1][0] == max and s[-1][1] >= v:
                    a = False
                    break
                break
            if a:
                s.append((max, v))
        elif cmd == 2: #min
            while s:
                if s[-1][0] == max and s[-1][1] <= v:
                    break
                if s[-1][0] == min and s[-1][1] <= v:
                    a = False
                    break
                if s[-1][0] == min and s[-1][1] > v:
                    s.pop()
                if s and s[-1][0] == max and s[-1][1] >= v:
                    s.clear()
                    s.append(((lambda x,y: y), v))
                    a = False
                    break
                break
            if a:
                s.append((min, v))

        elif cmd == 3:
            for f, a in s:
                v = f(v,a)
            print(v)

def main_():
   s = []
   for _ in range(int(input())):
        cmd, v = list(map(int, input().split()))
        if cmd == 1: #max
            while s and s[-1][0] < v:
                s.pop()
            if not s or s[-1][0] < v:
                s.append((v, ))
        elif cmd == 2: #min
            while s and s[-1][0] > v:
                s.pop()
            if not s or s[-1][0] > v:
                s.append((v, ))
        elif cmd == 3:
             print(max(s)[0] if s else 0)
main_()


