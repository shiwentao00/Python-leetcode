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
An implementation that is easy to understand and memorize:
```python
def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        inorder = []
        
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                inorder.append(root.val)
                root = root.right # do NOT add if root.right!!!!!
                
        return inorder
```

Another implementation:
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
        root = root.right # do NOT add if root.right!!!!!
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

### Construct binary tree from preorder and inorder
The method below is trick but easy to understand. The build method is a reursive pre-order traveral of the binary tree. Therefore, the order of builing nodes is exactly pre-order, so we can use a global pre_idx to select current node from the preorder list.
```python
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        pre_idx = 0
        
        # find index of an element in inorder in O(1)
        in_indices = {val: key for key, val in enumerate(inorder)}
        
        def build(in_start, in_end):
            nonlocal pre_idx
            
            # root node
            root_val = preorder[pre_idx]
            root = TreeNode(val=root_val)
            
            in_idx = in_indices[root_val]
            
            # the build method is a pre-order recursive
            # traveral, so we just need to increase the 
            # index of preorder one by one.
            pre_idx += 1
            
            # left sub-tree
            if in_idx > in_start:
                root.left = build(in_start, in_idx - 1)
            
            # right sub-tree
            if in_idx < in_end:
                root.right = build(in_idx + 1, in_end)
            
            return root
        
        return build(0, len(preorder) - 1)
```

### Construct binary tree from inorder and posterorder
The key here is that the reverse of postorder is actully a preorder in (root->right->left). With this observation, we can use the same method when constructing from preorder and inorder.
```python
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        
        post_idx = len(postorder) - 1
        
        # find inorder index in O(1)
        in_indices = {val: key for key, val in enumerate(inorder)}
        
        def build(in_start, in_end):
            nonlocal post_idx
            root_val = postorder[post_idx]
            root = TreeNode(val=root_val)
            
            # index of the root in inorder
            root_in_idx = in_indices[root_val]
            
            post_idx -= 1
            
            # build right subtree
            if root_in_idx < in_end:
                root.right = build(root_in_idx + 1, in_end)
            
            # build left subtree
            if root_in_idx > in_start:
                root.left = build(in_start, root_in_idx - 1)
            
            return root
        
        return build(0, len(inorder) - 1)
```

### Construct binary tree from preorder and postorder
The solution below passed the test of Leetcode 889, but is not elegant enough. O(N) time. None that preorder and postorder arrays can not determine the binary tree. For example, pre = [1, 2, 4, 5], post = [4, 5, 2, 1]. In this solution, we always construct the subtree as left subtree when we can construct on either side.
```python
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        post_indices = {val: i for i, val in enumerate(post)}
        
        def helper(pre_s, pre_e, post_s, post_e):
            root_val = pre[pre_s]
            root = TreeNode(val=root_val)
            length = pre_e - pre_s + 1
            if length == 1:
                return root
            
            # construct left subtree
            left_root_val = pre[pre_s + 1]
            left_post_e = post_indices[left_root_val]
            left_post_s = post_s
            left_pre_s = pre_s + 1
            left_pre_e = left_post_e - left_post_s + left_pre_s
            root.left = helper(left_pre_s, left_pre_e, left_post_s, left_post_e)
            
            # construct right subtree
            right_root_val = post[post_e - 1]
            # if right root == left root, don't need to construct
            # right subtree. (there are multiple answers in this case)
            if right_root_val != left_root_val:
                right_post_e = post_e - 1
                right_post_s = left_post_e + 1
                right_pre_s = left_pre_e + 1
                right_pre_e = pre_e
                root.right = helper(right_pre_s, right_pre_e, right_post_s, right_post_e)
                
            return root
        
        return helper(0, len(pre) - 1, 0, len(post) - 1)
```

This is Leetcode's solution. However, this solution taks O(N^2) time, because it uses linear search to find index.
```python
    def constructFromPrePost(self, pre, post):
        def make(i0, i1, N):
            if N == 0: return None
            root = TreeNode(pre[i0])
            if N == 1: return root

            # L = post.index(pre[1]) + 1
            for L in xrange(N):
                if post[i1 + L - 1] == pre[i0 + 1]:
                    break

            root.left = make(i0 + 1, i1, L)
            root.right = make(i0 + L + 1, i1 + L, N - 1 - L)
            return root

        return make(0, 0, len(pre))
```
