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

To sort a dictionary:
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

### Heap
The buil-in heap in Python is called "heapq", it implements min heap:
```python
import heapq
nums = [1, 2, 3, 4]
heapq.heapify(nums) # in-place, O(N) time
heapq.heappop(nums)
heapq.heappush(nums, x)
```
To access the top of the heap, use 0 index:
```python
heap_top = nums[0]
```
The nlargest() function of the Python module heapq returns the specified number of largest elements from a Python iterable like a list, tuple and others.
```python
iterable = [6,1,7,9,3,5,4]
k = 3

# O(nlogk + klogk) time, maintain a heap of size k, iterate over the list n times.
# The result is sorted reversely in the end, which is O(klogk).
# Equivalent to: sorted(iterable, key=key, reverse=True)[:k] (or [0:k]).
largests = heapq.nlargest(k, iterable) 
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

