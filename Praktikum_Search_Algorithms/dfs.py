from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, goal, path, visited):
        path.append(v)
        visited.add(v)
        
        if v == goal:
            print("Path found:", path)
            return path
        
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                result = self.dfs_util(neighbor, goal, path.copy(), visited.copy())
                if result:
                    return result
        
        return None

    def dfs(self, start, goal):
        visited = set()
        print("DFS traversal:")
        path = self.dfs_util(start, goal, [], visited)
        if not path:
            print("No path found.")

if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('E', 'F')
    
    start_node = 'A'
    goal_node = 'F'
    g.dfs(start_node, goal_node)
