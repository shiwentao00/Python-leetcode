# Python cheat sheet
Python cheat sheet for daily work and coding interveiws for those not good at memorizing.

### About Python
* [Yield](https://github.com/Wentao-Shi/Python-cheat-sheet/blob/main/python_yield.md)
* [Reference copy](https://github.com/Wentao-Shi/Python-cheat-sheet/blob/main/python_reference_copy.md)
* [Division](https://github.com/Wentao-Shi/Python-cheat-sheet/blob/main/python_division.md)
* [XOR](https://github.com/Wentao-Shi/Python-cheat-sheet/blob/main/python_xor.md)
* [Infinity](https://github.com/Wentao-Shi/Python-cheat-sheet/blob/main/python_infinity.md)

### Data Structures
* [Built-in hashset](https://github.com/Wentao-Shi/Python-cheat-sheet/blob/main/built_in_hashset.md)
* [Built-in hashmap](https://github.com/Wentao-Shi/Python-cheat-sheet/blob/main/built_in_hashmap.md)
* [Built-in string](https://github.com/Wentao-Shi/Python-cheat-sheet/blob/main/built_in_string.md)
* [Using the heapq API](https://github.com/Wentao-Shi/Python-cheat-sheet/blob/main/using_heapq.md)

### Algorithms
* [Built-in sorting](https://github.com/Wentao-Shi/Python-cheat-sheet/blob/main/built_in_sort.md)


### Tricks
* [Connected chain](https://github.com/Wentao-Shi/Python-cheat-sheet/blob/main/trick_connected_chain.md)






### ASCII value of a character
```python
acsii_c = ord('c') # convert to ascii value
char_c = chr(acsii_c) # convert back to character
```

### Class variable and instance variable
```python
class Shark:
    animal_type = "fish" # class variable
    def __init__(self, name, age):
        self.name = name # can be acessed from outside
        age = age # can NOT be acessed from outside
```
### Tree
Insert a tree node with value val:
```python
node.left = TreeNode(val)
or 
node.right = TreeNode(val)
```

Delete a leaf node, node:
```python
node = None
```

### Linked-list 
Insert a dummy head node
```python
dummy = listNode(-1)
dummy.next = head
```


### Array
Initiliaze a 2d-array, m * n --> m rows  n columns
```python
2d_array = [[0] * n for _ in range(m)]  
```





