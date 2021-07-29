# Sorting Algorithms
Templates of some classical sorting algorithms

## Quick Sort
The quick sort adopts the paradigm of divide-and-conquer. During each recursion, a random element is selected as the "pivot" number, and the array is divided into 3 parts: the pivot, the elements less than or equal to the the pivot, and the elements larger than the pivot. Repeat this recursively and the array will be sorted in O(NlogN) time. Note that if the array is already sorted, it becomes the worse case, O(N^2) time. To prevent this, we can always shuffle the array (O(N) time) before sorting.

```python
def quickSort(nums):
  pivot = nums[-1]
  left, right = [], []
  for x in nums[0:-1]:
    if x <= pivot:
      left.append(x)
    else:
      right.append(x)
    
  return quickSort(left) + [pivot] + quickSort(right)
```

## Merge Sort

## Heap Sort
