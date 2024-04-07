from typing import Tuple


class SingleManager:
    def __init__(
        self,
    ) -> None:
        self.stack = []
        self.min = 0

    def open(self, i: int):
        self.stack.append(i)

    def close(self, i: int):
        if self.stack:
            self.stack.pop(-1)+1
        else:
            self.min = i

    def low(self) -> int:
        if self.stack:
            return self.stack[-1]
        return self.min



class TripleManager:
    def __init__(self) -> None:
        self.ans = 0
        self.n = 1
        self.managers = []
    
    def process1(self, s: str) -> Tuple[int, int]:
        self.ans = 0
        self.n = 1

        self.manager = SingleManager()

        for i, c in enumerate(s):
            if c == ')':
                self.manager.close(i+1)
            elif c == '(':
                self.manager.open(i+1)
          

            cur = i+1 - self.manager.low()
            if cur > 0 and cur == self.ans:
                self.n += 1
            if cur > self.ans:
                self.ans = cur
                self.n = 1
        return self.ans, self.n

    def process(self, s: str) -> Tuple[int, int]:
        self.ans = 0
        self.n = 1

        self.managers = [SingleManager(), SingleManager(), SingleManager()]

        for i, c in enumerate(s):
            if c == ')':
                self.managers[0].close(i+1)
            elif c == '(':
                self.managers[0].open(i+1)
            elif c == '}':
                self.managers[1].close(i+1)
            elif c == '{':
                self.managers[1].open(i+1)
            elif c == ']':
                self.managers[2].close(i+1)
            elif c == '[':
                self.managers[2].open(i+1)

            cur = min([i+1 - m.low() for m in self.managers])
            if cur > 0 and cur == self.ans:
                self.n += 1
            if cur > self.ans:
                self.ans = cur
                self.n = 1
        return self.ans, self.n


print(*TripleManager().process1(input()))
