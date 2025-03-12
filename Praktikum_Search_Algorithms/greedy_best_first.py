from queue import PriorityQueue

def greedy_best_first_search(graph, heuristic, start, goal):
    frontier = PriorityQueue()
    frontier.put((heuristic[start], start, [start]))  # (heuristic, node, path)
    explored = set()
    
    print("Traversal order:")
    
    while not frontier.empty():
        _, current_node, path = frontier.get()
        print(current_node, end=' ')
        
        if current_node == goal:
            print("\nGoal node found!")
            print("Path:", path)
            return path
        
        explored.add(current_node)
        
        for neighbor in graph[current_node]:
            if neighbor not in explored:
                frontier.put((heuristic[neighbor], neighbor, path + [neighbor]))
    
    print("\nGoal node not found!")
    return None

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
    'S': ['A', 'E'],
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['G'],
    'D': ['G'],
    'E': ['D']
}

# Start and goal nodes
start_node = 'S'
goal_node = 'G'

greedy_best_first_search(graph, heuristic, start_node, goal_node)
