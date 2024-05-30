import pygame

class Cell:
    def __init__(self, neighbours, x, y):
        self.alive = False
        self.neighbours = neighbours
        self.alive_neighbours = alive_neighbours
        self.x = x
        self.y = y

    def tick():
        if (self.alive == True) and (len(self.alive_neighbours) < 2):
            self.alive = False
            return
        if (self.alive == True) and (len(self.alive_neighbours) in [2, 3]):
            return
        if (self.alive == True) and (len(self.alive_neighbours) > 3):
            self.alive = False
            return
        if (self.alive == False) and (len(self.alive_neighbours) == 3):
            self.alive = True
            return

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 500))
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")
        pygame.display.flip()
        clock.tick()


    pygame.quit()


main()
