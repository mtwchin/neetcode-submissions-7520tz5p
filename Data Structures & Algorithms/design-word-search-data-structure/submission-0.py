class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        # k is the iterator lives through recursive calls
        def dfs(root, k):
            node = root
            for i in range(k, len(word)):
                char = word[i]
                if char == '.':
                    for child in node.children.values():
                        if dfs(child, i+1):
                            return True
                    return False
                else: # for regular chars
                    if char not in node.children:
                        return False
                    node = node.children[char]
            return node.isEndOfWord
        return dfs(self.root, 0)
            