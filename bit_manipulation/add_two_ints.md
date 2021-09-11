## Add two (signed) integers
Bit-manipulation can be used to implement integer addition without using + and - operators. See Leetcode 371.
```python
def getSum(self, a: int, b: int) -> int:
    # make sure a dominates the sign
    x, y = abs(a), abs(b)
    if x < y:
        return self.getSum(b, a)
    
    # compute sign
    if a > 0:
        sign = 1
    elif a < 0:
        sign = -1
    else:
        return b
    
    # if a and b have the same sign, then its addition
    if a * b >= 0:
        while y:
            # sum without carry
            s = x ^ y
            # carry
            carry = (x & y) << 1
            # keep adding sum and carry
            x, y = s, carry
    
    # if a and b have different signs, then its subtraction
    elif a * b < 0:
        while y:
            # difference without borrow
            d = x ^ y
            # borrow
            borrow = (~x & y) << 1
            # keep substracting borrowed from the difference
            x, y = d, borrow
            
    return sign * x
```