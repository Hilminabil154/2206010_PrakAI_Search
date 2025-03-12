from queue import PriorityQueue

def a_star_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put((0 + heuristic[start], 0, start, [start]))  # (f, g, node, path)
    explored = set()
    
    while not frontier.empty():
        _, cost, current_node, path = frontier.get()
        
        if current_node == goal:
            print("Goal node found!")
            print("Path:", path)
            print("Total cost:", cost)
            return path, cost
        
        explored.add(current_node)
        
        for neighbor, step_cost in graph[current_node].items():
            if neighbor not in explored:
                g = cost + step_cost  # Path cost
                f = g + heuristic[neighbor]  # f = g + h
                frontier.put((f, g, neighbor, path + [neighbor]))
    
    print("Goal node not found!")
    return None, float('inf')

# Heuristic values
heuristic = {
    'A': 9,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'S': 7,
    'G': 0
}

# Graph adjacency list
graph = {
    'S': {'A': 3, 'E': 2},
    'A': {'B': 3, 'C': 4},
    'B': {'D': 5},
    'C': {'G': 7},
    'D': {'G': 3},
    'E': {'D': 6}
}

# Start and goal nodes
start_node = 'S'
goal_node = 'G'

# Execute A* search
a_star_search(graph, start_node, goal_node, heuristic)
