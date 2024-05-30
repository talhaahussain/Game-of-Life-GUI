def moore(x, y, lower_x, lower_y, upper_x, upper_y):
  neighbours = [(i, j) for i, j in ((x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1))] if lower_x<=i<upper_x and lower_y<=j<upper_y]
  return neighbours
 
def von_Neumann(x, y,  lower_x, lower_y, upper_x, upper_y):
  neighbours = [(i, j) for i, j in ((x, y-1), (x-1, y), (x+1, y), (x, y+1)) if lower_x<=i<upper_x and lower_y<=j<upper_y]
  return neighbours


print(moore(2, 0, 0, 0, 10, 10))
print(len(moore(2, 0, 0, 0, 10, 10)))

