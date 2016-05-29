"""
Finding the minimal path sum in a matrix from the left column to the right column.
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
minPath = min([sum(row) for row in matrix])
count = 0

# finding the shortest way using the Dijkstra's algorithm
def findPath(i = 0, j = 0, value = 0, direction = ''):
    global paths, minPath, count

    count += 1

    # if reache the edge of matrix
    if (i < 0 or i > n-1 or j > n-1):
        return

    # if you walk down the first column, just set each start element to it's value
    if j == 0:
        value = 0
        
    currentValue = value + matrix[i][j]
    
    if currentValue > minPath:
        return
    
    if (i,j) not in paths or currentValue < paths[(i,j)]:
        paths[(i,j)] = currentValue

        # if reach the right column
        if j == n-1:
            if paths[(i,j)] < minPath:
                minPath = paths[(i,j)]
            return

        findPath(i, j+1, currentValue) # move right
        if direction != 'up':
            findPath(i+1, j, currentValue, direction = 'down') # move down
        if direction != 'down': 
            findPath(i-1, j, currentValue, direction = 'up') # move up

if __name__ == '__main__':

    findPath()   
    print(minPath, count)

