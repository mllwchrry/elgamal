import random
from keypair_generation import generate_keypair, gcd


def text_to_int(text):
    integer_value = int.from_bytes(text.encode(), 'big')
    return integer_value


def int_to_text(n):
    text = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    return text


def split_utf8_integer(integer):
    integer_str = str(integer)
    chunks = []
    i = 0
    while i < len(integer_str):
        # Check if the current byte is the start of a UTF-8 character
        if (ord(integer_str[i]) & 0xC0) != 0x80:
            chunk_size = 1 if (ord(integer_str[i]) & 0x80) == 0 else 2
            chunk = int(integer_str[i:i+chunk_size])
            chunks.append(chunk)
            i += chunk_size
        else:
            raise ValueError("Invalid UTF-8 encoding")
    return chunks


def encrypt(msg, pk):
    y, g, p = pk
    k = random.randint(2, p - 1)

    while gcd(k, p - 1) != 1:
        k = random.randint(2, p - 1)

    cb = []
    m = text_to_int(msg)
    blocks = split_utf8_integer(m)

    a = pow(g, k, p)
    for i in range(len(blocks)):
        cb.append(pow(y, k, p) * blocks[i] % p)

    return a, cb


def decrypt(c, sk):
    x, g, p = sk
    a, cb = c
    result = ''
    for i in range(len(cb)):
        decrypted = cb[i] * pow(a, p - 1 - x, p) % p
        result += str(decrypted)

    return int_to_text(int(result))
