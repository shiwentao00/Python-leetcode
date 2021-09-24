# Hierholzer's Algorithm
Hierholzer's Algorithm is a graph traversal algorithm that traverse a graph in a **Eulerian Path**. A **Eulerian Path** is a trail in a finite graph that every edge is visited exactly once. The conditions for having a **Eulerian Path** (for directed graph) are:
* At most one vertex has outdegree - indegree = 1 (starting point)
* At most one vertex has indegree -outdegree = 1 (ending point)
* all other vertices have equal in- and outdegrees

## Implementation
The Hierholzer's Algorithm can be implemented as a post-order DFS. For each node in the recursive function, we pop out the edge that is visited. After all the edges of a node are traversed, this node is appended to the result. 
```python
graph = collections.defaultdict(list)
        
for src, dst in edges:
	graph[src].append(dst)
            
	for key in graph.keys():
		graph[key].sort(reverse=True)

	result = []
	def dfs(node):
		while graph[node]:
			# we pop this destination because we don't visit
			# it anymore.
			dst = graph[node].pop()
        	dfs(dst)
			
		# post-order traversal
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
for key in graph.keys():
	graph[key].sort(reverse=True)
```
