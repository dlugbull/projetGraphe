import pygame
import random
import networkx as nx


def reset():
    global in_maze, maze_edges, walls, steps

    # Réinitialiser les structures
    in_maze = set()
    maze_edges = []

    # Réinitialiser les murs
    for node in G.nodes():
        walls[node] = {"N": True, "S": True, "E": True, "W": True}

    # Effacer l’écran
    screen.fill(BG)

    # Redessiner la grille vide
    for node in G.nodes():
        draw_cell(node, BG)
        draw_walls(node)

    font = pygame.font.SysFont('Arial', 24)
    text = font.render("ESPACE pour lancer Dijkstra", True, (200, 200, 200))
    screen.blit(text, (10, 10))
    text = font.render("F5 pour réinitialiser", True, (200, 200, 200))
    screen.blit(text, (10, 40))
    text = font.render("ÉCHAP pour quitter", True, (200, 200, 200))
    screen.blit(text, (10, 70))

    pygame.display.flip()

    # Recréer le générateur Wilson
    steps = wilson_steps()


# -----------------------------
# PARAMÈTRES
# -----------------------------
n = 40  # taille de la grille (40x40)
wall = 4  # épaisseur des murs
cell = 20  # taille d'une cellule

# Couleurs
BG = (20, 20, 20)
WALK = (50, 150, 255)
MAZE = (0, 200, 0)
WALL_COLOR = (0, 0, 0)

# -----------------------------
# INITIALISATION PYGAME
# -----------------------------
pygame.init()
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h))
pygame.display.set_caption("Maze")
clock = pygame.time.Clock()

# Centrage du labyrinthe
offset_x = (info.current_w - n * cell) // 2
offset_y = (info.current_h - n * cell) // 2

# -----------------------------
# GRAPHE NETWORKX
# -----------------------------
G = nx.grid_graph([n, n])

# Chaque cellule a 4 murs : N, S, E, W
# On les initialise tous à True
walls = {
    (x, y): {"N": True, "S": True, "E": True, "W": True}
    for x, y in G.nodes()
}

def remove_wall(a, b):
    """Supprime les murs entre deux cellules adjacentes."""
    ax, ay = a
    bx, by = b

    if ax == bx and ay == by + 1:  # a est au sud de b
        walls[a]["N"] = False
        walls[b]["S"] = False
    elif ax == bx and ay == by - 1:  # a est au nord de b
        walls[a]["S"] = False
        walls[b]["N"] = False
    elif ay == by and ax == bx + 1:  # a est à l'est de b
        walls[a]["W"] = False
        walls[b]["E"] = False
    elif ay == by and ax == bx - 1:  # a est à l'ouest de b
        walls[a]["E"] = False
        walls[b]["W"] = False

def draw_cell(node, color):
    x, y = node
    px = offset_x + x * cell
    py = offset_y + y * cell
    pygame.draw.rect(screen, color, (px, py, cell, cell))

def draw_walls(node):
    x, y = node
    px = offset_x + x * cell
    py = offset_y + y * cell

    if walls[node]["N"]:
        pygame.draw.rect(screen, WALL_COLOR, (px, py, cell, wall))
    if walls[node]["S"]:
        pygame.draw.rect(screen, WALL_COLOR, (px, py + cell - wall, cell, wall))
    if walls[node]["W"]:
        pygame.draw.rect(screen, WALL_COLOR, (px, py, wall, cell))
    if walls[node]["E"]:
        pygame.draw.rect(screen, WALL_COLOR, (px + cell - wall, py, wall, cell))

# -----------------------------
# ALGORITHME DE WILSON (GÉNÉRATEUR)
# -----------------------------
maze_edges = []
in_maze = set()

def loop_erased_random_walk(start_node):
    path = [start_node]
    current = start_node

    while current not in in_maze:
        nxt = random.choice(list(G.neighbors(current)))

        if nxt in path:
            idx = path.index(nxt)
            path = path[:idx+1]
        else:
            path.append(nxt)

        current = nxt

        # Animation de la marche
        for node in path:
            draw_cell(node, WALK)
            draw_walls(node)
        pygame.display.flip()
        clock.tick(240)

        yield path

    return path


def wilson_steps():
    start = random.choice(list(G.nodes()))
    in_maze.add(start)

    draw_cell(start, MAZE)
    draw_walls(start)
    pygame.display.flip()

    remaining = set(G.nodes()) - in_maze

    while remaining:
        start_node = random.choice(list(remaining))
        walker = loop_erased_random_walk(start_node)

        try:
            while True:
                yield next(walker)
        except StopIteration as e:
            path = e.value

        # Ajout au labyrinthe
        for i in range(len(path)-1):
            u, v = path[i], path[i+1]
            maze_edges.append((u, v))
            in_maze.add(u)
            in_maze.add(v)

            remove_wall(u, v)

            draw_cell(u, MAZE)
            draw_cell(v, MAZE)
            draw_walls(u)
            draw_walls(v)
            pygame.display.flip()
            clock.tick(240)

        remaining = set(G.nodes()) - in_maze

def neighbors_in_maze(node):
    """Retourne les voisins accessibles (murs ouverts)."""
    x, y = node
    neigh = []
    if not walls[node]["N"]:
        neigh.append((x, y-1))
    if not walls[node]["S"]:
        neigh.append((x, y+1))
    if not walls[node]["W"]:
        neigh.append((x-1, y))
    if not walls[node]["E"]:
        neigh.append((x+1, y))
    return neigh


def dijkstra_visual(start, goal):
    """Solveur visuel Dijkstra."""
    import heapq

    dist = {node: float("inf") for node in G.nodes()}
    prev = {node: None for node in G.nodes()}
    dist[start] = 0

    pq = [(0, start)]
    visited = set()

    while pq:
        d, node = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        # Animation : cellule visitée
        draw_cell(node, (80, 120, 255))  # bleu clair
        draw_walls(node)
        pygame.display.flip()
        clock.tick(300)

        if node == goal:
            break

        for neigh in neighbors_in_maze(node):
            nd = d + 1
            if nd < dist[neigh]:
                dist[neigh] = nd
                prev[neigh] = node
                heapq.heappush(pq, (nd, neigh))

    # Reconstruction du chemin
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()

    # Animation du chemin final
    for node in path:
        draw_cell(node, (255, 220, 0))  # jaune
        draw_walls(node)
        pygame.display.flip()
        clock.tick(200)

    return path

# -----------------------------
# BOUCLE PRINCIPALE
# -----------------------------
screen.fill(BG)
for node in G.nodes():
    draw_cell(node, BG)
    draw_walls(node)

font = pygame.font.SysFont('Arial', 24)
text = font.render("ESPACE pour lancer Dijkstra", True, (200, 200, 200))
screen.blit(text, (10, 10))
text = font.render("F5 pour réinitialiser", True, (200, 200, 200))
screen.blit(text, (10, 40))
text = font.render("ÉCHAP pour quitter", True, (200, 200, 200))
screen.blit(text, (10, 70))

pygame.display.flip()

running = True
steps = wilson_steps()

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Quitter
            if event.key == pygame.K_ESCAPE:
                running = False

            # Lancer Dijkstra
            if event.key == pygame.K_SPACE:
                start = (0, 0)
                goal = (n-1, n-1)
                dijkstra_visual(start, goal)

            # Relancer le programme avec F5
            if event.key == pygame.K_F5:
                reset()


    # Avancer dans Wilson tant qu'il reste des étapes
    try:
        next(steps)
    except StopIteration:
        pass



pygame.quit()
