

import heapq

def main():
    h = [i for i in range(1, 100000)]
    heapq.heapify(h)
    P = dict()
    for _ in range(int(input())):
        s, n = input().split()
        n = int(n)
        if s == '-':
            heapq.heappush(h,P[n])
            del P[n]
        else:
            P[n] = heapq.heappop(h)
            print(P[n])

main()