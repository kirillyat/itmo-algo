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
            self.stack.pop(-1)
        else:
            self.min = i

    def min(self):
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
        self.managers = []

    def process(self, s: str) -> int:
        self.ans = 0
        self.managers = [SingleManager(), SingleManager(), SingleManager()]

        for i, c in enumerate(s):
            if i in "()":
                self.managers[0].process(i, c)
            if i in "{}":
                self.managers[1].process(i, c)
            if i in "[]":
                self.managers[2].process(i, c)

            self.ans = max(self.ans, max([m.min() for m in self.managers]))
        return self.ans


print(TripleManager().process(input()))
