# Python cheat sheet
Python cheat sheet for daily work and coding interveiws for those not good at memorizing.

## About Python

## Data Structures
* [Using the heapq API](https://github.com/Wentao-Shi/Python-cheat-sheet/blob/main/using_heapq.md)
## Algorithms
* [Built-in sorting](https://github.com/Wentao-Shi/Python-cheat-sheet/blob/main/built_in_sort.md)
* [Built-in hashset](https://github.com/Wentao-Shi/Python-cheat-sheet/blob/main/built_in_hashset.md)



### Hashmap
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

a = math.inf
b = - math.inf  # no need to import math
```

### String
String is immutable, so the variable is re-assigned when doing this:
```python
a = "abc"
a += "d"
```
If you want to do a lot of string concatenation, it is better to convert it into a list first:
```python
s = "abcd"
s = list(s)
s.append("e")
```
To convert the char list back to string, use the ```join``` function:
```python
s = "".join(s) 
```

To break up a string from a specified seperator and return a list of string:
```python
text= 'Love thy neighbor'
# splits at space
print(text.split()) =>(print as) ['Love', 'thy', 'neighbor']

grocery = 'Milk, Chicken, Bread'
# splits at ','
print(grocery.split(', ')) => (print as) ['Milk', ' Chicken', ' Bread']
```

### Binary addition on strings of 1 and 0
```python
a, b = "11", "1" # binary numbers as string
s, c = int(a, 2), int(b, 2) # convert to integer with base 2 (3, 1).

# bit manipulation to implement addition
while c != 0:
    s, c = s ^ c, (s & c) << 1 
    
return bin(s)[2:] # convert to binary with bin function, need to remove first two characters "0b".
return "{0:b}".format(s) # or we can convert inteter directy to string with format() by specifying binary.
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
### Array
Initiliaze a 2d-array, m * n --> m rows  n columns
```python
2d_array = [[0] * n for _ in range(m)]  
```
### Python reference copy
List, dictionary is mutable.
String, tuple is immutable.
Use list as an example:
```python
a.append(b.copy()) (when b will change)
or
a.append(b[:]) (when b will change)
```

### Mod
When you want to design a chain that connect 0,1,..9 as a circle, you can use % 10.
```python
-1 % 10 = 9
```

### Python yeild
The yield statement suspends function’s execution and sends a value back to the caller, but retains enough state to enable function to resume where it is left off. When resumed, the function continues execution immediately after the last yield run. This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.
```python
def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
  
# Driver code to check above generator function 
for value in simpleGeneratorFun():  
    print(value) 
```
```
Output:
1
2
3
```
