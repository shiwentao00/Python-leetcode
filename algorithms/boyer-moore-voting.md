### Boyer-Moore Majority Voting Algorithm
This algorithm can find the majority member (appears more than n/2 times) in a list when it is guaranteed that there is a majority member. Time complexity is O(N) and space complexity is O(1). This problem comes from Leetcode 169.   

```python
    def majorityElement(self, nums: List[int]) -> int:
        """majority vote"""
        cnt = 0
        candidate = None
        for x in nums:
            if cnt == 0:
                candidate = x
                cnt += 1
            else:
                if x == candidate:
                    cnt += 1
                else:
                    cnt -= 1
                    
        return candidate
```