import collections

def bfs(graph, start, goal):
    visited = set()
    queue = collections.deque([(start, [start])])
    
    while queue:
        vertex, path = queue.popleft()
        
        if vertex == goal:
            print("Path found:", path)
            return path
        
        visited.add(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
    
    print("No path found.")
    return None

if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    start_node = 'A'
    goal_node = 'F'
    print("Breadth First Search traversal :")
    bfs(graph, start_node, goal_node)
