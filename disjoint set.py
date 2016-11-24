# Node class for storing rank, representative of set and the parent of the node
class Node:
    def __init__(self,value):
        self.parent = self
        self.representative = value
        self.rank = 0


class Graph:
    def __init__(self):
        self.setS = {}  # initialize empty dict for storing node

    def makeSet(self,vertexValue):  # function to initializing a node and add it to graph dictionary
        node = Node(vertexValue)
        self.setS[vertexValue]=node

    def findParent(self,node):  # function to find the parent of node
        if node.parent!=node:
            node.parent = self.findParent(node.parent)   # used for recursion and path compression
        return node.parent

    def printRepresent(self,vertex):    # function to return the representative of the set
        return self.findParent(self.setS[vertex]).representative

    def unionSet(self,vertex1,vertex2):  # function to do the union of two sets
        node1 = self.setS[vertex1]
        node2 = self.setS[vertex2]
        parent1 = self.findParent(node1)
        parent2 = self.findParent(node2)
        if parent1==parent2:
            return
        if parent1.rank<parent2.rank:
            parent1.parent = parent2
        elif parent1.rank>parent2.rank:
            parent2.parent = parent1
        else:
            parent1.parent = parent2
            parent2.rank +=1




g = Graph(5)
for i in xrange(1,6):
    g.makeSet(i)
g.unionSet(1,2)
g.unionSet(2,3)
g.unionSet(3,4)
g.unionSet(4,5)
g.unionSet(5,1)

for i in xrange(1,6):
    print g.printRepresent(i)