def main():
    n, m = list(map(int, input().split()))
    prefs = [0]
    for n in map(int, input().split()):
        prefs.append(prefs[-1]+n)
    for _ in range(m):
        a, b = list(map(int, input().split()))
        print(prefs[b]-prefs[a-1])
    
main()