import heapq
from typing import List, Tuple, Dict, Optional

class Node:
    def __init__(self, position: Tuple[int, int], parent: Optional['Node'] = None, g: float = 0, h: float = 0):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h
    
    def __lt__(self, other):
        return self.f < other.f
    
    def __eq__(self, other):
        return self.position == other.position
    
def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """Heuristic function for the A * search algorithm
    
    Keyword arguments:
    a -- first node/position
    b -- second/next node/position
    Return: the heuristic value from the Manhattan distance between the two nodes/positions
    """  
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def A_starSearch(grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> Tuple[Optional[List[Tuple[int, int]]], Optional[Dict[Tuple[int, int], float]]]:
    """A * search algorithm for finding the shortest path between two nodes/positions in a grid
    
    Keyword arguments:
    grid -- grid with the nodes/positions
    start -- start state node/position
    goal -- goal state node/position
    Return: a tuple with the path and the visited nodes/positions
    """
    # # We define our initial variables
    # We get the number of rows and columns of the grid
    (rows,cols) = (len(grid), len(grid[0])) 

    # We use hueristics of start and goal nodes/positions
    priorityQueue = [Node(start, None, 0, heuristic(start, goal))]    

    open_set = {start: 0} # We Initialize the open set dictionary
    
    # We Initialize the visited nodes/positions dictionary
    visited = {}

    while priorityQueue: # We iterate while the priority queue is not empty
        # We get the current node/position by popping the node/position with the lowest f value
        current = heapq.heappop(priorityQueue)
        # We get the current node/position
        (x,y) = current.position

        # We check if the current node/position is the goal node/position
        if (x,y) == goal:
            path = [] # We initialize the path list
            while current: # We iterate while the current node/position is not None
                # We append the current node/position to the path list
                path.append(current.position)
                # We update the current node/position to its parent
                current = current.parent
            # We return the reversed path and the visited nodes/positions
            return path[::-1], visited
        
        # We add the current node/position to the visited nodes/positions dictionary
        visited[(x,y)] = current.f

        # We calculate the cost of moving to the neighbors and add them to the priority queue to be explored later, 
        # with least cost nodes/positions explored first
        for (Dx,Dy) in [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]:
            # We get the next node/position
            X,Y = x + Dx, y + Dy
            # We validate if the next node/position is within the grid and is not an obstacle and has not been visited
            if 0 <= X < rows and 0 <= Y < cols and grid[X][Y] == 0 and (X,Y) not in visited:
                # We calculate the g value of the next node/position
                if (Dx,Dy) in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                    g = current.g + 1.41
                else:
                    g = current.g + 1
                # We calculate the h value of the next node/position
                h = heuristic((X,Y), goal)
                
                if (X, Y) not in open_set or g < open_set[(X, Y)]:
                    open_set[(X, Y)] = g
                    heapq.heappush(priorityQueue, Node((X, Y), current, g, h))
    return [], visited