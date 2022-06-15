# Bucket Sort
Bucket sort is a sorting algorithm that distributes the numbers into buckets, then process each bucket seperately. In some problems, it can achieve O(N) time, which is better than comparison-based sorting's O(NlogN). For example, we can have an array ```buckets```, where ```buckets[i]``` is a list of all elements with frequency i. In this way, we can solve these two problems in O(N) time:
1. Leetcode 347 - Top K frequent element
2. Leetcode 692 - Top K frequent words

## Algorithm
```
count the frequencies

an array ```buckets```, where ```buckets[i]``` is a list of all elements with frequency i

for each list in reversed(buckets)
    find the elements
```