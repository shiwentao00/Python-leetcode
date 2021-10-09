class Solution:
    """Solution of Leetcode 1135. Connecting Cities With Minimum Cost"""
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        """Kruskal's algorithm with Union-find"""
        
        # sort the edges according to the cost
        connections.sort(key=lambda x: x[2])
        
        # construct Union-find, index 0 is not used
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        # find with path compression
        def find(x):
            if parent[x] == x:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]
        
        # union by rank
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_x] = root_y
                rank[root_y] += 1
        
        # Krukal's alorithm to greedily add edges
        connected_nodes = set()
        num_edges = 0
        total_cost = 0
        for x, y, cost in connections:
            root_x, root_y = find(x), find(y)
            # if x and y have the same root, adding
            # this edge forms a cycle
            if root_x == root_y:
                continue
                
            union(x, y)
            total_cost += cost
            connected_nodes.add(x)
            connected_nodes.add(y)
            num_edges += 1
        
        # check if an MST is formed
        if len(connected_nodes) == n and num_edges == n - 1:
            return total_cost
        else:
            return -1