class AhoCorasick:
    def __init__(self, patterns):
        self.trie = {0: {}}
        self.fail = {}
        self.output = {}
        self.build_trie(patterns)
        self.build_aho_corasick()

    def build_trie(self, patterns):
        node_id = 1
        for pattern in patterns:
            current_node = 0
            for char in pattern:
                if char not in self.trie[current_node]:
                    self.trie[current_node][char] = node_id
                    self.trie[node_id] = {}
                    self.fail[node_id] = 0
                    self.output[node_id] = []
                    node_id += 1
                current_node = self.trie[current_node][char]
            self.output[current_node].append(pattern)

    def build_aho_corasick(self):
        queue = []
        for char, child in self.trie[0].items():
            self.fail[child] = 0
            queue.append(child)

        while queue:
            current_node = queue.pop(0)
            for char, child in self.trie[current_node].items():
                queue.append(child)
                fail_state = self.fail[current_node]
                while fail_state != 0 and char not in self.trie[fail_state]:
                    fail_state = self.fail[fail_state]
                if char in self.trie[fail_state]:
                    self.fail[child] = self.trie[fail_state][char]
                else:
                    self.fail[child] = 0
                self.output[child].extend(self.output[self.fail[child]])

    def count_occurrences(self, text):
        current_node = 0
        occurrences = []
        for i, char in enumerate(text):
            while current_node != 0 and char not in self.trie[current_node]:
                current_node = self.fail[current_node]
            if char in self.trie[current_node]:
                current_node = self.trie[current_node][char]
            else:
                current_node = 0
            if self.output[current_node]:
                for pattern in self.output[current_node]:
                    occurrences.append(i - len(pattern) + 1)
        return occurrences

def solve(s, t, queries):
    results = []
    for l1, r1, l2, r2 in queries:
        sub_s = s[l1-1:r1]
        sub_t = t[l2-1:r2]
        aho = AhoCorasick([sub_s])
        occurrences = aho.count_occurrences(sub_t)
        results.append(len(occurrences))
    return results




if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    q = int(input().strip())
    queries = []
    
    for _ in range(q):
        l1, r1, l2, r2 = map(int, input().strip().split())
        queries.append((l1, r1, l2, r2))
    
    results = solve(s, t, queries)
    for result in results:
        print(result)

