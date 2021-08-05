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
The difference of this implementation is that when partitioning the array to find the pivot, we do it in-place, which saves some space. In addtion, we always compare the index of pivot, so we don't have to recalculate k during the recursion.
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k + 1
        k_idx = k - 1
        
        def partition(left, right):
            """return a pivot index"""
            pivot = nums[right]
            
            # write pointer
            write_p = left
            
            # swap numbers <= pivot to left, and
            # numbers > pivot to right
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[write_p], nums[i] = nums[i], nums[write_p]
                    write_p += 1
                    
            # swap the pivot number to the correct position
            nums[write_p], nums[right] = nums[right], nums[write_p]
            
            return write_p
        
        def quickSelect(left, right, k_smallest_idx):
            """return the kth smallest element"""
            pivot_idx = partition(left, right)
            if pivot_idx == k_smallest_idx:
                return nums[pivot_idx]
            elif pivot_idx > k_smallest_idx:
                return quickSelect(left, pivot_idx - 1, k_smallest_idx)
            else:
                return quickSelect(pivot_idx + 1, right, k_smallest_idx)
            
        random.shuffle(nums)
        return quickSelect(0, len(nums) - 1, k_idx)
```
