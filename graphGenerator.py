import random
import string
import argparse

def generate_vertex_name():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

def main():
    parser = argparse.ArgumentParser(description="Generate a weighted graph")
    parser.add_argument("--vertices", type=int, help="Number of vertices in the graph")
    parser.add_argument("--connected", action="store_true", help="Generate a connected graph")
    args = parser.parse_args()

    num_vertices = 0
    if args.vertices:
        num_vertices = args.vertices
    else:
        num_vertices = random.randint(1,25)
    is_connected = args.connected
    generate(num_vertices, is_connected)


def roundEdge(edge):
    roundTo = random.randint(0,4)
    edge = round(edge, roundTo)
    return edge

def generate(num_vertices, is_connected):
    #generate vertices
    nodes1 = []
    nodes2 = []
    for i in range(num_vertices):
        nodes1.append(generate_vertex_name())
        vertex2 = generate_vertex_name()
        #check if vertices are the same
        while nodes1[i] == vertex2:
            vertex2 = generate_vertex_name()
        nodes2.append(vertex2)

    #create weights for nodes
    edges = []
    for i in range(num_vertices):
        if is_connected:
            edge = random.uniform(-99,99)
            edge = roundEdge(edge)
            #check if edge already exists
            for ed in edges:
                while ed == edge:
                    edge = random.uniform(-99,99)
                    edge = roundEdge(edge)
            edges.append(edge)

    #print out
    count = 1
    for i in range(num_vertices):
        if(is_connected):
            print(count, f"{nodes1[i]} {nodes2[i]} {edges[i]}")
        else:
             print(count, f"{nodes1[i]} {nodes2[i]}")
        count += 1
            
main()
