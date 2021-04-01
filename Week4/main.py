"""
HTCS6702 Cryptography - Week 4 Homework

NOTE: This implementation of encryption has security flaws but the code is kept as short as possible for educational purposes.


See documentation at: 
    https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption.html#cryptography.hazmat.primitives.ciphers.Cipher
"""
import binascii
import random
import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import fire


"""
Base64 is a way for us to encode bytes into an ASCII string. In this homework exercise you'll learn how base64 encoding/decoding works, how to use your operating system's cryptographically-secure pseudorandom number generator (CSPRNG) and how to encrypt/decrypt using AES-ECB mode (insecure, but the easiest to use for this homework).

    Tasks:
        Take the plaintext message "Hello from Firstname-IDNumber." and convert it to bytes.
            e.g. "Hello from Alice-12345678."
        Generate a random key and display the key as base64.
        Encrypt the bytes with AES-ECB using the random key.
        Encode the bytes with base64 and email me the base64-encoded ciphertext.

        Decrypt the following base64-encoded ciphertext with the key 


        Email me the following things:
            - Your base64-encoded ciphertext and key from above.
            - Your decoded 


"""


# You don't need to change this function.
def base64_encode(data):
    """Encodes data (in bytes format) into base-64 encoding."""
    if isinstance(data, str):
        data = bytes(data.encode('ascii'))

    #encoded_data = base64.encodebytes(data).strip()  # Remove newline character on end
    encoded_data = base64.b64encode(data)
    return encoded_data


# You don't need to change this function.
def base64_decode(data):
    """Decodes data (in base-64 format) into bytes encoding."""
    if isinstance(data, str):
        data = bytes(data.encode('ascii'))

    #decoded_data = base64.decodebytes(data)
    decoded_data = base64.b64decode(data)
    return decoded_data


# You don't need to change this function.
def message_to_bytes(message):
    """
    This function adds padding to the message.

    See documentation at https://cryptography.io/en/latest/hazmat/primitives/padding.html
     if you're curious how it works.
    """
    print(f'Unpadded message: {message}')
    padder = padding.PKCS7(128).padder()
    message_as_bytes = bytes(message.encode('ascii'))
    padded_message = padder.update(message_as_bytes) + padder.finalize()
    print(f'Padded message: {padded_message}')

    return padded_message


# You don't need to change this function.
def remove_pkcs7_padding(padded_data):
    """
    Removes PKCS7 Padding.
    """
    if isinstance(padded_data, str):
        print(f'Removing padding for: {padded_data}')
        # String: ascii -> bytes -> escape unicode chars
        padded_data = bytes(padded_data.encode('ascii'))
        print(f'padded_data as bytes: {padded_data}')
        padded_data = padded_data.decode('unicode_escape').encode('ascii')

    print(f'Removing PKCS7 padding for: {padded_data}')
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data)
    data = data + unpadder.finalize()
    print(f'Data without padding: {data}')
    return data


"""
Make these functions work.
"""

# Make this function work.
def generate_key():
    """
    This function should generate a random 16-byte (128-bit) encryption key.
    """
    # TODO: Generate a random 16-byte (128-bit) encryption key. (Hint: 1 line of code required)
    # See here for a hint: https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption.html
    key = b'password12345678'  # TODO: We need to use a good source of randomness for our key.

    print(f'Your {len(key)*8}-bit key as bytes is: {key}')
    return key


def encrypt(message):
    """Takes a message and uses a 128-bit AES key in ECB mode to encrypt the message."""

    print(f'Plaintext message to encrypt is: {message}')

    print('Generating a key:')

    # TODO: Generate and display a key using a function from above. (Hint: 1 line of code required)
    key = b'password12345678' # TODO: You must use the function above to generate a key.


    print(f'Key: {key}')


    # TODO: Encode the key as base64 using a function from above. (Hint: 1 line of code required)
    base64_encoded_key = 'TODO'
    print(f'\nBase64 encoded key: {base64_encoded_key}\n')


    # TODO: Convert the message to bytes using a function from above. (Hint: 1 line of code required)
    message = b'TODO'


    # Create a new 'cipher' instance using AES (with the above key) and ECB mode. (Hint: 1 line of code required)
    # ECB mode doesn't need an initialization vector (iv) so just type modes.ECB()
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    

    # TODO: Create an 'encryptor'. (Hint: 1 line of code required)
    encryptor = 'TODO'


    # TODO: Update the encryptor with your message and finalize the encryptor. (Hint: 1 line  of code required)
    ciphertext = 'TODO'

    # TODO: Run 'finalize()' on the encryptor. (Hint: 1 line of code required)
    ciphertext = 'TODO'  # Add ciphertext from above to encryptor.finalize() like in the documentation examples.


    # Print the ciphertext
    print(f'Ciphertext: {ciphertext}')

    # TODO: Display the base-64 encoded ciphertext. (Hint: 1 line of code required)
    base64_encoded_ciphertext = 'TODO - This is not base64 encoded yet.'


    # Print the base64 encoded ciphertext.
    print(f'\nBase64 encoded key: {base64_encoded_key}\n')
    print(f'Base64 encoded ciphertext: {base64_encoded_ciphertext}')


def decrypt(key, ciphertext):
    """
    Uses AES-ECB with base64-encoded 128-bit key to decrypt base64-encoded ciphertext.
    """

    print('=== Decrypting ===')
    print(f'Key as base64: {key}')

    # TODO: Decode the key from base64 into bytes using a function from above. (Hint: 1 line of code required)
    key_as_bytes = 'TODO - Decode the key from base64 to bytes using the function above'

    print(f'\nKey as bytes: {key_as_bytes}\n')

    # TODO: Decode the ciphertext from base64 into bytes using a function from above. (Hint: 1 line of code required)
    print(f'Decoding ciphertext as bytes: {ciphertext}')
    ciphertext_as_bytes = 'TODO - Decode the ciphertext from base64 to bytes using the function above'
    print(f'Decoded ciphertext as bytes: {ciphertext_as_bytes}')

    # TODO: Create an AES-ECB cipher instance using the decoded key. (Hint: 1 line of code required)
    # Use modes.ECB() instead of modes.CBC(iv) from the example.
    print('Create new Cipher()')
    cipher = 'TODO'

    print('Create decryptor')
    # TODO: Create a 'decryptor' instance. (Hint: 1 line of code required)
    decryptor = 'TODO'
    
    print('Updating decryptor')
    # TODO: Use the decryptor to decrypt (and finalize) the ciphertext. (Hint: 2 lines of code required).
    plaintext_with_padding = 'TODO - Update the decryptor with the ciphertext. See docs for help.'
    final_plaintext = 'TODO - Finalize the decryptor'
    plaintext_with_padding = final_plaintext

    print(f'Plaintext with padding looks like: {plaintext_with_padding}')

    # TODO: Remove the padding using a function from above. (Hint: 1 line of code required).
    plaintext = 'TODO - Remove PKCS7 padding from the plaintext.'

    print('\n\n')
    print(f'Decrypted plaintext: {plaintext}')



"""NOTE: You don't need to change anything beneath this line."""
if __name__ == '__main__':
    fire.Fire(name='main')
