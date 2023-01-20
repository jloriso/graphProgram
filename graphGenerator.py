import random
import string

def generate_vertex_name():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def main():
    num_vertices = 10
    num_edges = verticesInput()
    vertex_names = set()
    for i in range(num_edges):
        vertex1 = generate_vertex_name()
        vertex2 = generate_vertex_name()
        while vertex1 == vertex2:
            vertex2 = generate_vertex_name()
        weight = round(random.uniform(-100, 100), 4)
        print(f"{vertex1} {vertex2} {weight}")


def verticesInput():
    while True:
        try:
            n = input("Enter an integer or enter r for random: ")

            if n == "r" or n == "R":
                n = random.randint(1,50)
                print(n)
            else:
                n = int(n)

            return n
        except ValueError:
            print("Invalid input. Please enter an integer.")

            
main()
