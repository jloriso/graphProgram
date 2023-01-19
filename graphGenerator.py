import random
import string

def generate_vertex_name():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def main():
    num_vertices = 10
    num_edges = 15
    vertex_names = set()
    for i in range(num_edges):
        vertex1 = generate_vertex_name()
        vertex2 = generate_vertex_name()
        while vertex1 == vertex2:
            vertex2 = generate_vertex_name()
        weight = round(random.uniform(0, 100), 4)
        print(f"{vertex1} {vertex2} {weight}")


def verticesInput():
    while True:
        try:
            n = int(input("Enter an integer: "))
            return n
        except ValueError:
            print("Invalid input. Please enter an integer.")

            
main()
