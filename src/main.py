from .search import A_starSearch
from fastapi import FastAPI
from typing import Tuple

# We instantiate the FastAPI object
app = FastAPI(title="A* Search Algorithm", description="A* Search Algorithm", version="1.0.0")

# We define the route for the A* search algorithm
@app.post("/search")
async def search(start: Tuple[int, int], goal: Tuple[int, int]):
    """A * search algorithm

    Keyword arguments:
    start -- start node/position
    goal -- goal node/position
    Return: a tuple with the path and the visited nodes/positions
    """
    
    grid = [[0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0]]
    
    # We call the A* search algorithm    
    path, visited = A_starSearch(grid, start, goal)
    return {
    "path": path if path else "[No path found]",  
    "visited": {str(k): v for k, v in visited.items()} if visited else "[No visited nodes/positions]"
    }


