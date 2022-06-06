# Singly-linked list
## Leetcode 206 reverse linked list
```python
# recursive solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        def reverse(node):
            if not node.next:
                return node
            
            tail = reverse(node.next)
            
            node.next.next = node
            node.next = None # remove head's next link
            
            return tail
        
        return reverse(head)
```
```python
# iterative solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
```

# Doubly-linked list