## Hashmap
### Dictionary
Hashmap is implemented as dictionary in Python:
```python
a = {}
```
To add an item:
```python
a[1] = 2
```
To remove an item by key:
```python
a.pop(1) # remove key 1
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

### Defaultdict
The defaultdict class is the same as a dictionary, except that it never raises valueError. 
```python
# Define a function to return a default 
# value for keys that is not present 
def def_value(): 
    return "not valid key"
      
# Defining the dict 
d = collections.defaultdict(def_value) 
d["a"] = 1
d["b"] = 2
  
print(d["a"]) 
print(d["b"]) 
print(d["c"]) 
```
If we want the deafaultdict to use empty list/set as default, we can initialize by passing the list/set function:
```python
d1 = collections.defaultdict(list)
d2 = collections.defaultdict(set)
```
