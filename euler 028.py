def spiral(X, Y, output = False):
    x = y = 0
    dx = 0
    dy = -1
    sumDiagonal = 0 # sum on diagonals
    for i in range(max(X, Y)**2):
        if abs(x) == abs(y):
            sumDiagonal += i+1
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2): # output coordinats
            if output:
                print (x, y)
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy
    return sumDiagonal

print("Sum of the numbers on the diagonals in a 1001 by 1001 spiral formed is %d" % spiral(1001,1001))