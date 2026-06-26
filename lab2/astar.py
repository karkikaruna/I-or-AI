from heapq import heappush, heappop

start=(
    (5,8,2),
    (1,0,3),
    (4,7,6)
)
goal=(
    (1,2,3),
    (4,5,6),
    (7,8,0),
)

def h1 (start):
    count=0
    for i in range(3):
        for j in range (3):
            if start[i][j]!=0 and start[i][j]!=goal[i][j]:
                count=count+1
    return count
def find_blank(start):
    for i in range(3):
        for j in range (3):
            if start[i][j]==0 :
                return i,j

def get_neighbours(start):
    x,y=find_blank(start)
    moves=[(-1,0), (0,-1), (1,0), (0,1)]
    neighbours=[]

    for dx,dy in moves:
        nx=x+dx
        ny=y+dy
        if 0<=nx<3 and 0<=ny<3:
            board=[list(row) for row in start]
            board[x][y], board[nx][ny]=board[nx][ny], board[x][y]
            neighbours.append(tuple(map(tuple, board)))
        
    return neighbours
    
    
def display(start):
    for row in start:
        print(row)
    print()

def aStar(start, heuristic):
    pq=[]
    heappush(pq, (heuristic(start), 0,start))
    parent={start: None}
    g_cost={start:None}

    expanded=0


    while pq:
        f,g, current=heappop(pq)
        expanded+=1

        if current==goal:
            return True, parent,expanded
        for neighbour in get_neighbours(current):
            new_g=g+1
            if neighbour not in g_cost or new_g<g_cost[neighbour]:
                g_cost[neighbour]=new_g
                f_cost=new_g+ heuristic(neighbour)
                heappush(
                    pq, 
                    (f_cost, new_g, neighbour)

                )
                parent[neighbour]=current
    return False,parent, expanded

def reconstruct(parent, current):
    path=[]
    while current is not None:
        path.append(current)
        current=parent[current]
    return path[::-1]

goalFound,parent,expanded =aStar(start, h1)

if(goalFound):
    print(f"Goal found after expanding {expanded} starts")
    for state in reconstruct(parent, goal):
        display(state)

else:
    print(F"Goal start not found after expanding {expanded}")

   
