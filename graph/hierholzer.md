# Hierholzer's Algorithm
Hierholzer's Algorithm is a graph traversal algorithm that traverse a graph in a **Eulerian Path**. A **Eulerian Path** is a trail in a finite graph that every edge is visited exactly once. The conditions for having a **Eulerian Path** (for directed graph) are:
* At most one vertex has outdegree - indegree = 1 (starting point)
* At most one vertex has indegree -outdegree = 1 (ending point)
* all other vertices have equal in- and outdegrees

## Implementation
The Hierholzer's Algorithm can be implemented as a post-order DFS. For each node in the recursive function, we pop out the edge that is visited. After all the edges of a node are traversed, this node is appended to the result. 
```python
from collections import defaultdict
graph = defaultdict(list)
edge_cnt = defaultdict(lambda: 0)
for a, b in edges:
	graph[a].append(b)
    edge_cnt[(a, b)] += 1
            
result = []
def dfs(node):
    # The Eulerian Path is actually a reversed postorder edge traversal 
	# of the graph, and each edge is visited exactly once.
    for nei in graph[node]:
        if edge_cnt[(node, nei)] > 0:
            edge_cnt[(node, nei)] -= 1
            dfs(nei)
    result.append(node)
    
dfs(start)

# If all the edges are traversed, the result is correct.
# Reversed(result) is the order we traverse the graph.
if len(result) == num_edges + 1:
	return reversed(result)
else:
	return None
```
The time complexity is the number of edges O(E).
## Example (Leetcode 332 - Reconstruct Itinerary)
This problem requires that the nodes are visited in lexical order, so we need to sort the destinations of each node:
```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Hierholzer's Algorithm
        
        # construct a graph and a counter for the edges
        from collections import defaultdict
        graph = defaultdict(list)
        edge_cnt = defaultdict(lambda: 0)
        for a, b in tickets:
            graph[a].append(b)
            edge_cnt[(a, b)] += 1
        
        # sort the neighbors the visiting order is lexical
        for node in graph:
            graph[node].sort()
        
        itinerary = []
        def dfs(node):
            # the itinerary is actually a reversed postorder traversal of the graph,
            # and each edge is visited exactly once
            for nei in graph[node]:
                if edge_cnt[(node, nei)] > 0:
                    edge_cnt[(node, nei)] -= 1
                    dfs(nei)
            itinerary.append(node)
            
        dfs("JFK")
        
        return reversed(itinerary)
```
