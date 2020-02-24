from Crypto.Cipher import AES
from hashlib import sha512

index = 0

def encrypt(message, password):
    global index
    iv = sha512((password + str(index*2)).encode("utf8")).digest() 
    password = sha512((password + str(index)).encode("utf8")).digest() 
    obj = AES.new(password[0:32], AES.MODE_CFB, iv[0:16])
    ciphertext = obj.encrypt(message)
    return ciphertext

def decrypt(ciphertext, password):
    global index
    iv = sha512((password + str(index*2)).encode("utf8")).digest() 
    password = sha512((password + str(index)).encode("utf8")).digest() 
    obj = AES.new(password[0:32], AES.MODE_CFB, iv[0:16])
    message = obj.decrypt(ciphertext)
    return message

def convert(m, p):
    global index
    m = encrypt(m, p)
    index += 1

    return m

def unconvert(m, p):
    global index
    m = decrypt(m, p)
    m = m.decode("utf8")
    index += 1

    return m
