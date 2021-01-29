
## Binary Search
Binary search performs search on a sorted array with O(logN) time. There are two templates for binary search.

Template 1, basic binary search, for cases where we don't need access to <em>mid</em> index's neighbor.
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
