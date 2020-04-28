import os
import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


# load plaintext file
plaintext_file = input ("Give me the file to encrypt: \n")
readed_file = open("./"+ plaintext_file, "rb").read()
print("\nValue of the plaintext file is: ", readed_file[0:len(readed_file)-1])

# uncomment the following lines to load the private key

# load private key
private_key_filename = input ("\nGive me the file with the key: \n")
with open("./"+ private_key_filename,"rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
         )


# generate public key from private key
public_key = private_key.public_key()


ciphertext = public_key.encrypt(
    readed_file,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\nValue of message_encrypted: ", ciphertext)

plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("\nValue of the decrypted message is: ", plaintext[0:len(plaintext)-1])