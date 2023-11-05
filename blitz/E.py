from heapq import *
from collections import Counter

n = int(input())
candies = list(map(int, input().split()))

freq = Counter(candies)
queue = []

for value in freq.values():
    heappush(queue, -value)

answer = 0

while len(queue) > 0:
    curr = -heappop(queue)
    if curr > 2:
        curr -= 2
        answer += 2
        heappush(queue, -curr)
    elif curr == 2:
        answer += 1

print(answer)
