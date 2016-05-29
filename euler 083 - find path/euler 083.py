"""
Finding the minimal path sum in a matrix from the top left to the bottom right by moving all ways (right, left, up, down).
"""

import sys
#sys.setrecursionlimit(5000)

matrix = [
    [131,673,234,103,18],
    [201,96,342,965,150],
    [630,803,746,422,111],
    [537,699,497,121,956],
    [805,732,524,37,331]
]

matrix = [list(map(int, row.split(","))) for row in open("matrix.txt").read().split("\n")]

n = len(matrix) # size for matrix (works only with square matrix)

minPath = sum([matrix[i][i+j] for i in range(n) for j in range(2) if i+j<n])

paths = dict()

# finding the shortest way using the Dijkstra's algorithm
def findPath(i = 0, j = 0, value = 0, visited = dict()):
    global paths, minPath

    #print(i, j, visited); input();

    # if reach the edge of matrix
    if (i > n-1 or j > n-1 or i < 0 or j < 0):
        return

    # becouse you could go in every direction it is possible to close path and start going in circles
    # to prevent that we need to remember where we've been
    if (i,j) in visited:
        return
    else:
        currentVisited = visited.copy()
        currentVisited[(i,j)] = True

    currentValue = value + matrix[i][j]

    if currentValue >= minPath:
        return

    if i == n-1 and j == n-1 and currentValue < minPath:
        minPath = currentValue
        return
        
    if (i,j) not in paths or currentValue < paths[(i,j)]:
        paths[(i,j)] = currentValue

        findPath(i-1, j, currentValue, currentVisited) # move up
        findPath(i+1, j, currentValue, currentVisited) # move down
        findPath(i, j+1, currentValue, currentVisited) # move right
        findPath(i, j-1, currentValue, currentVisited) # move left

if __name__ == '__main__':
    
    findPath()
    print(minPath)
    
    #print(paths[(n-1, n-1)])

