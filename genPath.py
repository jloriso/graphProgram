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
            print("Vertex ", start, " not in graph")
            sys.exit(1)
        if end not in self.vertices:
            print("Vertex ", end, " not in graph")
            sys.exit(1)

        queue = [(start, [start])]
        visited = set()
        while queue:
            (vertex, path) = queue.pop(0)
            if vertex in visited:
                continue
            visited.add(vertex)
            for (neighbour, weight) in self[vertex]:
                if neighbour == end:
                    return path + [end]
                queue.append((neighbour, path + [neighbour]))
        return None

def main():
    g = Graph()
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) != 3:
            break
        u, v, w = parts
        if not all(c.isalnum() for c in u):
            print(f"Invalid vertex name: {u}")
            sys.exit(1)
        if not all(c.isalnum() for c in v):
            print(f"Invalid vertex name: {v}")
            sys.exit(1)
        try:
            w = float(w)
        except ValueError:
            print(f"Invalid weight: {w}")
            sys.exit(1)
        g.add_edge(u,v,w)

    if len(sys.argv) != 3:
        if len(sys.argv) == 1 and sys.argv == "^D":
            print("Stopping input")
        else:
            print("Usage: sp start end")
            sys.exit(1)
    start, end = sys.argv[1:3]
    path, dist = g.bfs(start, end)
    print(f"Path: {'-'.join(path)}")
    print(f"Length: {dist}")

main()