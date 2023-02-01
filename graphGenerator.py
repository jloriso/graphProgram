import random
import string
import argparse

def generate_vertex_name():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def main():
    parser = argparse.ArgumentParser(description="Generate a weighted graph")
    parser.add_argument("--vertices", type=int, help="Number of vertices in the graph")
    parser.add_argument("--connected", action="store_true", help="Generate a connected graph")
    args = parser.parse_args()

    num_vertices = args.vertices if args.vertices else random.randint(1, 20)
    print(num_vertices)
    is_connected = args.connected
    generate(num_vertices, is_connected)


def generate(num_vertices, is_connected):
    vertex_names = set()
    count = 1
    for i in range(num_vertices):
        vertex1 = generate_vertex_name()
        vertex2 = generate_vertex_name()
        while vertex1 == vertex2:
            vertex2 = generate_vertex_name()
        weight = round(random.uniform(-100, 100), 4)
        print(count, f"{vertex1} {vertex2} {weight}")
        count += 1
            
main()
