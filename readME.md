# README #

## Description ##

This repository contains 2 python programs. The 1st generates a graph and the 2nd generates a between vertices in a graph.

Program 1) (graphGenerator.py) Generates a graph, either connected or unconnected based on user input, with a certain number of veritces, if provided by user input.
If no arguments are provided, the program will generate a random number of vertices and will randomly decided whether the graph will be connected or not.

Program 2) (genPath.py) Takes in user input for a start and end vertice and then generates a path, if possible, between the two. The program also takes in
user input for what the graph will be.

## How do I get set up? ##

Instructions in this README file are for a Windows 11 environment with python installed on the device.

### Configuration ###

1. Clone the repository:

```
$ git clone https://github.com.jloriso/graphProgram.git
```

2. Change into the graphProgram directory
```
$ cd graphProgram
```

3. Run the python file for part 1
This program takes 2 arguments --vertices followed by an integer and --connected for a connected graph
For example:
```
$ python graphGenerator.py --vertices 10 --connected
```
This program would make a graph with 10 vertices that is guaranteed to be connected.
If you do not want a connected graph simply omit the --connected part and the program will randomly generate either a connected or unconnected graph.
```
$ python graphGenerator.py --vertices 10
```
The --vertices part can also be omitted and the program will generate a random number of vertices:
```
$ python graphGenerator.py
```

4. Run the python file for part 2
This program takes 2 arguments the starting vertice and the ending vertice:
```
$ python genPath.py q1 q4
```
If a start and end are not provided no path can be provided.
Upon entering the start and end vertices the user will then enter the vertices and weights in the format. The vertices and weight are all separated by a space.
```
vertice1 vertice2 weight
```
Vertices can be any combination of numbers and letters, and weights can be any number excluding scientific notation.
To stop input of a graph the user enters ctrl + D and then enter.
The program will then generate a path if possible.

### Who do I talk to? ###

Email jloriso@hawk.iit.edu