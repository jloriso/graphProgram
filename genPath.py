from collections import defaultdict, deque
import sys
import re

def parse_input():
    graph = defaultdict(list)
    for i, line in enumerate(sys.stdin, 1):
        edge = line.strip().split()
        if len(edge) != 3:
            print("Invalid input format at line", i)
            sys.exit(1)
        node1, node2, weight = edge
        if not re.match("^[a-zA-Z0-9]+$", node1) or not re.match("^[a-zA-Z0-9]+$", node2):
            print("Invalid node name at line", i)
            sys.exit(1)
        try:
            weight = float(weight)
        except ValueError:
            print("Invalid weight at line", i)
            sys.exit(1)
        if node1 in graph and (node2, weight) in graph[node1]:
            print("Duplicate edge at line", i, "first appeared at", graph[node1].index((node2, weight)) + 1)
            sys.exit(1)
        graph[node1].append((node2, weight))
        graph[node2].append((node1, weight))
    return graph

def find_shortest_path(graph, start, end):
    queue = [(start, [start])]
    visited = set()
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex in visited:
            continue
        visited.add(vertex)
        for (neighbour, weight) in graph[vertex]:
            if neighbour == end:
                return path + [end]
            queue.append((neighbour, path + [neighbour]))
    return None

def main():
    start, end = sys.argv[1], sys.argv[2]
    graph = parse_input()
    path, length = find_shortest_path(graph, start, end)
    print(f"Path: {path}")
    print(f"Length: {length}")

main()