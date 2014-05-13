import math
import sys
 
 
def is_prime(num):
    """Checks if num is prime number"""
    for i in range(2, int(math.sqrt(num)) + 1):
        if not num % i:
            return False
    return True
 
 
def find_prime_factors(num):
    """Find prime factors of num"""
    if is_prime(num):
        print("The largest prime factor: %d" % num)
        return
    for i in range(int(math.sqrt(num)) + 1, 1, -1):
        if not num % i and is_prime(i):
            print("The largest prime factor: %d" % i)
            return
    
    # return
 
 
if __name__ == '__main__':
    try:
        num = int(input("Enter number: "))
    except (TypeError, ValueError, IndexError):
        sys.exit("Usage: euler_3.py number")
    if num < 1:
        sys.exit("Error: number must be greater than zero")
 
    find_prime_factors(num)

