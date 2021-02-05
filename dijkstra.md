Dijkstra's algorithm can be implemented with heap since it looks for the closest node to starting point at each iteration.
```python
        def dijkstra(start):
            # store the checked nodes, the values are the 
            # distance to starting point
            visited = {}
            
            # initialize a heap storing nodes and their distances
            # to the start node
            heap = [(float("inf"), i) for i in range(n) if i != start]
            heap.append((0, start))
            heapq.heapify(heap)

            # start dijkstra algorithm
            while heap:
                # current nearest node to start
                dist, node = heapq.heappop(heap)
                
                # simply remove the visited nodes from heap
                if node in checked_nodes: continue    
                
                # this is the SHORTEST path from start to node,
                # we will not visit this node in the future
                visited[node] = dist
                
                # edge relaxation
                for neighbor, weight in graph[node]:
                    if neibhor not in visited:
                        heapq.heappush(heap, (dist + weight, neighbor))
                
            return visited_nodes
```
