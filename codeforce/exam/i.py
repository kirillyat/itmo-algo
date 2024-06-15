class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def contains(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def count_unique_concatenations(s, t):
    trie = Trie()
    unique_combined_strings = set()

    for i in range(1, len(s) + 1):
        trie.insert(s[:i])
    
    for i in range(1, len(t) + 1):
        prefix_t = t[:i]
        node = trie.root
        temp_str = ""
        for char in s:
            temp_str += char
            if valid_prefix(node, char):
                combined_str = temp_str + prefix_t
                unique_combined_strings.add(combined_str)
            node = node.children.get(char)
            if not node:
                break
    
    return len(unique_combined_strings)

def valid_prefix(node, char):
    return char in node.children

s = input().strip()
t = input().strip()

result = count_unique_concatenations(s, t)
print(result)