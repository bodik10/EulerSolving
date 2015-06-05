"What is the first value which can be written as the sum of primes in over five thousand different ways?"

# much the same solution as in problem 031, 076

def primes_generator():
    yield 2
    num = 3
    while True:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0: break
        else:
            yield num
        num += 1
    
def prime_summations(ways_goal):
    
    target = 10

    while True:
        ways = [1] + [0]*target
        for prime in primes_generator():
            if prime >= target: break
            for i in range(prime, target+1):
                ways[i] += ways[i-prime]

                if ways[i] == ways_goal:
                    return i, ways[i]

        target += 1


print(prime_summations(5))
print(prime_summations(5000))
print(prime_summations(10000))
