


def main():
    s = []
    for _ in range(int(input())):
        cmd, v = list(map(int, input().split()))
        if cmd == 1:
            while s and (s[-1][0] != min and s[-1][1]<v or s[-1][0] != max and s[-1][1]>v):
                s.pop()
        elif cmd == 2:
            while s and (s[-1][0] != max and s[-1][1]>v or s[-1][0] != min and s[-1][1]<v):
                s.pop()
        elif cmd == 3:
            for f, a in s:
                v = f(a,v)
            print(v)
#main()
def main():
    s = []
    for _ in range(int(input())):
        cmd, v = list(map(int, input().split()))
        if cmd == 1:
            s.append(('max', v))
            while s and (s[-1][0] != 'min' and s[-1][1] < v or s[-1][0] != 'max' and s[-1][1] > v):
                s.pop()
        elif cmd == 2:
            s.append(('min', v))
            while s and (s[-1][0] != 'max' and s[-1][1] > v or s[-1][0] != 'min' and s[-1][1] < v):
                s.pop()
        elif cmd == 3:
            for f, a in s:
                if f == 'max':
                    v = max(a, v)
                elif f == 'min':
                    v = min(a, v)
            print(v)

main1()

