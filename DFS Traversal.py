from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSAll(self,visited,v):
        visited[v]=True
        print v,
        for nextVertex in self.graph[v]:
            if not visited[nextVertex]:
                self.DFSAll(visited,nextVertex)

    # if the graph is not connected (any given source can not lead to any given destination)
    def DFSAllNotConnected(self):
        visited = [False]*len(self.graph)
        for vertex in self.graph:
            if not visited[vertex]:
                self.DFSAll(visited,vertex)

    # if the graph is connected (any given source can lead to any given destination)
    def DFSAllConnected(self,startVertex):
        visited = [False] * len(self.graph)
        self.DFSAll(visited,startVertex)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.DFSAllConnected(2)
print
g.DFSAllNotConnected()
