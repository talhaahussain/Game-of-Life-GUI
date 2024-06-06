import pygame
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()

if args.n == "von-neumann" or args.n == "moore":
    neighbour_mode = args.n
else:
    print("Invalid argument. Please try again.\n")
    print("(Hint - Try run the program with \"-n von-neumann\" or \"-n moore\".)\n")
    exit(1)

class Cell:
    def __init__(self, alive, neighbours, x, y):
        self.alive = alive
        self.next_alive = None
        self.colour = "#00ff00" if self.alive else "#000000"
        self.neighbours = neighbours
        self.living_neighbours = 0
        self.height = 10
        self.width = 10
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, pygame.Rect((self.x, self.y, self.width-1, self.height-1)))

    def tick(self):
        if self.alive == True and self.living_neighbours < 2:
            self.next_alive = False
            return
        elif self.alive == True and self.living_neighbours == 2:
            self.next_alive = True
            return
        elif self.alive == True and self.living_neighbours == 3:
            self.next_alive = True
            return
        elif self.alive == True and self.living_neighbours > 3:
            self.next_alive = False
            return
        elif self.alive == False and self.living_neighbours == 3:
            self.next_alive = True
            return
        else:
            self.next_alive = False           
    
    def update(self):
        self.alive = self.next_alive
        if self.alive == True:
            self.colour = "#00ff00"
        elif self.alive == False:
            self.colour = "#000000"

def get_neighbours(x, y):
    x, y = int(x/10), int(y/10) # Converts from Pygame coordinates to cell coordinates
    if neighbour_mode == "moore":
        neighbours = [(i, j) for i, j in ((x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)) if 0<=i<75 and 0<=j<75]
    else:
        neighbours = [(i, j) for i, j in ((x, y-1), (x-1, y), (x+1, y), (x, y+1)) if 0<=i<75 and 0<=j<75]
    return neighbours

def cells_init():
    row = []
    matrix = []
    for i in range(0, 750, 10):
        for j in range(0, 750, 10):
            row.append(Cell(not(bool(random.getrandbits(3))), get_neighbours(i, j), i, j))
        matrix.append(row)
        row = []

    return matrix

def main():
    pygame.init()
    cells = cells_init()
    screen = pygame.display.set_mode((750, 750))
    clock = pygame.time.Clock()
    running = True
    iteration = 0
    while running:
        iteration = iteration + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("white")

        for i in range(75):
            for j in range(75):
                cells[i][j].draw(screen)
                cells[i][j].living_neighbours = 0
                for neighbour in cells[i][j].neighbours:
                    if cells[neighbour[0]][neighbour[1]].alive == True:
                        cells[i][j].living_neighbours += 1
                cells[i][j].tick()
         
        for i in range(75):
            for j in range(75):
                cells[i][j].update()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


main()
