# ElGamal Algorithm

This is the Python implementation of the ElGamal signature and encryption schemes.

## Key Generation

```python
pk, sk = generate_keypair(2048)
```

## Digital Signature

The ElGamal signature scheme is a digital signature scheme 
based on the algebraic properties of modular exponentiation, 
together with the discrete logarithm problem.

```python
pk, sk = generate_keypair(2048)
signature = sign(message, sk)
is_valid = verify(message, pk, signature)
```

## Encryption

ElGamal encryption system is an asymmetric key encryption algorithm for 
public-key cryptography which is based on the Diffie–Hellman key exchange.

Messages are split into blocks under the hood for the correct encryption and decryption.

```python
pk, sk = generate_keypair(self.bit_length)
ciphertext = encrypt(message, pk)
decrypted = decrypt(ciphertext, sk)
```


## Run Tests

```sh
python3 -m unittest test.py   
```

### Test results

Note, that small key length for tests was chosen for the performance reasons,
but for real usage it is recommended to use a value between 2048 and 4096.

