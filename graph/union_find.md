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

    # compress the path while looking for root
    def find(self, x):
        if x == self.parent[x]:
            return x
        # recursively make all nodes on the path
        # to be root's children
        self.parent[x] = find(self.parent[x])
        return self.parent[x]

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

### Example Problems
    1. Leetcode examples: LC 547

### Complexity Analysis for Variations of Disjoint-set
The table below shows the time complexity of different variations, where N is the number of nodes.
| Method | constructor | find | union | connected |   
| --- | --- | --- | --- | --- |      
| Quick Find | O(N) | O(1) | O(N) | O(1) |   
| Quick Union | O(N) | O(logN), O(N) worst case | O(N) worst case | O(N) worst case |   
| Union by Rank | O(N) | worst case O(logN) | worst case O(logN) | worst case O(logN) |    
| Path Compression | O(N) | O(logN), O(N) worst case | O(logN), O(N) worst case | O(logN), O(N) worst case |    
| Union by Rank with Path Compression | O(N) | O(&alpha(N)) | O(&alpha(N)) | O(&alpha(N)) |     


1. Only using ```quick find```. This variation optimizes the ```find``` method by using a ```root``` array to store the roots of each node. 
2. Only using ```quick union```. This variation uses array ```parent``` instead of ```root```. In this case, the ```find``` method has to climb up the tree to the root, and the worst case is where the tree is a linked list with a time complexity of O(N).
3. Only using ```union by rank```. This variation uses an other array ```rank``` to store the heights of the trees. During the ```union``` operation, the root of the higher tree is always the root of unioned tree. The worst case is where each ```union``` operation unions two trees of the same height, and the time complexity is O(1 + logN) = O(logN).
4. Only using ```path compression```. This variation improves the ```find``` method such that all nodes on the path are connected to their root directly as their parent. The average time for ```find``` is O(logN), which is the height of the tree. The worst case is where the tree is a linked list, and time is O(N).
5. Use ```union by rank``` + ```path compression```. This is the final optimized form of Union-find. The time complexity is O(&alpha(N)), where &alpha(N) is called [Inverse Ackermann Function](https://en.wikipedia.org/wiki/Ackermann_function), which can be treated as constant time.