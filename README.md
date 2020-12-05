# Python cheat sheet
Python cheat sheet for daily work and coding interveiws for those not good at memorizing.

### Sorting
To sort in-place:
```python
a = [2, 1, 3]
a.sort()
a.sort(reverse=True)
```
To return a sorted list:
```python
x = sorted(a)
x = sorted(a, reverse=True)
```

### Hashset
Hashset in Python is implemented as ```set()```:
```python
a = set([1, 2, 3])
```
To add, remove, and empty the set:
```python
a.add(4)
a.remove(3)
a.clear()
```
Hashset is iterable,
```python
for x in a:
    print(x)
```
but it is not indexable. To index a hashset, convert it to list first:
```python
list(a)[0]
```

### Hashmap
Hashmap is implemented as dictionary in Python:
```python
a = {}
```
To add an item:
```python
a[1] = 2
```
To iterate over key-value pairs:
```python
for k, v in a.items():
    print(k, v)
```
To iterate over keys or values:
```python
for k in a.keys():
    print(k)
for v in a.values():
    print(v)
```

### Replicating a list
There are two ways to replicate a list. If the elements are immutable, we can do:
```python
a = [0] * 1000
```
However, if the elements are mutable, all the replications will be the same reference of the origianl elements. In this case, we need to use list comprehension:
```python
a = [set() for _ in range(1000)]
```

### Copy a list
To make a copy instead of creating reference:
```python
a = [1, 2, 3]
b = a.copy()
b = a[:] # using slicing of entire array
b = a[0:2] # slicing creates shallow copy
```

### Reverse a list
To reverse in-place:
```python
a= [1, 2, 3]
a.reverse()
```
T return a copy of reversed list, use slicing:
```python
b = a[::-1]
```


### Division
There are two kinds of division:
```python
a // b # round down, even for negative number
a / b # round to zero, for both positive and negative numbers
```

### XOR
```python
a ^ b
```

### Infinity
```python
a = float('inf')
b = float('-inf')
```

### String
String is immutable, so the variable is re-assigned when doing this:
```python
a = "abc"
a += "d"
```

### Heap
The buil-in heap in Python is called "heapq", it implements min heap:
```python
import heapq
nums = [1, 2, 3, 4]
heapq.heapify(nums) # in-place
heapq.heappop(nums)
heapq.heappush(nums, x)
```
To implement max heap, simply negate all the numbers in nums:
```python
nums = [-1* x for x in nums]
heapq.heapify(nums)
```

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

### The infinity value
```python
inf = float('inf')
-inf = float('-inf')
```
