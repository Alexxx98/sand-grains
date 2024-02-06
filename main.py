import pygame
from models import Node
from settings import WIDTH, HEIGHT, WHITE, BLACK, FPS

import time


pygame.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()


def main():
    running = True
    drawing = False
    nodes = get_grid()
    grains = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawing = True

            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    mouse_pos = pygame.mouse.get_pos()
                    for row in nodes:
                        for node in row:
                            if mouse_pos[0] in range(
                                node.x,
                                node.x + node.width,
                            ) and mouse_pos[1] in range(node.y, node.y + node.height):
                                node.make_sand()
                                grains.append(node)

            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False

        for grain in grains:
            grain_pos = grain.get_pos()
            try:
                next_grain = nodes[grain_pos[0]][grain_pos[1] + 1]
                if not next_grain.is_sand():
                    next_grain.make_sand()
                    grain.make_space()
                    grains.remove(grain)
                    grains.append(next_grain)
            except IndexError:
                pass

        draw_grid(nodes)

        clock.tick(FPS)

    pygame.quit()


def get_grid():
    nodes = []
    node_width = 5
    node_height = 5
    rows = WIDTH // node_width
    cols = HEIGHT // node_height

    for row in range(rows):
        nodes.append([])
        for col in range(cols):
            nodes[row].append(Node(row, col, node_width, node_height))

    return nodes


def draw_grid(nodes):
    for row in nodes:
        for node in row:
            pygame.draw.rect(
                WINDOW, node.grain, pygame.Rect(node.x, node.y, node.width, node.height)
            )

    pygame.display.flip()


def draw_node(node):
    pygame.draw.rect(
        WINDOW, node.grain, pygame.Rect(node.x, node.y, node.width, node.height)
    )
    pygame.display.flip()


if __name__ == "__main__":
    main()
