# Bellman-ford Algorithm
This post is a summarization of [this Leetcode tutorial](https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3864/). The Bellman-ford Algorithm solves the problems of finding the length of shortest path in a weighted graph, where the weights can be negative, but no negative cycle is allowed.

## Theorems
Theorem 1: In a “graph with no negative-weight cycles” with N vertices, the shortest path between any two vertices has at most N-1 edges.   
Theorem 2: In a “graph with negative weight cycles (sum of weights on the cycle is negative)”, there is no shortest path.

## Dynamic Programming Approach
First, we can develop a dynamic programming algorithm (with state compression) as a naive version fo Bellman-ford. Basically, we define a dp table, where dp[i][j] is the minimum distance to node j using at most i edges. According to theorem 1, there are at most N - 1 edges on the shortest path if it exists, the the number of rows of the dp table is N. During the process of dynamic programming, we only need row i and row i - 1, so we end up with only two rows.

## Bellman-ford Algorithm Approach
Bellman-for alorithm is an optimized dynamic programming approach. We only have one dp array called ```distance```, which stores the current shortest path of each node to starting point. We iterate over the edges, and update the distances greedily. The idea is that during the dp, we can update dp[i][j] according to dp[i][k], if there is an edge from k to j. This is actually updating the next row(s) in advance, but it does not affect the final results.   

Note: if the problem asks you to find the shortest path within k edges, you need to use the naive dp approach.

### Complexity
Time Complexity: we iterate through all the vertices, and in each iteration, we'll perform a relaxation operation for each appropriate edge. Therefore, the time complexity would be O(V⋅E).

Space Complexity: O(V). We use two arrays of length V. One to store the shortest distance from the source vertex using at most k-1 edges. The other is to store the shortest distance from the source vertex using at most k edges.

### Detecting negative cycles
Although the “Bellman-Ford algorithm” cannot find the shortest path in a graph with “negative weight cycles”, it can detect whether there exists a “negative weight cycle” in the “graph”.

Detection method: After relaxing each edge N-1 times, perform the Nth relaxation. According to the “Bellman-Ford algorithm”, all distances must be the shortest after relaxing each edge N-1 times. However, after the Nth relaxation, if there exists distances[u] + weight(u, v) < distances(v) for any edge(u, v), it means there is a shorter path . At this point, we can conclude that there exists a “negative weight cycle”.

## Shortest Path Faster Algorithm (SPFA)
The SPFA algorithm is an improved version of Bellman-ford. In the BF algorithm, for each iteration, we traverse the edges using arbitrary order. In fact, the order of the edges matters. So, in SPFA, the order of edge traversal is optimized using a queue. Only when the shortest distance of a vertex is relaxed and that the vertex is not in the “queue”, we add the vertex to the queue. We iterate the process until the queue is empty. At this point, we have calculated the minimum distance from the given vertex to any vertices.

### Complexity
Upper bound time is still O(V⋅E), however, the the time is optimized. 

Space Complexity: O(V)O(V). We need to store VV vertices.

## Implementation
### Naive Bellman-ford Algorithm
The Naive Bellman-ford Algorithm is useful to solve the minimum distance problem under the restriction of "using at most k edges". It solves Leetcode ```787. Cheapest Flights Within K Stops```.
```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """Naive Bellman-ford"""
        start, end = src, dst
        # construct a graph, graph[i] is a tuple (src, price)
        graph = [[] for _ in range(n)]
        for src, dst, price in flights:
            graph[dst].append((src, price))
            
        # dp_prev[i] is the min cost of using at most number of edges - 1 to get i from start
        # dp[i] is the min cost of using at most the number of edges used to get i from start
        dp_prev = [float('inf')] * n
        dp_prev[start] = 0
        dp = [float('inf')] * n
        dp[start] = 0

        # at most n - 1 edges on the shortest path, and k + 1 <= n - 1
        # (k stops -> k + 1 edges)
        # each iteration, we increase the most number of edges to use by 1
        for _ in range(k + 1):
            for node in range(n):
                #if node == start:
                #    continue
                for src, price in graph[node]:
                    dp[node] = min(dp[node], dp_prev[src] + price)
            dp_prev = dp
            dp = [float('inf')] * n
            dp[start] = 0
        
        if dp_prev[end] < float('inf'):
            return dp_prev[end]
        else:
            return -1
```

### Optimized Bellman-ford Algorithm
The optimized version update the rows of dp table greedily so that the problem may be solved within < than n - 1 iterations. But it cannot solve the problem with k-edge restriction. Example: 743. Network Delay Time.
```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """Bellman-ford"""
        start = k
        # shortest[i] is the shortest time from start to node i
        shortest = [float('inf')] * (n + 1)
        shortest[start] = 0
            
        # if shortest not changed for a iteration, algorithm has finished
        changed = False
        # at most n - 1 iterations
        for _ in range(n - 1):
            for src, dst, time in times:
                #shortest[dst] = min(shortest[dst], shortest[src] + time)
                if shortest[src] + time < shortest[dst]:
                    shortest[dst] = shortest[src] + time
                    changed = True
            if not changed:
                break
                
        max_time = max(shortest[1:])
        if max_time < float('inf'):
            return max_time
        else:
            return -1
```

### Shortest Path Faster Algorithm (SPFA)
Further optimize the Bellman-ford algorithm to reduce redundant computation. The key is the order of the edges. Example: 743. Network Delay Time.
```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """Shortest Path Faster Algorithm (SPFA)"""
        shortest = [float('inf')] * (n + 1)
        shortest[k] = 0
        q = collections.deque([k])
        graph = [[] for _ in range(n + 1)]
        for src, dst, time in times:
            graph[src].append((dst, time))
        
        while q:
            node = q.popleft()
            for dst, time in graph[node]:
                new_dist = shortest[node] + time
                if new_dist < shortest[dst]:
                    shortest[dst] = new_dist
                    # only add the node to the q when the distance is updated
                    q.append(dst)
                    
        max_time = max(shortest[1:])
        if max_time < float('inf'):
            return max_time
        else:
            return -1
```