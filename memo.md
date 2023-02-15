# MEMO #

## Coding language ##

The implementation of the graph programs was scripted in Python

## Description ##

#### Part 1 ####

Part 1 is a graph generator. It will generate the graph and write
out the description of the weighted graph. Each line in the output
names two vertices and the weight of the edge between them.
The names of the vertices and weight are separated by
one or more white spaces. The vertices will have no more than 6 
characters, and the decimal for the weight no more than than 4 digits.
Edges will not be repeated.
---
The program takes a max of 2 arguments from the command line
1. --vertices N, which will generate N vertices, N must be an integer
2. --connected, when entered the graph will be connected
*Note that both of these are optional, the program will generate a random
number of vertices without argument 1 and the graph will randomly be
connected or unconnected without argument 2.*
---
The algorithm used to generate the connected graph runs in time complexity
O(n) since it uses a for loop to go through all the nodes in the graph.

#### Part 2 ####

Part 2 is a path generator. It will take the description of a connected
graph and find the shortest path between two vertices specificed by the
user in the command line. The result will then be printed out.
The program takes 2 arguments, the start and end vertices, while these
arguments are optional without them no path can be generated. After
entering the start and end vertices the user then enters the graph.
The graph will follow the format of, vertice1 vertice2 weight, all separated
by at least one space. Vertices can be any string that includes letters in
the English alphabet and digits 0-9. Weights can be positive or negative
decimals, scientific notation is not accepted. The user ends the input by
pressing CTRL + D. The program then outputs the names of the vertices in
the path and the length of the path.