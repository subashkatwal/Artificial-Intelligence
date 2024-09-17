import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue stores (cost, node, path)
    queue = [(0, start, [start])]
    visited = set()
    
    while queue:
        cost, node, path = heapq.heappop(queue)
        
        if node in visited:
            continue
        
        visited.add(node)
        
        if node == goal:
            return cost, path
        
        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + edge_cost, neighbor, path + [neighbor]))
    
    return float('inf'), []

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

cost, path = uniform_cost_search(graph, "A", "D")
print(f'Subash Katwal\n')
print(f'Path: {" -> ".join(path)} with Total Cost: {cost}')
