from typing import List

def meteorCollision(meteors: List[int]) -> List[int]:
        stack = []
        sign = lambda x: x/abs(x)
        for a in meteors:
            if stack and sign(stack[-1]) > sign(a):
                while stack and sign(stack[-1]) > sign(a):
                    t = stack[-1]
                    if abs(a)<abs(t):
                        break 
                    if abs(a)==abs(t): 
                        stack.pop()
                        break
                    if abs(a)>abs(t):
                        stack.pop()
                        if stack and sign(stack[-1]) > sign(a):
                            continue
                        stack.append(a)
                        break
            else:
                stack.append(a)

        return stack


def main():
    n = int(input())
    arr = map(int, input().split())
    result = meteorCollision(arr)
    print(len(result))
    for i in result:
        print(i, end=' ')

main()