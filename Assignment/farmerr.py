from collections import deque

def is_safe(state):
    f, w, g, c = state

    if w == g and f != w:
        return False

    if g == c and f != g:
        return False

    return True


def solve_wolf_goat_cabbage():
    # (farmer, wolf, goat, cabbage)
    start_state = (1, 1, 1, 1)
    goal_state = (-1, -1, -1, -1)

    queue = deque([(start_state, [])])
    visited = {start_state}

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path

        f, w, g, c = current_state

        moves = []

        if f == w:
            moves.append(("wolf",))

        if f == g:
            moves.append(("goat",))

        if f == c:
            moves.append(("cabbage",))

        # Farmer moves alone
        moves.append(())

        for move in moves:
            new_state = list(current_state)

            # Farmer crosses river
            new_state[0] = -f

            if "wolf" in move:
                new_state[1] = -w

            if "goat" in move:
                new_state[2] = -g

            if "cabbage" in move:
                new_state[3] = -c

            new_state = tuple(new_state)

            if new_state not in visited and is_safe(new_state):
                visited.add(new_state)
                queue.append((new_state, path + [move]))

    return None


solution = solve_wolf_goat_cabbage()

if solution:
    for i, step in enumerate(solution, start=1):
        if step:
            print(f"Step {i}: Farmer takes {step[0]}")
        else:
            print(f"Step {i}: Farmer crosses alone")
else:
    print("No solution found")