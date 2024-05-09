import sys
from collections import deque


class Automata:
    def __init__(self):
        self.nodes = [self.Node()]
        self.size = 0

    class Node:
        def __init__(self):
            self.next = [0] * 26
            self.terminant = []
            self.sLink = 0
            self.ssLink = 0

    def add(self, s):
        cur = 0
        for char in s:
            nextC = ord(char) - ord("a")
            if self.nodes[cur].next[nextC] == 0:
                self.nodes.append(self.Node())
                self.nodes[cur].next[nextC] = len(self.nodes) - 1
            cur = self.nodes[cur].next[nextC]
        self.nodes[cur].terminant.append(self.size)
        self.size += 1

    def build(self):
        q = deque([0])
        while q:
            cur = q.popleft()
            for i in range(26):
                if self.nodes[cur].next[i] == 0:
                    if cur == 0:
                        self.nodes[cur].next[i] = 0
                    else:
                        self.nodes[cur].next[i] = self.nodes[
                            self.nodes[cur].sLink
                        ].next[i]
                else:
                    next = self.nodes[cur].next[i]
                    if cur == 0:
                        self.nodes[next].sLink = 0
                    else:
                        self.nodes[next].sLink = self.nodes[self.nodes[cur].sLink].next[
                            i
                        ]
                        self.nodes[next].ssLink = (
                            self.nodes[self.nodes[next].sLink].ssLink
                            if len(self.nodes[self.nodes[next].sLink].terminant) == 0
                            else self.nodes[next].sLink
                        )
                    q.append(next)

    def findOccur(self, t):
        occur = [False] * self.size
        found = [False] * len(self.nodes)
        cur = 0
        for char in t:
            cur = self.nodes[cur].next[ord(char) - ord("a")]
            tmp = cur

            while not found[tmp]:
                for ends in self.nodes[tmp].terminant:
                    occur[ends] = True

                found[tmp] = True
                tmp = self.nodes[tmp].ssLink

        return occur


# Main function
def main():

    n = int(input())
    automata = Automata()

    for _ in range(n):
        s = input().strip()
        automata.add(s)

    t = input().strip()
    automata.build()

    ans = automata.findOccur(t)
    for an in ans:
        print("YES" if an else "NO")


if __name__ == "__main__":
    main()
