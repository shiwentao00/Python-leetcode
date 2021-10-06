"""API for a min heap"""

def __heapify_node(nums, index):
    """Makes the input node a heap in-place."""
    left_child = index * 2 + 1
    right_child = index * 2 + 2

    if left_child < len(nums) and nums[left_child] < nums[index]:
        smallest = left_child
    else:
        smallest = index

    if right_child < len(nums) and nums[right_child] < nums[smallest]:
        smallest = right_child

    if index != smallest:
        nums[index], nums[smallest] = nums[smallest], nums[index]
        __heapify_node(nums, smallest)


def heapify(nums):
    # find the first index of last row
    i = 0
    while i * 2 + 1 < len(nums):
        i = i * 2 + 1

    # we don't need to heapify last row 
    for i in range(i - 1, -1, -1):
        __heapify_node(nums, i)


def heappop(nums):
    """Removes heap top."""
    nums[0], nums[-1] = nums[-1], nums[0]
    top = nums.pop()
    __heapify_node(nums, 0)
    return top


def heappush(nums, x):
    """Insert a new element into heap"""
    nums.append(x)
    index = len(nums) - 1
    parent = int((index - 1) / 2)
    # keep bubbling up until it forms a heap
    while nums[index] < nums[parent]:
        __heapify_node(nums, parent)
        index = parent
        # we want to ROUND TO ZERO
        parent = int((index - 1) / 2)


if __name__ == '__main__':
    nums = [2,3,5,1,-1,-3, 9, 1,-4]
    heapify(nums)
    print(nums)
    while nums:
        #print(heappop(nums))
        heappop(nums)
    heappush(nums, 1)
    heappush(nums, -2)
    heappush(nums, 0)
    heappush(nums, 3)
    heappush(nums, 9)
    heappush(nums, 6)
    heappush(nums, -3)
    heappush(nums, -4)
    print(nums)
    
    print('-----------------------')
    import heapq
    nums = [2,3,5,1,-1,-3, 9, 1,-4]
    heapq.heapify(nums)
    print(nums)
    while nums:
        #print(heapq.heappop(nums))
        heapq.heappop(nums)
    heapq.heappush(nums, 1)
    heapq.heappush(nums, -2)
    heapq.heappush(nums, 0)
    heapq.heappush(nums, 3)
    heapq.heappush(nums, 9)
    heapq.heappush(nums, 6)
    heapq.heappush(nums, -3)
    heapq.heappush(nums, -4)
    print(nums)