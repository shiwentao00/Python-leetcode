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

Heap elements can be tuples. This is useful for assigning comparison values (such as task priorities) alongside the main record being tracked:
```
>>> h = []
>>> heappush(h, (5, 'write code'))
>>> heappush(h, (7, 'release product'))
>>> heappush(h, (1, 'write spec'))
>>> heappush(h, (3, 'create tests'))
>>> heappop(h)
(1, 'write spec')
```
The second element in the tuple will be sorted as well:
```python
a = [(1, 3),(2,5), (3, 0),(2, 1), (1,2), (1,4), (3, -1)]
heapq.heapify(a)
while a:
    print(heapq.heappop(a))
```
```
(1, 2)
(1, 3)
(1, 4)
(2, 1)
(2, 5)
(3, -1)
(3, 0)
```
