## Union Find
Union Find, or Disjoint-set is a graph data structure that stores information about connected components. During the process of forming graph, it dynamically connects nodes. The pseudo code is as follow:
```
Initialize all nodes to point to themselves only

for each edge:
    src_root, dst_root = find(src), find(dst)
    if src_root ! = dst_root:
        union(src_root, dst_root)
```
The time complexity of Union Find will be O(E * alpha(n)), where E is number of edges, and alpha(n) is called [Inverse Ackerman Function](https://en.wikipedia.org/wiki/Ackermann_function#Inverse), which has output less than 5 for any pratical input number. So, the overall time complexity is still O(E). As can be seen from the actual implementation, we can implement `find` with O(1) time by `path compression`,  and `union` with O(alpha(n)) time. Below is the Python solution for Leetcode 323:
```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Union Find, O(E), where E is number of edges
        """
        # initially all nodes are connected to themselves
        parent = list(range(n))
        # store the sizes of trees to form balanced trees
        sizes = [1] * n
        # number of independent components
        cnt = n
        
        def find(node):
            """
            Find the root parent of the node.
            """
            while parent[node] != node:
                # node compression, reduce the depth of tree by
                # connecting the node to its grandparent
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(x, y):
            """
            Connect node x and y by connect their root parents.
            """
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                # always connect smaller tree to root of larger tree
                if sizes[root_x] >= sizes[root_y]:
                    parent[root_y] = root_x
                    sizes[root_x] += sizes[root_y]
                else:
                    parent[root_x] = root_y
                    sizes[root_y] += sizes[root_x]
                nonlocal cnt
                cnt -= 1
                    
        for src, dst in edges:
            union(src, dst)
        
        # note that the elements in parent array are not all roots,
        # so we can NOT get number of groups by len(set(parent))
        return cnt
``` 