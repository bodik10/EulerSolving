import myprofiler

def find_palindrome():
    result = []
    counter = 0
    
    for i in range(999, 99, -1):
        j = i + ((999 - i) // 10 * 10)
        
        while j >= i:
            palinNum = i*j
            counter += 1

            if str(palinNum) == str(palinNum)[::-1]:
                print("Iterations:", counter)
                return i, j, palinNum
                
            j -= 10

with myprofiler.profile():
    palindrome = find_palindrome()

print("Largest palindrome made from the product of %dx%d: %d" % palindrome) 
