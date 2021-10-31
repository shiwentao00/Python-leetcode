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

A more efficient quick sort which sorts the array in-place:
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(left, right):
            pivot = nums[right]
            wp = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[wp], nums[i] = nums[i], nums[wp]
                    wp += 1
            nums[wp], nums[right] = nums[right], nums[wp]
            return wp
            
        def quick_sort(left, right):
            pivot = partition(left, right)
            
            if pivot > left:
                quick_sort(left, pivot - 1)
                
            if pivot < right:
                quick_sort(pivot + 1, right)
        
        random.shuffle(nums)
        quick_sort(0, len(nums) - 1)
        return nums
```

## Merge Sort
Merge sort breaks the array into units of length 1, then combine them with sorted order.
```python
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print(myList)
```

Note that merge sort is very suitable for linked list (Leetcode 148). It is very natural and simple to merge two sorted linked lists.
```python
class Solution(object):
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next
    
        tail.next = h1 or h2
        return dummy.next
    
    def sortList(self, head):
        if not head or not head.next:
            return head
    
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return self.merge(*map(self.sortList, (head, slow)))
```
## Heap Sort
