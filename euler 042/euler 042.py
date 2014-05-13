f = open("words.txt")
words = f.read().split(",")
f.close()

triangles = [sum(range(i+1)) for i in range (1, 30)] # 29 triangle numbers (29th number is 435, this is more than enough: in file max word has 192)

triangle_words = []
for word in words:
    N = sum([ord(char)-64 for char in word[1:-1]])
    if N in triangles:
        triangle_words.append((word[1:-1], N))

print ("There are %d triangle words in file 'words.txt'" % len(triangle_words))
print (triangle_words)