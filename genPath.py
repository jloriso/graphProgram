import sys
import re
from collections import defaultdict

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

def bfs(graph, start, end):
    pass