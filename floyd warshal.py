# function to calculate minimum shortest distance between all pair of vertices of a graph


def minimum_distance_vertex_pair(graph):
    n = len(graph)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[j][k] > graph[j][i]+graph[i][k]:
                    print
                    graph[j][k] = graph[j][i]+graph[i][k]

    return graph

# INF = float('Inf')
# graph = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]
# print fun(graph)