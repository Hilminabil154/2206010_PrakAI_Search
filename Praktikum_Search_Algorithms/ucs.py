import heapq
import networkx as nx

def uniform_cost_search(graph, start, goal):
    """
    Performs Uniform Cost Search using a priority queue (heapq).
    
    Args:
        graph: A NetworkX graph object.
        start: The starting node.
        goal: The goal node.
    Returns:
        A tuple containing:
            - The minimum cost to reach the goal node.
            - The path from the start node to the goal node.
    """
    priority_queue = [(0, start, [])]  # (cost, node, path)
    visited = set()
    
    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        
        if node in visited:
            continue
        
        path = path + [node]
        visited.add(node)
        
        if node == goal:
            return cost, path
        
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                edge_cost = graph[node][neighbor]['weight']
                heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path))
    
    return float('inf'), []  # Return infinity if goal is unreachable

# Example usage:
graph = nx.Graph()
graph.add_edge(0, 1, weight=2)
graph.add_edge(0, 3, weight=5)
graph.add_edge(3, 1, weight=5)
graph.add_edge(3, 6, weight=6)
graph.add_edge(3, 4, weight=2)
graph.add_edge(1, 6, weight=1)
graph.add_edge(4, 5, weight=3)
graph.add_edge(2, 5, weight=5)
graph.add_edge(5, 6, weight=3)
graph.add_edge(6, 4, weight=7)

start_node = 0
goal_node = 5

min_cost, path = uniform_cost_search(graph, start_node, goal_node)

if min_cost == float('inf'):
    print("Goal node is unreachable.")
else:
    print("Minimum cost:", min_cost)
    print("Path:", path)
