class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        """Prim's algorithm with heap"""
        # graph[0] is unused
        graph = [[] for _ in range(1 + n)] 
        
        # add the edge info to the graph
        for x, y, cost in connections:
            graph[x].append((y, cost))
            graph[y].append((x, cost))
            
        # visited and unvisited nodes, and visit node 1
        visited = set([1])
        unvisited = set([i for i in range(2, n + 1)])
        
        # add the edges of node 1 to heap
        edges = []
        for neighbor, cost in graph[1]:
            edges.append((cost, 1, neighbor))
        heapq.heapify(edges)
        
        # Prim's algorithm. During each iteration, we
        # connect current cut to the outside using the 
        # edge with minimum cost
        num_edges = 0
        total_cost = 0
        visited_edges = set()
        while edges:
            edge = heapq.heappop(edges)
            visited_edges.add(edge)
            cost, src, dst = edge
            # this edge is connecting current cut to 
            # its outside
            if src in visited and dst in unvisited:
                num_edges += 1
                total_cost += cost
                visited.add(dst)
                unvisited.remove(dst)
                # add the edges from dst to other nodes
                for neighbor, cost in graph[dst]:
                    new_edge = (cost, dst, neighbor)
                    if new_edge not in visited_edges:
                        heapq.heappush(edges, new_edge)
                    
        # check if a MST is formed
        if len(visited) == n and num_edges == n - 1:
            return total_cost
        else:
            return -1