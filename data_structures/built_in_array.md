
# Array

### Initiliaze a 2d-array, m * n --> m rows  n columns
```python
2d_array = [[0] * n for _ in range(m)]  
```

### matrix (m,n), get matrix size
```python
a=[[1,2,5],[3,4,7]]
m = len(a)
n = len(a[0])
print(m, n)
```
output is
```python
2 3
```

### matrix (m,n), get j-th column 
e.g., get the 2nd column
```python
a=[[1,2,5],[3,4,7]]
m = len(a)
n = len(a[0])
print([a[i][2] for i in range(m)])
```
output is
```python
[5, 7]
```
