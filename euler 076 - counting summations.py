"How many different ways can number be written as a sum of at least two positive integers?"

def counting_summations(N):
    count = 0
    index = 0
    summands = [N]
    while len(summands) != N:
        if summands[index] == 1:
            index -= 1
            continue

        summands[index] -= 1
        
        if index+1 > len(summands)-1:
            summands.append(0)
        if summands[index] < summands[index+1] +1:
            summands.append(1)
            index -= 1
        else:
            index += 1
            summands[index] += 1
        
        count += 1

        print(summands, index); input()

    return count

#print(counting_summations(5))
print(counting_summations(100))
