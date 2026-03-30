def a_star(graph, heuristic, start, goal):
    open_list = [start]
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    parent = {}

    while open_list:
        # find node with lowest f = g + h
        current = min(open_list, key=lambda x: g_cost[x] + heuristic[x])

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent.get(current)
            path.reverse()
            return path, g_cost[goal]

        open_list.remove(current)

        for neighbor in graph[current]:
            new_cost = g_cost[current] + graph[current][neighbor]

            if new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                parent[neighbor] = current

                if neighbor not in open_list:
                    open_list.append(neighbor)

    return None, float('inf')