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
    for i in range(2, p):
        if gcd(i, p - 1) == 1:
            return i
    raise ValueError("Impossible to find primitive root")


def generate_keypair(bit_length):
    p = gen_prime(bit_length)
    g = get_primitive_root(p)
    sk = random.randint(1, p - 2)
    while gcd(p, sk) != 1:
        sk = random.randint(1, p - 2)
    pk = pow(g, sk, p)
    return pk, sk, g, p
