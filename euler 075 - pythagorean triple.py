"""
Pythagorean triple (Числа Піфагора)

http://en.wikipedia.org/wiki/Pythagorean_triple
http://codereview.stackexchange.com/questions/25388/speed-up-solution-to-project-euler-problem-75
"""

from collections import Counter
from itertools import count
from timeit import timeit

def gcd(m, n):
    """Return the greatest common divisor of m and n."""
    while n != 0:
        m, n = n, m % n
    return m

def coprime(m, n):
    """Return True iff m and n are coprime."""
    return gcd(m, n) == 1

def all_primitive_triples():
    """Generate all primitive Pythagorean triples, together with a lower
    bound on the perimeter for which all triples have been generated
    so far.
    """
    for m in count(1):
        for n in range(1, m):
            if (m + n) % 2 and coprime(m, n):
                # Euclid's formula
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                q = 2 * m * (m + 1) # P=2m(m+n), q is a lower bound on the perimeter (when n=1)
                yield a, b, c, q

def problem75(limit):
    """Return the number of values of L <= limit such that there is
    exactly one integer-sided right-angled triangle with perimeter
    L.
    """
    triangles = Counter()
    for a, b, c, q in all_primitive_triples():
        if q > limit:
            break
        P = a + b + c
        for i in range(P, limit + 1, P):
            triangles[i] += 1
    return sum(n == 1 for n in triangles.values())

print (problem75(1500000))
print (timeit(lambda: problem75(1500000), number=1))
