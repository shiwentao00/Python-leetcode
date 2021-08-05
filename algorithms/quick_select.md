## Quick Select
The Quick Select is similar to Quick Sort. It is used to find the kth largest/smallest element in an array. The average time complexity is O(N), because it is O(N + N/2 + N/4 + ...) = O(2N). The worst case time is O(N^2) when the array is already sorted.

### Easy implementation
This implementation is easy to come up with and code, but not efficient interms of space:
```python
def quickSelect(nums, k_smallest):
	"""returns kth smallest element in nums"""
	# shuffle nums before calling the function to avoid worst case
	pivot = nums[-1]
	left = [x for x in nums[0:-1] if x <= pivot]
	right = [x for x in nums[0:-1] if x > pivot]
            
    if len(left) == k_smallest - 1:
    	return pivot
	elif len(left) > k_smallest - 1:
    	return quickSelect(left, k_smallest)
	else:
		return quickSelect(right, k_smallest - len(left) - 1)
```

### More efficient implementation and Leetcode 215: keth largest number in an array
```python
```
