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
The buil-in heap in Python is called "heapq":
```python
nums = [1, 2, 3, 4]
```


