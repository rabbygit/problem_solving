import heapq
from typing import List

# Edge
class Edge:
    def __init__(self, point1: int, point2: int, cost: int) -> None:
        self.point1 = point1
        self.point2 = point2
        self.cost = cost
        
    def __lt__(self, other):
        return self.cost < other.cost

# Disjoint set for track root node of a node
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    # kruskal algorithm
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # using kruskal's algorithm to find minimum spanning tree
        size = len(points)
        count = size - 1
        min_cost = 0
        priority_queue = []
        uf = UnionFind(size)

        # calculate weight/cost for every possible edges
        for i in range(size):
            for j in range(i+1, size):
                x1 , y1 = points[i]
                x2 , y2 = points[j]
                # calculate distance between two points
                cost = abs(x1 - x2) + abs(y1 - y2)
                edge = Edge(i, j, cost)
                priority_queue.append(edge)

        # represent the edges in the priority queqe
        heapq.heapify(priority_queue)

        # construct the minimum spaning tree using kruskal algo
        # steps:
        # 1. take the minimum cost edge
        # 2. connect the vertex using the selected adge if they can't form a cycle
        # 3. repeat
        while priority_queue and count > 0:
            edge = heapq.heappop(priority_queue)
            if not uf.connected(edge.point1, edge.point2):
                uf.union(edge.point1, edge.point2)
                min_cost += edge.cost
                count -= 1

        return min_cost

    # using prim's algorithm
    def minCostConnectPointsPrim(self, points: List[List[int]]) -> int:
        # using prim's algorithm to find minimum spanning tree
        size = len(points)
        count = size - 1
        min_cost = 0
        priority_queue = []
        visited = [False] * size # to track visited node

        # add all edges to min heap starting from vertex 0
        x1 , y1 = points[0]
        for j in range(1, size):
            x2 , y2 = points[j]
            # calculate distance between two points
            cost = abs(x1 - x2) + abs(y1 - y2)
            edge = Edge(0, j, cost)
            priority_queue.append(edge)

        # represent the edges in the priority queqe
        heapq.heapify(priority_queue)
        visited[0] = True # mark vertex 0 as visited

        # construct the minimum spaning tree using prim's algorithm
        # steps:
        # 1. take the minimum cost edge
        # 2. connect the edge if destination vertex is not visited yet
        # 3. take all edges starting from the destinantion vertex and insert in the heap
        # 4. repeat
        while priority_queue and count > 0:
            edge = heapq.heappop(priority_queue)
            point2 = edge.point2
            cost = edge.cost
            if not visited[point2]:
                min_cost += cost
                count -= 1
                visited[point2] = True

                # add all edges starting from point2 in the heap
                for j in range(size):
                    if not visited[j]:
                        distance = abs(points[point2][0] - points[j][0]) + \
                                   abs(points[point2][1] - points[j][1])
                        heapq.heappush(priority_queue,Edge(point2 , j , distance))

        return min_cost

    # using prim's algorithm
    def minCostConnectPointsPrimAlt(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}
        minHeap = [[0, 0]]  # cost, dst
        totalCost = 0
        visited = set()

        # build the adjacency list with cost
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # pop from the minHeap
        # check if the node is in visited or not
        # go through it's neighbors and add to minHeap
        while len(visited) < n:
            cost, i = heapq.heappop(minHeap)

            if i not in visited:
                totalCost += cost
                visited.add(i)

                for neiCost, nei in adj[i]:
                    if nei not in visited:
                        heapq.heappush(minHeap, [neiCost, nei])

        return totalCost