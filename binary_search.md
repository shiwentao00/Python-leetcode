
## Binary Search
Binary search performs search on a sorted array with O(logN) time. There are two templates for binary search.

Template 1, basic binary search, searching closed intervals of [left, right] for cases where we don't need access to <em>mid</em> index's neighbor.
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

Template 2, searching open intervals of (left, right), so we can safely access nums[mid - 1] and nums[mid + 1]. Need to evaluate nums[left] and nums[right] after the while loop ends.
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    # length of search range is least 3
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            ## can safely access nums[mid - 1], nums[mid + 1] here
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid
    
    # post-process left and right
    if nums[left] == target:
        return left
    elif nums[right] == target:
        return right
    
    return -1
```
