import heapq
from pacman_game import GameState


# class Node:
#     def __init__(self, state, cost):
#         self.state = state
#         self.cost = cost

    
def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def heuristic(state):
    if not state.food:
        return 0
    return min([manhattan(state.pacman_pos, f) for f in state.food])

def a_star_search(map_loader, path = None, cost = 0):
    if path is None:
        path=[]

    start = GameState(map_loader.pacman_pos, map_loader.food, cost)
    f = 0
    frontier = []
    heapq.heappush(frontier, (f, (start, path)))
    visited = set()

    while frontier:
        _, state = heapq.heappop(frontier)
        current, path = state

        if current.goalState():
            return path, current.cost
        
        if current in visited:
            continue
        visited.add(current)

        for new_x, new_y, action in current.successors():
            #  = successor

            max_y, max_x = map_loader.getHeight() - 1, map_loader.getWidth() - 1
            new_x, new_y = GameState.isTeleport(pos=(new_x, new_y), max_pos=(max_x, max_y))

            if 0 <= new_y < max_y and 0 <= new_x < max_x:
                cell = map_loader.map_data[new_y][new_x]
                can_pass = cell != '%' or current.power_timer > 0

                if can_pass:
                    new_food = set(current.food)
                    new_power = max(0, current.power_timer - 1)

                    if (new_x, new_y) in new_food:
                        new_food.remove((new_x, new_y))
                    if (new_x, new_y) in map_loader.magic_pies:
                        new_power = 5

                    new_cost = current.cost + 1
                    new_state = GameState((new_x, new_y), new_food, new_cost, new_power)
                    new_path = path + [action]
                    f = new_cost + heuristic(new_state)
                    heapq.heappush(frontier, (f, (new_state, new_path)))
    return None, None
