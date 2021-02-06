## Hashset

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
Union of sets:
```python
A = {'a', 'c', 'd'}
B = {'c', 'd', 2 }
C = {1, 2, 3}

print('A U B =', A.union(B))
print('B U C =', B.union(C))
print('A U B U C =', A.union(B, C))
print('A.union() =', A.union())
```
Union using the | operator
```python
A = {'a', 'c', 'd'}
B = {'c', 'd', 2 }
C = {1, 2, 3}

print('A U B =', A| B)
print('B U C =', B | C)
print('A U B U C =', A | B | C)
```
