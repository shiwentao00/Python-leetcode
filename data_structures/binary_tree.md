# Binary Tree

### Recursive traversal
Reursive traversal of a binary tree is trivial DFS:
```python
    def dfs(node):
        # print(node.val)
        # pre-order traversal

        if node.left:
            dfs(node.left)

        # print(node.val)
        # in-order traversal

        if node.right:
            dfs(node.right)

        # print(node.val)
        # post-order traversal
```

### Iiterative pre-order traversal:
```python
    if not root:
        return None
    stack = [root]
    while stack:
        # pop stack first, pre-order
        node = stack.pop()
        print(node.val)
        # push right child first, so right child 
        # visited last
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
```

### Iiterative in-order traversal:
```python
    # Time complexity is O(H + N), where
    # H is heigh of tree and N is number of 
    # nodes.
    stack = []
    while stack or root:
        # keep pushing left node to stack
        while root:
            stack.append(root)
            root = root.left
        
        root = stack.pop()
        # in-order
        print(root.val)
        root = root.right
```

Another in-order traversal (not tested yet), it is essentially the same as the previous solution:
```python
def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = list()
        res = list()
        
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                curr = stack.pop()
                res.append(curr.val)
                root = curr.right
                
        return res
```

### Iiterative post-order traversal:
My method uses another visited hashset to keep track of visited nodes:
```python
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        
        stack = [root]
        res = []
        visited = set([root])
        while stack:
            top = stack[-1]
            # keep pushing left nodes to stack
            if top.left and top.left not in visited:
                stack.append(top.left)
                visited.add(top.left)
            # keep pushing right nodes to stack if there is
            # no left child
            elif top.right and top.right not in visited:
                stack.append(top.right)
                visited.add(top.right)
            # if there is no left and right child, or both children have
            # been visited, we can pop the stack. 
            else:
                # post order
                node = stack.pop()
                res.append(node.val)
                
        return res
```

Another method from Leetcode community, not tested:
```python
    def postorderTraversal(self, root):
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res
```

### Construct binary tree from inorder and posterorder
```python
```

### Construct binary tree from preorder and inorder
```python
```

### Construct binary tree from preorder and postorder
```python
```