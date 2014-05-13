pyram = []

for row in open("pyramide.txt"):
    pyram.append( list( map(int, row[:-1].split(" ")) ) )
    
all_paths = []
all_sums = []


def find_paths(path = [], row = 0, index = 0):
    global all_paths
    
    current_path = path[:]
    
    current_path.append( pyram[row][index] )
    
    if len(current_path) != len(pyram):
        find_paths(current_path, row + 1, index)
        find_paths(current_path, row + 1, index + 1)
    else:
        all_paths.append(current_path)

        
def find_sums(sum = 0, row = 0, index = 0):
    global all_sums
    
    current_sum = sum    
    current_sum += pyram[row][index]
    
    if row != len(pyram) - 1:
        find_sums(current_sum, row + 1, index)
        find_sums(current_sum, row + 1, index + 1)
    else:
        all_sums.append(current_sum)
    
        
        
find_paths()
find_sums()
    
print(len(all_paths)) 
print(all_paths[:5])


print(len(all_sums))
maxSum = max(all_sums)
print("The maximum total from top to bottom of the triangle below: %d" % maxSum)

print("Max path:", all_paths[all_sums.index(maxSum)])