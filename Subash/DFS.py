
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
        
    visited.add(start)
    print(start, end=' ')

    for adjacent in graph[start]:
        if adjacent not in visited:
            dfs(graph, adjacent, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B'],
    'D': ['B', 'E'],
    'E': ['D']
}

start_node = 'A'
print("DFS starting from start node:", start_node)
dfs(graph, start_node)
