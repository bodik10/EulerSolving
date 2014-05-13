# f = open("names.txt")
# f.close

from urllib.request import urlopen
f = urlopen("http://projecteuler.net/project/names.txt")

names = f.read().decode().replace('"', '').split(",")
names.sort()

scores = []
i = 1
for name in names:
    score = sum([ord(l) - 64 for l in name]) * i
    scores.append(score)
    i += 1

print ("The total of all the name scores in the file is %d" % sum(scores))

maxScore = max(scores)
print ("Name %s has maximum score %d" % (names[scores.index(maxScore)], maxScore))
print ("But ARNOLD only %d :(" % scores[names.index("ARNOLD")])
print ("Some names and their scores:")
for row in zip(names[:25], scores[:25]):
    print (row)
