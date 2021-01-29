# Built-in sorting of Python

## To sort in-place:
```python
a = [2, 1, 3]
a.sort()
a.sort(reverse=True)
```
## To return a sorted list:
```python
x = sorted(a)
x = sorted(a, reverse=True)
```

## To sort a dictionary:
```python
a = {'d':4, 'a':1, 'c':3, 'b':2}
b = sorted(a.items(), key=lambda x: x[1]) # by value
c = sorted(a.items(), key=lambda x: x[0]) # by key
```
output:
```
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
```
