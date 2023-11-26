brackets = {
    '}': '{',
    ']': '[',
    ')': '('
}

def check(s: str)->bool:
    stack = []
    for c in s:
        if c in brackets.keys():
            if stack and stack.pop() == brackets[c]:
                continue
            return False
        else:
            stack.append(c)
    return len(stack)==0

def main():
    if check(input()):
        print("YES")
    else:
        print("NO") 
main()