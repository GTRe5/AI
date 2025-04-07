import pygame
import sys
import time
from map_loader import MapLoader
from astar import a_star_search

CELL_SIZE = 24
FPS = 10

def draw_map(screen, map_loader, pacman_pos, food, power_timer):
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont(None, 20)

    for y, row in enumerate(map_loader.map_data):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = (50, 50, 50)
            if cell == '%':
                color = (0, 0, 255)
            elif (x, y) in food:
                color = (255, 255, 255)
            elif (x, y) in map_loader.magic_pies:
                color = (255, 0, 255)
            pygame.draw.rect(screen, color, rect)

    pac_rect = pygame.Rect(pacman_pos[0] * CELL_SIZE, pacman_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.circle(screen, (255, 255, 0), pac_rect.center, CELL_SIZE // 2)

    label = font.render("Magic Pies: pink rectangles", True, (255, 0, 255))
    screen.blit(label, (10, map_loader.getHeight() * CELL_SIZE + 5))

    label = font.render("Foods are: white rectangles", True, (255, 255, 255))
    screen.blit(label, (10, map_loader.getHeight() * CELL_SIZE + 20))

    pygame.display.flip()

def main():
    map_loader = MapLoader('task02_pacman_example_map.txt').load()
    path, cost = a_star_search(map_loader)

    if path is None:
        print("No path found!")
        return

    print(f"Actions: {path}")
    print(f"Total cost: {cost}")

    pygame.init() 
    width = map_loader.getWidth() * CELL_SIZE
    height = map_loader.getHeight() * CELL_SIZE + 50
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    food = set(map_loader.food)
    pacman_pos = map_loader.pacman_pos
    power_timer = 0

    draw_map(screen, map_loader, pacman_pos, food, power_timer)
    print("Press any key to start...")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                break
        else:
            continue
        break

    for move in path:
        dx, dy = {'North': (0, -1), 'South': (0, 1), 'East': (1, 0), 'West': (-1, 0)}[move]
        new_pos = (pacman_pos[0] + dx, pacman_pos[1] + dy)

        pacman_pos = new_pos
        power_timer = max(0, power_timer - 1)
        if pacman_pos in food:
            food.remove(pacman_pos)

        if pacman_pos in map_loader.magic_pies:
            map_loader.magic_pies.remove(pacman_pos)

        draw_map(screen, map_loader, pacman_pos, food, power_timer)
        time.sleep(0.1)
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
