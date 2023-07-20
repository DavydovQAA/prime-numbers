# Осуществим проверку с помощью встроенной функции any


def prime_numbers(num):
    if num < 2:
        return False
    return not any(num % i == 0 for i in range(2, int(num ** 0.5) + 1))


def print_primes(limit):
    primes = [num for num in range(2, limit + 1) if prime_numbers(num)]
    print(primes)


print_primes(30)
