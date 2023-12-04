import random


def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Miller-Rabin primality test
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def gen_prime(bit_length):
    while True:
        n = random.randint(2 ** (bit_length - 1), 2 ** bit_length)
        if is_prime(n):
            return n


def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def get_primitive_root(p):
    if p == 2:
        return 1

    factors = prime_factors(p - 1)
    for a in range(2, p):
        if all(pow(a, (p - 1) // f, p) != 1 for f in factors):
            return a
    raise ValueError('No primitive root of %d found' % p)


def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def generate_keypair(bit_length):
    p = gen_prime(bit_length)
    g = get_primitive_root(p)
    sk = random.randint(1, p - 2)
    while gcd(p, sk) != 1:
        sk = random.randint(1, p - 2)
    pk = pow(g, sk, p)
    return pk, sk, g, p
