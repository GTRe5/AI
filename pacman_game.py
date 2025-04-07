import map_loader

class GameState:
    def __init__(self, pacman_pos, food, cost, power_timer=0):
        self.pacman_pos = pacman_pos
        self.food = frozenset(food)
        self.power_timer = power_timer
        self.cost = cost

    def __hash__(self):
        return hash((self.pacman_pos, self.food, self.power_timer))

    def __eq__(self, other):
        return (self.pacman_pos, self.food, self.power_timer) == (other.pacman_pos, other.food, other.power_timer)
    
    def goalState(self):
        if len(self.food) == 0:
            return True
        return False
    
    def actions(self):
        direction = [('North', (0, -1)),
               ('South', (0, 1)),
               ('East', (1, 0)),
               ('West', (-1, 0))]
        return direction
    
    def successors(self):
        x, y = self.pacman_pos

        return [(x + move[0], y + move[1], action) for action, move in self.actions()]

        # result = []
        # for action, move in self.actions():
        #     new_x = x + move[0]
        #     new_y = y + move[1]
        #     result.append((new_x, new_y))
        # return result

    def isTeleport(pos, max_pos):
        x, y = pos[0], pos[1]
        max_x, max_y = max_pos[0], max_pos[1]

        if (x, y) in [(0, 0), (0, max_y), (max_x, 0), (max_x, max_y)]:
                return (max_x - x, max_y - y)
        return (x, y)

    def __lt__(self, other):
        """So sánh GameState dựa trên vị trí hoặc số thức ăn còn lại."""
        return len(self.food) < len(other.food)  # So sánh số lượng thức ăn còn lại
    

