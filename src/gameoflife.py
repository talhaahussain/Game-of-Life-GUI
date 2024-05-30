import pygame
import random

class Cell:
    def __init__(self, alive, neighbours, x, y):
        self.alive = alive
        self.next_alive = None
        self.colour = "#00ff00" if self.alive else "#000000"
        self.neighbours = neighbours
        self.alive_neighbours = None
        self.height = 10
        self.width = 10
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, pygame.Rect((self.x, self.y, self.width-1, self.height-1)))

    def tick():
        if (self.alive == True) and (len(self.alive_neighbours) < 2):
            self.next_alive = False
            return
        if (self.alive == True) and (len(self.alive_neighbours) in [2, 3]):
            self.next_alive = True
            return
        if (self.alive == True) and (len(self.alive_neighbours) > 3):
            self.next_alive = False
            return
        if (self.alive == False) and (len(self.alive_neighbours) == 3):
            self.next_alive = True
            return

    def update():
        self.alive = self.next_alive
        if self.alive == True:
            self.colour = "#00ff00"
        else:
            self.colour = "#000000"


def get_neighbours(x, y):
    x, y = int(x/10), int(y/10) # Converts from Pygame coordinates to cell coordinates
    neighbours = [(i, j) for i, j in ((x-1, y-1), (x, y-1), (x+1, y-1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)) if 0 <=i<50 and 0<=j<50]
    return neighbours

def cells_init():
    row = []
    matrix = []
    for i in range(0, 500, 10):
        for j in range(0, 500, 10):
            row.append(Cell(bool(random.getrandbits(1)), get_neighbours(i, j), i, j))
            print(get_neighbours(i, j))
            print("\n")
        matrix.append(row)
        row = []
    
    return matrix

def main():
    pygame.init()
    cells = cells_init()
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    running = True
    iteration = 0
    while running:
#       print(iteration)
        iteration = iteration + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("white")
        for i in range(50):
            for j in range(50):
                cells[i][j].draw(screen)

        pygame.display.flip()
        clock.tick()


    pygame.quit()


main()
