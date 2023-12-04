import hashlib
import random
from keypair_generation import generate_keypair, gcd


def sign(m, sk):
    k = random.randint(2, p - 1)
    r = pow(g, k, p)
    h = int(hashlib.sha256(m.encode()).hexdigest(), 16)

    while gcd(k, p - 1) != 1:
        k = random.randint(2, p - 1)
        r = pow(g, k, p)
        h = int(hashlib.sha256(m.encode()).hexdigest(), 16)

    s = ((h - sk * r) * pow(k, -1, p - 1)) % (p - 1)

    return r, s


def verify(m, pk, signature):
    r, s = signature
    if (1 < r < p - 1) and (0 < s < p - 1):
        h = int(hashlib.sha256(m.encode()).hexdigest(), 16)
        v1 = (pow(pk, r, p) * pow(r, s, p)) % p
        v2 = pow(g, h, p)
        return v1 == v2

    return False


pk, sk, g, p = generate_keypair(32)

message = 'Hello, World!'
message1 = 'Hello, World'
signature = sign(message, sk)
is_valid = verify(message, pk, signature)

print(f"signature: {signature}")
print(f"verification: {is_valid}")
