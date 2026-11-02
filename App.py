import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    pq = [(0, start)]
    cost = {start: 0}
    parent = {start: None}

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while pq:
        f, current = heapq.heappop(pq)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for dr, dc in directions:
            r = current[0] + dr
            c = current[1] + dc

            if (0 <= r < len(grid) and
                0 <= c < len(grid[0]) and
                grid[r][c] == 0):

                neighbor = (r, c)
                new_cost = cost[current] + 1

                if neighbor not in cost or new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost
                    f = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(pq, (f, neighbor))
                    parent[neighbor] = current

    return None


grid = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0]
]

start = (0, 0)
goal = (3, 3)

path = astar(grid, start, goal)

print("Path:", path)