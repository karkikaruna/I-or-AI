from collections import deque

CAPACITY_A=4
CAPACITY_B=3

def get_next_states(state):
    A,B=state
    next_states=[]

    next_states.append((CAPACITY_A,B))
    

    next_states.append((A,CAPACITY_B))

    next_states.append((0,B))

    next_states.append((A,0))

    transfer=min(A, CAPACITY_B-B)
    next_states.append((A-transfer, B+transfer))

    transfer=min(B, CAPACITY_A-A)
    next_states.append((A+transfer, B-transfer))
    return next_states

def bfs():
    start=(0,0)
    queue=deque()

    queue.append((start, [start]))

    visited=set()
    while queue:
        state, path=queue.popleft()

        if state in visited:
            continue

        visited.add(state)

        if state[0]==2:
            return path
        for next_state in get_next_states(state):
            if next_state not in visited:
                queue.append((next_state, path+ [next_state]))
    return None
solution=bfs()

if solution:
    print("Shortesst solution Path: \n")

    for step, state in enumerate(solution):
        print(f"Step {step}: {state}")
    
else:
    print("NO solution found.")