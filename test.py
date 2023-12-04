import unittest
from keypair_generation import generate_keypair
from digital_signature import sign, verify
from encryption import encrypt, decrypt

class TestElGamalSchemes(unittest.TestCase):

    # small number used for quick testing (works with larger values as well)
    bit_length = 256

    # should sign and verify a message correctly
    def test_signature(self):
        message = "Hello, world!"
        pk, sk = generate_keypair(self.bit_length)
        signature = sign(message, sk)
        self.assertTrue(verify(message, pk, signature))

    # should verify the incorrect signature (changed message) properly
    def test_signature_invalid_message(self):
        message = "Hello, world!"
        wrong_message = "Hello, world"
        pk, sk = generate_keypair(self.bit_length)
        signature = sign(message, sk)
        self.assertFalse(verify(wrong_message, pk, signature))

    # should verify the incorrect signature (changed public key) properly
    def test_signature_invalid_pk(self):
        message = "Hello, world!"
        wrong_message = "Hello, world"
        pk, sk = generate_keypair(self.bit_length)
        wrong_pk, _ = generate_keypair(self.bit_length)
        signature = sign(message, sk)
        self.assertFalse(verify(wrong_message, wrong_pk, signature))

    # should encrypt and decrypt a message correctly
    def test_encryption(self):
        message = "Hello, world!"
        pk, sk = generate_keypair(self.bit_length)
        ciphertext = encrypt(message, pk)
        decrypted = decrypt(ciphertext, sk)
        self.assertEqual(message, decrypted)

    # should encrypt and decrypt a long message correctly
    def test_encryption_long(self):
        message = ('Алгоритм Ель-Гамаля був запропонований Тахіром Ель-Гамалем у 1985 році як '
                   'поліпшена версія алгоритму Діффі-Хеллмана. Він удосконалив систему Діффі-Хеллмана '
                   'і створив два алгоритми – один для шифрування, інший для автентифікації. '
                   'Одна з переваг алгоритму Ель-Гамаля полягає в тому, що він не підлягає патентуванню, '
                   'що робило його доступним і економічно вигідним в порівнянні з RSA, де потрібна '
                   'була ліцензійна оплата до закінчення строку дії патенту у 2000 році')

        pk, sk = generate_keypair(self.bit_length)
        ciphertext = encrypt(message, pk)
        decrypted = decrypt(ciphertext, sk)
        self.assertEqual(message, decrypted)

    # should not allow to decrypt message for another recipient (sk and pk don't match)
    def test_encryption_invalid_pk(self):
        message = "Hello, world!"
        pk, sk = generate_keypair(self.bit_length)
        wrong_pk, _ = generate_keypair(self.bit_length)
        ciphertext = encrypt(message, wrong_pk)
        try:
            decrypted = decrypt(ciphertext, sk)
        except UnicodeDecodeError:
            pass
        else:
            self.assertNotEqual(message, decrypted)
