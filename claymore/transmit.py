from Crypto.Cipher import AES
from hashlib import sha512

pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]
index = 0

def encrypt(message, password):
    global index
    iv = sha512((password + str(index*2)).encode("utf8")).digest() 
    password = sha512((password + str(index)).encode("utf8")).digest() 
    obj = AES.new(password, AES.MODE_CFB, iv[0:15])
    ciphertext = obj.encrypt(message)
    index += 1
    return ciphertext

def decrypt(ciphertext, password, iv):
    global index
    iv = sha512((password + str(index*2)).encode("utf8")).digest() 
    password = sha512((password + str(index)).encode("utf8")).digest() 
    obj = AES.new(password, AES.MODE_CFB, iv[0:15])
    message = obj.decrypt(ciphertext)
    index += 1
    return message

def convert(m, p):
    m = encrypt(m, p)

    return m

def unconvert(m, p):
    m = decrypt(m, p)
    m = m.decode("utf8")

    return m
