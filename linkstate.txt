def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    while len(visited) < len(graph):
        current_node = min(
        (node for node in graph if node not in visited),
key=distances.get)
        current_distance = distances[current_node]
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
        visited.add(current_node)
    return distances
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
start = 'A'
print(dijkstra(graph, start))
