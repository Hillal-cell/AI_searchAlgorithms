from collections import deque

def bfs(state_infos, start, goal):
    visited = set()  # Set to keep track of visited nodes.
    queue = deque([(start, [start])])  # Queue for BFS. Each element is a tuple (current_node, path_so_far)
    expanded = []

    while queue:
        node, path_so_far = queue.popleft()  # Dequeue the first node and its path

        if node not in visited:
            visited.add(node)
            expanded.append(node)

            if node == goal:
                unexpanded = list(set(state_infos.keys()) - set(expanded))
                return path_so_far, expanded, unexpanded

            neighbors = list(state_infos[node]["path_costs"].keys())
            for neighbor in neighbors:
                if neighbor not in visited:
                    new_path = list(path_so_far)
                    new_path.append(neighbor)
                    queue.append((neighbor, new_path))

    unexpanded = list(set(state_infos.keys()) - set(expanded))
    return None, expanded, unexpanded

state_infos = {
    'S': {
        "path_costs": {"A": 3, "B": 1},
        "heuristic_value": 7
    },
    'A': {
        "path_costs": {"B": 2, "C": 2},
        "heuristic_value": 5
    },
    'B': {
        "path_costs": {"C": 3},
        "heuristic_value": 7
    },
    'C': {
        "path_costs": {"D": 4, "G": 4},
        "heuristic_value": 4
    },
    'D': {
        "path_costs": {"G": 1},
        "heuristic_value": 1
    },
    'G': {
        'path_costs': {},
        "heuristic_value": 0
    }
}

path, expanded_states, unexpanded_states = bfs(state_infos, 'S', 'G')

if path:
    print(f"Path using BFS Tree Search: {' -> '.join(path)}")
    print(f"Order of states expanded: {', '.join(expanded_states)}")
    print(f"States that were not expanded: {', '.join(unexpanded_states)}")
else:
    print("No path found using BFS Tree Search!")
