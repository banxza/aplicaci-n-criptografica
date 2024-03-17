# Definiendo las funciones proporcionadas por el usuario
def alphabet_loader(language="Inglés"):
    if language == "Inglés":
        alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    elif language == "Español":
        alphabet_upper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        alphabet_lower = "abcdefghijklmnñopqrstuvwxyz"
    else:
        raise ValueError(f"Unsupported language: {language}")

    alphabet = alphabet_upper + alphabet_lower
    return alphabet

def caesar_cipher_encrypt(text, shift, alphabet):
    def shift_alphabet(shift):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabet = shift_alphabet(shift)
    lower_alphabet = alphabet.lower()
    upper_alphabet = alphabet.upper()

    table = str.maketrans(lower_alphabet + upper_alphabet, 
                          shifted_alphabet.lower() + shifted_alphabet.upper())

    encrypted_text = text.translate(table)
    return encrypted_text

def caesar_cipher_decrypt(text, shift, alphabet):
    return caesar_cipher_encrypt(text, shift, alphabet)


