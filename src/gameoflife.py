import pygame
import random

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
            """
            print(self.living_neighbours < 2)
            print(self.alive)
            print(self.next_alive)
            print("FATAL")
            exit()
            """
    def update(self):
        self.alive = self.next_alive
        if self.alive == True:
            self.colour = "#00ff00"
        elif self.alive == False:
            self.colour = "#000000"
        else:
            print("FATAL ERROR!")


def get_neighbours(x, y):
    x, y = int(x/10), int(y/10) # Converts from Pygame coordinates to cell coordinates
    neighbours = [(i, j) for i, j in ((x-1, y-1), (x, y-1), (x+1, y-1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)) if 0 <=i<50 and 0<=j<50]
    return neighbours

def cells_init():
    row = []
    matrix = []
    for i in range(0, 500, 10):
        for j in range(0, 500, 10):
            row.append(Cell(True, get_neighbours(i, j), i, j))
        matrix.append(row)
        row = []
   # bool(random.getrandbits(3))),
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
                cells[i][j].living_neighbours = 0
                for neighbour in cells[i][j].neighbours:
                    if cells[neighbour[0]][neighbour[1]].alive == True:
                        cells[i][j].living_neighbours += 1
                print("I have... " + str(cells[i][j].living_neighbours))
                cells[i][j].tick()
                
        
        for i in range(50):
            for j in range(50):
                cells[i][j].update()
        
        pygame.display.flip()
        clock.tick(0.5)


    pygame.quit()


main()
