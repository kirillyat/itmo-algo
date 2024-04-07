
n, t = map(int, input().split())
queue = []
events = reversed(list(map(int, input().split())))
D = set()

for event in events:
    if event not in D:
        D.add(event)
        queue.append(event)
for i in range(n, 0, -1):
    if i not in D:
        queue.append(i)


# В итоге queue содержит порядок людей в очереди после всех событий
print(*reversed(queue))