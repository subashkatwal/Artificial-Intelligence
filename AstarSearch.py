print("Subash Katwal \n ")
from queue import PriorityQueue

def a_star_search(graph, start, goal, heuristic):
    open_list = PriorityQueue()
    open_list.put((0 + heuristic[start], 0, start, [start]))
    came_from = {start: None}

    while not open_list.empty():
        _, current_cost, current_node, path = open_list.get()
        if current_node == goal:
            print(f"Goal reached! Path: {' -> '.join(path)} with Total Cost: {current_cost}")
            return
        for neighbor, cost in graph[current_node]:
            new_cost = current_cost + cost
            if neighbor not in came_from or new_cost < came_from[neighbor][1]:
                came_from[neighbor] = (current_node, new_cost)
                new_path = path + [neighbor]
                open_list.put((new_cost + heuristic[neighbor], new_cost, neighbor, new_path))

# Example graph and heuristic
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 4), ('E', 2)],
    'C': [('F', 2)],
    'D': [],
    'E': [('G', 1)],
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
a_star_search(graph, 'A', 'G', heuristic)
