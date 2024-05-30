import pygame

class Cell:
    def __init__(self, neighbours, x, y):
        self.alive = False
        self.next_alive = None
        self.colour = "#000000"
        self.neighbours = neighbours
        self.alive_neighbours = None
        self.height = 10
        self.width = 10
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, pygame.Rect((self.x, self.y, self.width, self.height)))

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


def cells_init():
    row = []
    matrix = []
    for i in range(0, 800, 10):
        for j in range(0, 800, 10):
            row.append(Cell(None, i, j))
        matrix.append(row)
        row = []
    
    return matrix

def main():
    pygame.init()
    cells = cells_init()
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    running = True
    iteration = 0
    while running:
        print(iteration)
        iteration = iteration + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("white")
        for i in range(80):
            for j in range(80):
                cells[i][j].draw(screen)

        pygame.display.flip()
        clock.tick()


    pygame.quit()


main()
