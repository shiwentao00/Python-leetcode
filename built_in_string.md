# String

### String is immutable, so the variable is re-assigned when doing this:
```python
a = "abc"
a += "d"
```
### If you want to do a lot of string concatenation, it is better to convert it into a list first:
```python
s = "abcd"
s = list(s)
s.append("e")
```
### To convert the char list back to string, use the ```join``` function:
```python
s = "".join(s) 
```

### To break up a string from a specified seperator and return a list of string:
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
