## Topological Sort
Topological Sort algorithm finds a global order for all nodes in a directed acyclic graph (DAG). It is often used in applications to schedule tasks or detect loops in a DAG. The idea is simple: we keep removing the nodes with 0 indegree, until there is no removable nodes.

```python
class Node:
	def __init__(self):
		self.indegree = 0
		self.outnodes = []
		
def topoSort(numNodes, edges):
	# construct a graph, there are other ways to construct a graph,
	# such as using a dictionary
	nodes = [None] * numNodes
	for i in range(numNodes):
		nodes[i] = Node()
	for dst, src in edges:
		nodes[dst].indegree += 1
		nodes[src].outnodes.append(nodes[dst])
		
	# find the nodes with indegree = 0
	canRemove = []
	for node in nodes:
		if node.indegree == 0:
			canRemove.append(node)
			
	# sort
	removed = [] # this list has the sorted nodes
	while canRemove:
		# you can also pop at the left side,
		# there can be multiple correct sorted order
		node = canRemove.pop() 
		removed.append(node)
		for nei in node.neighbors:
			nei.indegree -= 1
			if nei.indegree == 0:
				canRemove.append(nei)
										
	# do something with removed to get your answer
```

Note: topological sort can also be applied to Undirected graphs. In this case, the nodes to be removed should have degree of 1. Example: Leetcode 310 - Minimum Height Trees.
