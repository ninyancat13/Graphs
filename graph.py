from DSALinkedList import *
import numpy as np

vertices = DSALinkedList()
verticeslist = DSALinkedList()

class GraphNode:
    
    def __init__(self, key):
        self.key = key

class Graph:

    def __init__(self):
        self.vertices = vertices
        self.verticeslist = verticeslist
        
    def add_vertex(self, key):
        newNd = GraphNode(key)
        vertices.insertLast(newNd)

    def add_edge(self, key):
        for link in self.vertices:
            if link.key == key[0]:
                verticeslist.insertLast(key)
            if link.key != key[0]:
                pass


    def print_graph(self):
        print("Let us try iterate over verticeslist") 
        one = (verticeslist.removeFirst())
        print("print one", one)
        two = (verticeslist.removeFirst())
        print("print two", two)
        string = one[0] + ":[" + one[1]
        
        print("Try to print the string...", string)
        for x in range(5):
            if one[0] == two[0]:
                string = string + ", " + two[1]
                one = two
                two = (verticeslist.removeFirst())
            if one[0] != two[0]:
                string = string + "]"
                string = string + "\n" + two[0] + ":[" + two[1]
                one = two
                two = (verticeslist.removeFirst())
        string = string + "]"       
        print("Let us try to print the final string now...\n", string)
                

#    def add_list(self):
#        n = 0
#        for link in self.vertices:
#            while link.key == edge[n][0]:
#                verticeslist.insertLast(edge[n][1])
#                n += 1
#            
#    def print_graph(self):
#        string = ":["
#        verticeslist1 = iter(verticeslist)
#        for ii in verticeslist1:
#            string = string + ii + "  "
#        string = string + "]"
#        return string

g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')
g.add_vertex('G')
g.add_vertex('H')
g.add_vertex('I')
g.add_vertex('J')

#edge = ['AB', 'AC', 'BA', 'BD', 'BE']
#g.add_list()

g.add_edge("AB")
g.add_edge("AC")
g.add_edge("BC")
g.add_edge("BD")
g.add_edge("BF")
g.add_edge("BH")
g.add_edge("CJ")
g.add_edge("CI")
g.add_edge("DE")
g.add_edge("DJ")

print("Let us try iterate over vertices")
vertices1 = iter(vertices)
print(vertices1)
for ii in vertices1:
    print(ii.key)

print("Let us try iterate over vertices")
verticeslist1 = iter(verticeslist)
print(verticeslist1)
for ii in verticeslist1:
    print(ii)
                

g.print_graph()
