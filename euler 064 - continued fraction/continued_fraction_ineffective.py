def findRepeat(l):
    if not l: return l
    for i in range(1, len(l)//2+1):
        part = l[:i]
        offset = len(part)
        while offset <= len(l)-len(part):
            if part != l[offset:offset+len(part)]: break
            offset += len(part)
        else:
            return part 
    return l

# NOT CORRECT RESULT BECAUSE OF THE FLOATING POINT INACCURACY
def contFraction(N):
    a0 = int(N)
    repeat = []
    def findFraction(x):
        nonlocal repeat
        if x == 0: return
        xn = 1/x
        if len(repeat) < 10:
            repeat.append(int(xn))
            findFraction(xn - int(xn))
    findFraction(N-a0)                  
    return a0, repeat, findRepeat(repeat)


if __name__ == "__main__":
    for i in range(2,14):
        print ("\u221a%d =" % i, contFraction(i**0.5))
