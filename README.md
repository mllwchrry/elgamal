# ElGamal Algorithm

This is the Python implementation of the ElGamal signature and encryption schemes.

## Key Generation

<img width="551" alt="keys" src="https://github.com/mllwchrry/elgamal/assets/72436706/74e0dd68-d6a4-4984-9210-879f3aeeb879">

```python
pk, sk = generate_keypair(2048)
```

## Digital Signature

The ElGamal signature scheme is a digital signature scheme 
based on the algebraic properties of modular exponentiation, 
together with the discrete logarithm problem.

<img width="551" alt="keys" src="https://github.com/mllwchrry/elgamal/assets/72436706/de3c2152-8338-4d88-9bc9-c59a0abe82f4">


```python
pk, sk = generate_keypair(2048)
signature = sign(message, sk)
is_valid = verify(message, pk, signature)
```

## Encryption

ElGamal encryption system is an asymmetric key encryption algorithm for 
public-key cryptography which is based on the Diffie–Hellman key exchange.

<img width="551" alt="keys" src="https://github.com/mllwchrry/elgamal/assets/72436706/c558a56d-3d59-46d2-a6f4-eb384a682588">


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


<img width="551" alt="test results" src="https://github.com/mllwchrry/elgamal/assets/72436706/3266fbc3-d37c-4171-aac2-69caba2f9111">
