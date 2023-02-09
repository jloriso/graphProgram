from collections import defaultdict, deque
import sys

def parse_input():
    graph = defaultdict(list)
    for line in sys.stdin:
        src, dest, weight = line.strip().split()
        graph[src].append((dest, weight))
        graph[dest].append((src, weight))
    return graph

def find_shortest_path(graph, start, end):
    pass

def main():
    start, end = sys.argv[1], sys.argv[2]
    graph = parse_input()
    path, length = find_shortest_path(graph, start, end)
    print(f"Path: {path}")
    print(f"Length: {length}")

main()