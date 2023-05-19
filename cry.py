import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def encrypt_file(file_path, key):

    iv = os.urandom(16)


    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())


    with open(file_path, 'rb') as file:
        file_content = file.read()


    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(file_content) + padder.finalize()


    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    
    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(iv + encrypted_data)

    print('Arquivo criptografado com sucesso:', encrypted_file_path)



file_path = 'caminho/para/o/arquivo.txt'


key = b'chave_de_16_bytes'


encrypt_file(file_path, key)
