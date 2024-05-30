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
    
    def update(self):
        self.alive = self.next_alive
        if self.alive == True:
            self.colour = "#00ff00"
        elif self.alive == False:
            self.colour = "#000000"

def get_neighbours(x, y):
    x, y = int(x/10), int(y/10) # Converts from Pygame coordinates to cell coordinates
    neighbours = [(i, j) for i, j in ((x-1, y-1), (x, y-1), (x+1, y-1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)) if 0 <=i<10 and 0<=j<10]
    return neighbours

def cells_init():
    row = []
    matrix = []
    for i in range(0, 100, 10):
        for j in range(0, 100, 10):
            row.append(Cell(False, get_neighbours(i, j), i, j))
        matrix.append(row)
        row = []

    matrix[0][0].alive = True
    matrix[1][0].alive = True
    matrix[1][1].alive = True
    matrix[0][1].alive = True

    return matrix

def main():
    pygame.init()
    cells = cells_init()
    screen = pygame.display.set_mode((100, 100))
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

        for i in range(10):
            for j in range(10):
                cells[i][j].draw(screen)
                cells[i][j].living_neighbours = 0
                for neighbour in cells[i][j].neighbours:
                    if cells[neighbour[0]][neighbour[1]].alive == True:
                        cells[i][j].living_neighbours += 1

                print("I am cell (" + str(i) + "," + str(j) + ") and I have " + str(cells[i][j].living_neighbours) + " living neighbours.") 
                print("My living neighbours are...\n")
                for neighbour in cells[i][j].neighbours:
                    if cells[neighbour[0]][neighbour[1]].alive == True:
                        print(str(neighbour) + "\n")
                
                print("My neighbours are...\n")
                for neighbour in cells[i][j].neighbours:
                    print(str(neighbour) + "\n")

                print("I have " + str(len(cells[i][j].neighbours)) + " neighbours, alive or dead.")






                if cells[i][j].alive == True and cells[i][j].living_neighbours < 2:
                    cells[i][j].next_alive = False
                elif cells[i][j].alive == True and cells[i][j].living_neighbours == 2:
                    cells[i][j].next_alive = True
                elif cells[i][j].alive == True and cells[i][j].living_neighbours == 3:
                    cells[i][j].next_alive = True
                elif cells[i][j].alive == True and cells[i][j].living_neighbours > 3:
                    cells[i][j].next_alive = False
                elif cells[i][j].alive == False and cells[i][j].living_neighbours == 3:
                    cells[i][j].next_alive = True
                else:
                    cells[i][j].next_alive = False           
  
                
        
        for i in range(10):
            for j in range(10):
                cells[i][j].alive = cells[i][j].next_alive
                if cells[i][j].alive == True:
                    cells[i][j].colour = "#00ff00"
                elif cells[i][j].alive == False:
                    cells[i][j].colour = "#000000"





        pygame.display.flip()
        clock.tick(0.5)

    pygame.quit()


main()
