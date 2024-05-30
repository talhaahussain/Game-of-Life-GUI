def get_neighbours(x, y):
    neighbours = [(i, j) for i, j in ((x-1, y-1), (x, y-1), (x+1, y-1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)) if 0 <=i<50 and 0<=j<50]
    return neighbours

print(get_neighbours(50, 50))
