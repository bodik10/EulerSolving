from collections import defaultdict

start = 4643 # 4643 - smallest number that produces 12-digit cube

# find all cubes from start to 10000
result = []
for n in range(start, 10000): 
    cube = n**3
    cube_dict = {}
    for digit in str(cube):
        cube_dict[digit] = cube_dict.get(digit, 0) + 1 # count every digit in cube
    result.append(cube_dict)
    """
    [{'1': 2, '0': 4, '3': 1, '2': 1, '5': 1, '7': 2, '9': 1},
    {'1': 3, '0': 2, '2': 1, '5': 2, '4': 1, '9': 2, '8': 1},
    {'1': 2, '0': 3, '3': 1, '2': 3, '5': 1, '6': 2},
    {'1': 2, '0': 2, '3': 2, '2': 1, '5': 1, '7': 1, '6': 1, '8': 2},
    {'1': 2, '0': 4, '3': 2, '2': 1, '5': 1, '4': 1, '8': 1}]
    ........."""
        
# count how many permutation of similar digits are in result 
counter = defaultdict(list)
for cube in result:
    count = result.count(cube)
    if cube not in counter[count]:
        counter[count].append(cube)
        
print ("All five permutations of the same digits are cube:")   
for d in counter[5]:
    res = [(i+start)**3 for i in range(len(result)) if result[i] == d]
    print (res)

# the smallest cube for which exactly five permutations of its digits are cube: 127035954683

