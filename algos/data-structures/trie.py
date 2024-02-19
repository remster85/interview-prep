class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

# Example usage:

trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("cherry")

print(trie.search("apple"))  # True
print(trie.search("banana"))  # True
print(trie.search("cherry"))  # True
print(trie.search("dog"))  # False

print(trie.starts_with("app"))  # True
print(trie.starts_with("ban"))  # True
print(trie.starts_with("che"))  # True
print(trie.starts_with("do"))  # False