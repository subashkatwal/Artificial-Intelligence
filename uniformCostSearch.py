
import heapq 
def uniform_cost_search (graph,start,goal):
    queue=[(0,start)]
    visited=set()
    while queue:
        cost,node=heapq.heappop(queue)
        if node in visited:
            continue
        if node==goal:
            return cost
            visited.add(node)
        for neighbor,edge_cost in graph.get(node,[]):
            if neighbor not in visited :
                heapq.heappush(queue,(cost+edge_cost,neighbor))
    return float ('inf')
            
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}
print(f'Path cost is {uniform_cost_search(graph, "A", "D")}')
