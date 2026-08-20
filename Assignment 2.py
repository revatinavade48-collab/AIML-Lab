import heapq

def a_star(graph, heuristic, start, goal):

    # Priority queue: (f_cost, current_node)
    open_list = [(0, start)]

    # Cost from start node to each node
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    # To reconstruct the final path
    parent = {node: None for node in graph}

    while open_list:

        # Select node with minimum f(n)
        current_f, current = heapq.heappop(open_list)

        # Goal reached
        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path, g_cost[goal]

        # Explore neighboring nodes
        for neighbor, cost in graph[current]:

            # Calculate new actual cost
            new_g_cost = g_cost[current] + cost

            # Check whether this is a better path
            if new_g_cost < g_cost[neighbor]:

                # Update g(n)
                g_cost[neighbor] = new_g_cost

                # Store parent
                parent[neighbor] = current

                # Calculate f(n) = g(n) + h(n)
                f_cost = new_g_cost + heuristic[neighbor]

                # Add to priority queue
                heapq.heappush(open_list, (f_cost, neighbor))

    return None, float('inf')


# Graph representation
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1), ('E', 3)],
    'E': [('D', 3)]
}


# Heuristic values h(n)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0
}


# Starting and goal nodes
start = 'A'
goal = 'E'


# Execute A* algorithm
path, cost = a_star(graph, heuristic, start, goal)


# Display result
if path:
    print("Optimal Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found.")