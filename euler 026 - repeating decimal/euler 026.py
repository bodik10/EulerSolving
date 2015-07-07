from myfraction import Myfraction

cycleMax = ""
d = 0
for i in range(1,1001):
    x = Myfraction(1, i)    
    if len(x.recur_cycle) > len(cycleMax):
        cycleMax = x.recur_cycle
        d = i

print("d<1000 for which 1/d contains the longest (%d digits) recurring cycle in its decimal fraction part:\n%s\nd=%s" % (len(cycleMax), cycleMax, d))
