# Traverse all paths between two vertices
We can use DFS to traverse all paths between two vertices on a graph. It is actually backtracking. Below is the solution for Leetcode 797: All Paths From Source to Target.   

## Implementation
```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """List all paths from node 0 to node n - 1."""
        n = len(graph)
        
        def backtrack(node, path):
            if node == n - 1:
                result.append(path.copy())
                return
            
            for child in graph[node]:
                path.append(child)
                backtrack(child, path)
                path.pop()
                
        result = []
        backtrack(0, [0])
        return result
```

Note that in this problem the graph is a Directed Acyclic Graph (DAG), which means that we don't need to check for loops. If the graph is not a DAG, we should only enumerate the asyclic paths, since there will be infinite number of cyclic paths. A further optimization is that we can use another hashset to store the path, such that searching a node in path takes only ```O(1)```.

```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """List all (acyclic) paths from node 0 to node n - 1."""
        n = len(graph)
        
        def backtrack(node, path):
            if node == n - 1:
                result.append(path.copy())
                return
            
            for child in graph[node]:
                if child not in path:
                    path.append(child)
                    backtrack(child, path)
                    path.pop()
                
        result = []
        backtrack(0, [0])
        return result
```

## Complexity
If the graph is a DAG, the time and space complexities are ```O(2<sup>N</sup>⋅N)```. Otherwise, the lose upper bound of the algorithm is O((V−1)!), considering a fully-connected graph.