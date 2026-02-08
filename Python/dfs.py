def dfs(matrix, start_node):
    visited = []
    stack = []
    output = []
    stack.append(start_node)
    while stack:
        current = stack.pop()

        if current in visited:
            continue
        visited.append(current)
        output.append(current)

        for neighbor in range(len(matrix)):
            if matrix[current][neighbor] == 1 and neighbor not in visited:
                stack.append(neighbor)
    return output


example = dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1)
print(example)



