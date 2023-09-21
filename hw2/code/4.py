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
            self.stack.pop(-1) + 1
        else:
            self.min = i

    def low(self) -> int:
        if self.stack:
            return self.stack[-1]
        return self.min

    def process(self, i: int, c: str):
        if c in "({[":
            self.open(i)
        else:
            self.close(i)


class TripleManager:
    def __init__(self) -> None:
        self.ans = 0
        self.n = 1
        self.managers = []

    def process(self, s: str) -> Tuple[int, int]:
        self.ans = 0
        self.n = 1

        self.managers = [SingleManager(), SingleManager(), SingleManager()]

        for i, c in enumerate(s):
            if c in "()":
                self.managers[0].process(i, c)
            if c in "{}":
                self.managers[1].process(i, c)
            if c in "[]":
                self.managers[2].process(i, c)

            cur = min([i - m.low() for m in self.managers])
            if cur > 0 and cur == self.ans:
                self.n += 1
            if cur > self.ans:
                self.ans = cur
                self.n = 1
        return self.ans, self.n


print(TripleManager().process(input()))
