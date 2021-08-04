## Trie
[Trie](https://en.wikipedia.org/wiki/Trie) is a tree datastructure that stores prefixes. In some cases, it can be used as a replacement of hashset. 

```python
class Node:
    def __init__(self):
        # each node has a dict. key is a letter, and val is another node.
        # each node represents a word or prefix
        self.children = {}
        self.isWord = False
        
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currNode = self.root
        for letter in word:
            if letter not in currNode.children:
                currNode.children[letter] = Node()
            currNode = currNode.children[letter]
        currNode.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currNode = self.root
        for letter in word:
            if letter in currNode.children:
                currNode = currNode.children[letter]
            else:
                return False
        return currNode.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currNode = self.root
        for letter in prefix:
            if letter in currNode.children:
                currNode = currNode.children[letter]
            else:
                return False
        return True
```
