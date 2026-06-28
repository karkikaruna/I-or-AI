from collections import deque

grid = [
    ['S', '.', '.', 'X', '.'],
    ['.', 'X', '.', 'X', '.'],
    ['.', 'X', '.', '.', '.'],
    ['.', '.', 'X', 'X', '.'],
    ['.', '.', '.', '.', 'G']
]

rows = len(grid)
cols = len(grid[0])

start = (0, 0)
goal = (4, 4)

# Up, Down, Left, Right
directions = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs():
    queue = deque()
    queue.append((start, [start]))
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if (x, y) == goal:
            return path

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if (0 <= nx < rows and
                0 <= ny < cols and
                grid[nx][ny] != 'X' and
                (nx, ny) not in visited):

                queue.append(((nx, ny), path + [(nx, ny)]))

    return None


path = bfs()

if path:
    print("Shortest Path:\n")
    for step in path:
        print(step)
else:
    print("No Path Found")