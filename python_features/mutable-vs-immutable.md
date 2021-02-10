### Mutable vs Immutable

The value of some objects can change. Objects whose value can change are said to be mutable; objects whose value is unchangeable once they are created are called immutable.

Some of the mutable data types in Python are list, dictionary, set and user-defined classes. On the other hand, some of the immutable data types are int, float, decimal, bool, string, tuple, and range.

## Example: Tuple vs List Expanding
Now, we can try to expand our list and tuple using the += operator. This will operation work for both data types. Let’s see what will happen.

```python
list_values = [1, 2, 3]
set_values = (1, 2, 3)
print(id(list_values))
print(id(set_values))
print()

list_values += [4, 5, 6]
set_values += (4, 5, 6)
print(id(list_values))
print(id(set_values))
```

output:
```python
2450343168136
2450343205552

2450343168136
2450341742248
```
We can see that the list identity is not changed, while the tuple identity is changed. This means that we have expanded our list, but created a completely new tuple. Lists are more memory efficient than tuples.

## Example: int

```python
number = 42
print(id(number))

number += 1
print(id(number))
```
output
```python
1657696608
1657696640
```
## Example: string
```python
text = "Data Science"
print(id(text))

text += " with Python"
print(id(text))
```
output
```python
2450343168944
2450343426208
```
We see that both for the number and text variables, their identity is changed. This means that new variables are created in both cases.

```python
```
