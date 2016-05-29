"""
Finding the minimal path sum in a matrix from the top left to the bottom right by only moving right and down.
"""

matrix = [
    [131,673,234,103,18],
    [201,96,342,965,150],
    [630,803,746,422,111],
    [537,699,497,121,956],
    [805,732,524,37,331]
]

matrix = [list(map(int, row.split(","))) for row in open("matrix.txt").read().split("\n")]

n = len(matrix) # size for matrix (works only with square matrix)

paths = dict()

shortestPath = []

# finding the shortest way using the Dijkstra's algorithm
def findPath(i = 0, j = 0, value = 0, path = []):
    global paths, shortestPath

    # if reache the edge of matrix
    if (i > n-1 or j > n-1):
        return

    currentValue = value + matrix[i][j]

    my_path = path[:]
    
    if (i,j) not in paths or currentValue < paths[(i,j)]:
        paths[(i,j)] = currentValue

        # find an actual path ONLY from the top left to the bottom right 
        my_path.append(matrix[i][j])
        if i == n-1 and j == n-1:
            shortestPath = my_path

        findPath(i+1, j, currentValue, my_path) # move down
        findPath(i, j+1, currentValue, my_path) # move_right

if __name__ == '__main__':
    
    findPath()

    print(paths[(n-1, n-1)])
    print("Shortest path is: ", shortestPath)
