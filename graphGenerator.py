import random
import string
import argparse

def generate_vertex_name():
    length = random.randint(1,6)
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

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
    if is_connected == False:
        #randomly make a graph connected if not specified
        if random.random() > 0.5:
            is_connected = True
    generate(num_vertices, is_connected)

def roundEdge(edge):
    roundTo = random.randint(0,4)
    edge = round(edge, roundTo)
    return edge

def connect(num_vertices, is_connected, nodes, edges):
    inOrderNodes = []

    for i in range(len(nodes)):
        if i == 0:
            inOrderNodes.append(nodes[0])
        else:
            inOrderNodes.append(nodes[i])
            inOrderNodes.append(nodes[i])
    inOrderNodes.append(generate_vertex_name())
    return inOrderNodes

def unconnected(num_vertices, nodes, edges):
    inOrderNodes = []
    for i in range(len(nodes)):
        inOrderNodes.append(nodes[i])

    return inOrderNodes

def generate(num_vertices, is_connected):
    #generate vertices
    nodes = []
    edges = []
    if is_connected:
        for i in range(num_vertices):
            #generate vertices
            if i == 0:
                nodes.append(generate_vertex_name())
            #remove duplicates
            else:
                gen = generate_vertex_name()
                for node in nodes:
                    while node == gen:
                        gen = generate_vertex_name()
                nodes.append(generate_vertex_name())
    else:
        for i in range(2):
            for i in range(num_vertices):
                #generate vertices
                if i == 0:
                    nodes.append(generate_vertex_name())
                #remove duplicates
                else:
                    gen = generate_vertex_name()
                    for node in nodes:
                        while node == gen:
                            gen = generate_vertex_name()
                    nodes.append(generate_vertex_name())

    #create weights for nodes
    for i in range(num_vertices):
        edge = random.uniform(-99,99)
        edge = roundEdge(edge)
        #check if edge already exists
        for ed in edges:
            while ed == edge:
                edge = random.uniform(-99,99)
                edge = roundEdge(edge)
        edges.append(edge)

    vertices = []
    #generate the connections
    if is_connected:
        vertices = connect(num_vertices, is_connected, nodes, edges)
    else:
        vertices = unconnected(num_vertices, nodes, edges)
    
    #print out
    nodesCount = 0
    for i in range(num_vertices):
        print(f"{vertices[nodesCount]} {vertices[nodesCount+1]} {edges[i]}")
        nodesCount += 2
            
main()