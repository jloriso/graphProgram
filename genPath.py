from collections import defaultdict, deque
import sys

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}
        
    def add_edge(self, u, v, w):
        self.vertices.add(u)
        self.vertices.add(v)
        if (u, v) in self.edges:
            print(f"Duplicate edge ({u}, {v})")
            sys.exit(1)
        self.edges[(u, v)] = w

    def bfs(self, start, end):
        if start not in self.vertices:
            print(f"Vertex {start} not in graph")
            sys.exit(1)
        if end not in self.vertices:
            print(f"Vertex {end} not in graph")
            sys.exit(1)
        
        dist = {v: float('inf') for v in self.vertices}
        prev = {v: None for v in self.vertices}
        dist[start] = 0
        q = deque([start])
        
        while q:
            u = q.popleft()
            for v in self.vertices:
                if (u, v) in self.edges:
                    alt = dist[u] + self.edges[(u, v)]
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u
                        q.append(v)
                        
        if dist[end] == float('inf'):
            print(f"No path from {start} to {end}")
            sys.exit(1)
            
        path = []
        curr = end
        while curr != start:
            path.append(curr)
            curr = prev[curr]
        path.append(start)
        path.reverse()
        
        return path, dist[end]
        
def main():
    g = Graph()
    lineCount = 1
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) != 3:
            break
        u, v, w = parts
        if not all(c.isalnum() for c in u):
            print(f"Invalid vertex name: {u} at line: {lineCount}")
            sys.exit(1)
        if not all(c.isalnum() for c in v):
            print(f"Invalid vertex name: {v} at line: {lineCount}")
            sys.exit(1)
        try:
            w = float(w)
        except ValueError:
            print(f"Invalid weight: {w} at line: {lineCount}")
            sys.exit(1)
        g.add_edge(u,v,w)
        lineCount += 1

    if len(sys.argv) != 3:
        if len(sys.argv) == 1 and sys.argv == "^D":
            print("Stopping input")
        else:
            print("Enter in the format vertice1 vertice2 weight")
            sys.exit(1)
    start, end = sys.argv[1:3]
    path, dist = g.bfs(start, end)
    print(f"Path: {'-'.join(path)}")
    print(f"Length: {dist}")

main()