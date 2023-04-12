def d_vector(graph, start):
    distances = {}
    predecessors = {}
    for node in graph:
        distances[node] = float('inf')
        predecessors[node] = None
    distances[start] = 0
    for i in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                if distances[u] + graph[u][v] < distances[v]:
                    distances[v] = distances[u] + graph[u][v]
                    predecessors[v] = u
    for u in graph:
        for v in graph[u]:
            if distances[u] + graph[u][v] < distances[v]:
                raise ValueError('Graph contains a negative-weight cycle')
    return distances, predecessors
graph = {
'A': {'B': 5, 'H': 9},
'B': {'A': 5, 'C': 9, 'H': 11},
'C': {'B': 9, 'D': 7, 'F': 5, 'I': 2},
'D': {'C': 7, 'E': 9, 'F': 14},
'E': {'D': 9, 'F': 10},
'F': {'C': 5, 'D': 14, 'E': 10, 'G': 3},
'G': {'F': 3, 'H': 2, 'I': 6},
'H': {'A': 9, 'B': 11, 'G': 2, 'I': 7},
'I': {'C': 3, 'G': 6, 'H': 7}
}

print(d_vector(graph, 'A')[0])