
print("Subash Katwal \n")
from queue import PriorityQueue

def greedy_best_first_search(graph, start, goal, heuristic):
    open_list = PriorityQueue()
    open_list.put((heuristic[start], start, [start], 0))
    visited = set()

    while not open_list.empty():
        _, current_node, path, cost = open_list.get()
        if current_node == goal:
            print(f"Goal reached! Path: {' -> '.join(path)} with Total Cost: {cost}")
            return
        visited.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                new_cost = cost + 1  # Assuming cost of 1 for each step
                open_list.put((heuristic[neighbor], neighbor, new_path, new_cost))
                visited.add(neighbor)

# Example graph and heuristic
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}
heuristic = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 6,
    'E': 2,
    'F': 6,
    'G': 0
}

# Running the search
greedy_best_first_search(graph, 'A', 'G', heuristic)
