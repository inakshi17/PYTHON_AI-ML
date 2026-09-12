# Minimalist A* Search Algorithm in Python

import heapq

def a_star_search(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic[start], 0, start, [start]))
    visited = set()

    while open_set:
        f_score, g_score, current, path = heapq.heappop(open_set)

        if current == goal:
            return path, g_score

        if current in visited:
            continue
        visited.add(current)

        for neighbor, weight in graph.get(current, {}).items():
            if neighbor not in visited:
                tentative_g = g_score + weight
                f = tentative_g + heuristic.get(neighbor, float('inf'))
                heapq.heappush(open_set, (f, tentative_g, neighbor, path + [neighbor]))

    return None, float('inf')


# Standard Graph Setup
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Heuristic values (estimated distance to goal 'D')
heuristic = {
    'A': 7,
    'B': 6,
    'C': 1,
    'D': 0
}

path, cost = a_star_search(graph, 'A', 'D', heuristic)
print("Shortest Path:", path)
print("Total Cost:", cost)
