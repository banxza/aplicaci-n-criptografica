from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import binascii

def encrypt_message_cbc(plain_text):
    key = os.urandom(32)  # AES-256 requiere una clave de 32 bytes genera una clave aleatoria
    iv = os.urandom(16)   # AES-CBC requiere un IV de 16 bytes  genera un vector de inicializaciónm es necesario en el CBC porqe cifra desde un bloque de texto

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend()) #Crea un objeto de cifrado para usar la encriptación aes
    encryptor = cipher.encryptor() #Inicializa el cifrador 

    padder = padding.PKCS7(128).padder()
    padded_plain_text = padder.update(plain_text.encode()) + padder.finalize()

    encrypted_message = encryptor.update(padded_plain_text) + encryptor.finalize()

    return iv, key, encrypted_message

def decrypt_message_cbc(encrypted_message_hex, key_hex, iv_hex):
    encrypted_message = binascii.unhexlify(encrypted_message_hex)
    key = binascii.unhexlify(key_hex)
    iv = binascii.unhexlify(iv_hex)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_message) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return unpadded_data.decode('utf-8')


# Función para cifrar un mensaje
def encrypt_message_ecb(plaintext, key):
    # Asegurarse de que la clave tenga la longitud adecuada (16, 24, o 32 bytes para AES)
    backend = default_backend()
    key = key.ljust(32, b'\0')[:32]  # Ejemplo de ajuste de la longitud de la clave

    # Crear un objeto Cipher con AES en modo ECB
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()

    # Padding del texto plano para que sea múltiplo del tamaño de bloque
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    # Cifrar el texto plano
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return encrypted_data.hex()

# Función para descifrar un mensaje
def decrypt_message_ecb(encrypted_hex, key):
    # Convertir el texto cifrado hexadecimal en bytes
    encrypted_data = bytes.fromhex(encrypted_hex)

    # Asegurarse de que la clave tenga la longitud adecuada
    backend = default_backend()
    key = key.ljust(32, b'\0')[:32]  # Ejemplo de ajuste de la longitud de la clave

    # Crear un objeto Cipher con AES en modo ECB
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()

    # Desencriptar los datos cifrados
    padded_plaintext = decryptor.update(encrypted_data) + decryptor.finalize()

    # Quitar el padding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode('utf-8')