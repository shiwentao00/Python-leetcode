## Union Find
Union Find, or Disjoint-set is a graph data structure that stores information about connected components. During the process of forming graph, it dynamically connects nodes. The pseudo code is as follow:
```
Initialize all nodes to point to themselves only

for each edge:
    src_root, dst_root = find(src), find(dst)
    if src_root ! = dst_root:
        union(src_root, dst_root)
```
The time complexity of Union Find will be O(E * alpha(n)), where E is number of edges, and alpha(n) is called [Inverse Ackerman Function](https://en.wikipedia.org/wiki/Ackermann_function#Inverse), which has output less than 5 for any pratical input number. So, the overall time complexity is still O(E). As can be seen from the actual implementation, we can implement `find` with O(1) time by `path compression`,  and `union` with O(alpha(n)) time. 
```python
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

    # doing path compression while looking for root
    def find(self, x):
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

        # decrease the number of connected components by one
        # here if needed

    def connected(self, x, y):
        return self.find(x) == self.find(y)
``` 

Leetcode examples: LC 547