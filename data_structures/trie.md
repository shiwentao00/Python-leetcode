## Trie
[Trie](https://en.wikipedia.org/wiki/Trie) is a tree datastructure that stores prefixes. In some cases, it can be used as a replacement of hashset. This doc is a summarization of [this Leetcode tutorial](https://leetcode.com/explore/learn/card/trie/147/basic-operations/1048/).

### Complexity Compared with Hashtable
Time Complexity:   
1. The time complexity to search in hash table is typically O(1), but will be O(logN) in the worst time if there are too many collisions and we solve collisions using height-balanced BST.   
2. The time complexity to search in Trie is O(M), where M is the height of the Trie, or the longest word in Trie.   

Space Complexity:   
1. The space complexity of hash table is O(M * N).
2. The upper bound space complexity of Trie is also O(M * N), but it is always much samller than hashtables in practice.   

### Implementation
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
