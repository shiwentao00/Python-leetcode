### Floyd Warshall's Algorithm
This algorithm solves the "All Pairs Shortest Path" problem on graph. It can find the shortest path between all pairs of nodes. The time complexity is O(V^3), so it generally works for small graphs. It can also detect negative cycles (can keep cycling to reduce cost when edge weight is negative).   

This algorithm basically is implemented by dynamic programming. Let A be the adjacency matrix with distances. dp is a (n by n by n) memo table, where dp[k][i][j] = shortest path form i to j routing through nodes {0, 1,..., k - 1, k}. We initialize dp as the adjacency matrix:
```python
    dp = [[float("inf")] * n for _ in range(n)]
    for src, dst, weight in edges:
        dp[src][dst] = weight
        dp[dst][src] = weight
    for i in range(n):
        dp[i][i] = 0
```

Then for the recurrence relation, we can compute the shortest path as follow: 
```python    
    for k in range(n):
        for i in range(n):
            for j in range (n):
                dp[k][i][j] = min(dp[k - 1][i][j], dp[k - 1][i][k], dp[k - 1][k][j])
    return dp[n - 1]
```

One trick here is that dp[k] only depends on dp[k - 1], so we can reduce the memory from O(V^3) to O(V^2). In this case, we only need a 2-d dp array:
```python
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
```
    