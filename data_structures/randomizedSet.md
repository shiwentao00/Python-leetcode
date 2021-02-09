### Randomized Set
This is a problem from Leetcode 380. The randomized set data structure offers O(1) insertion, O(1) deletion, and O(1) time to return a random content. It is very useful in samling algorithms like Markov chain Monte Carlo. Hashset offers O(1) insertion and deletion, but it does not offer random access, so we need to convert the set into list first, which is O(N). List provides O(1) insertion, O(1) random access, but deletion is O(N). Here we can improve the list with hashmap to get the job done.   

The idea is to use the list as main data container. We maintain the indices of contents use another hashmap. Upon deleting, we swap the element to delete with the last element, and delete it. Then we update the previous last element's index. The whole oeprtion takes O(1) time. Below is the implementation:
```python
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.indices = {}        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.indices:
            return False
        self.data.append(val)
        self.indices[val] = len(self.data) - 1
        return True
    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.indices:
            return False
        val_idx = self.indices[val]
        # swap val with last element
        self.data[val_idx], self.data[-1] = self.data[-1], self.data[val_idx]
        # update the indices table
        self.indices[self.data[val_idx]] = val_idx
        # remove last element
        self.data.pop()
        # remove val from indices table
        self.indices.pop(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        i = random.randint(0, len(self.data) - 1)
        return self.data[i]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```