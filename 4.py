from sympy import sieve

# с использованием sympy
def print_primes(limit):
    primes = list(sieve.primerange(2, limit + 1))
    for prime in primes:
        print(prime)

print_primes(30)