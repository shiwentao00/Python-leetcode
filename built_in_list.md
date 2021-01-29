# list

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

### Swap two values in a list
To swap two values in a list:
```python
a[left], a[right] = a[right], a[left]
```

### Delete an item from a list
```python
a = [1, 2, 3, 4, 5]
a.pop() # pop last item, O(1) time
a.pop(i) # delete item at index i, O(N) amortized time because of shifting
```
