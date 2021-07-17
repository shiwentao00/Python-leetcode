# BFS
Some special cases of BFS.

### LC 45. Jump Game II
Here, we perform BFS on the array. The reaching range of each level is the nodes of next level.
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        # BFS solution
        start, end = 0, 0
        
        level_size = 0
        while end < len(nums) - 1:
            next_level_start, next_level_end = end, end
            for i in range(start, end + 1):
                next_level_end = max(next_level_end, i + nums[i])
            
            # it may happens that there's no way to proceed to next level 
            # when step sizes are 0
            if next_level_end > end:
                next_level_start = end + 1
                
            
            # update level
            start = next_level_start
            end = next_level_end
            level_size += 1
            
        return level_size
```
