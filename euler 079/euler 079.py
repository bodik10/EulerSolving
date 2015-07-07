keylogs = list(map(lambda x: list(map(int, x.strip())), open('keylog.txt').readlines()))

print(keylogs)

all_digits = list({j for i in keylogs for j in i}) # [0,1,2,3,6,7,8,9]

"""
e.g.
[3,1,0]
    3 -> [0,1,2,3,6,7,8,9]
    1 -> [0,3,2,1,6,7,8,9]
    0 -> [1,3,2,0,6,7,8,9]

    position of digits in right order: [1,0,3]
    1 !< 0 < 3, so do it again:
    
    3 -> [1,3,2,0,6,7,8,9]
    1 -> [3,1,2,0,6,7,8,9]
    0 -> [3,1,2,0,6,7,8,9]

    0 < 1 < 3 CORRECT! Go to next key in keylogs
"""
for key in keylogs:
    digit_pos = [0,0,0]
    while not (digit_pos[0] < digit_pos[1] < digit_pos[2]):
        digit_pos = [all_digits.index(key[0])]
        for i in range(1, 3):
            index = all_digits.index(key[i])
            digit_pos.append(index)
            if index < digit_pos[i-1]:
                all_digits[index], all_digits[digit_pos[i-1]] = all_digits[digit_pos[i-1]], all_digits[index]
                digit_pos[i], digit_pos[i-1] == digit_pos[i-1], digit_pos[i]

            #print(digit_pos)
            #print(all_digits); input()

print(all_digits)
