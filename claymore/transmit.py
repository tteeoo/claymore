from Crypto.Cipher import AES
from hashlib import pbkdf2_hmac

index = 0

def encrypt(message, password):
    global index
    iv = pbkdf2_hmac("sha256", bytes(password, "utf8"), (index*2).to_bytes(16, byteorder="big"), 200000, dklen=16).hex()
    key = pbkdf2_hmac("sha256", bytes(password, "utf8"), index.to_bytes(16, byteorder="big"), 200000, dklen=32).hex()
    obj = AES.new(key[0:32], AES.MODE_CFB, iv[0:16])
    ciphertext = obj.encrypt(message)
    return ciphertext

def decrypt(ciphertext, password):
    global index
    iv = pbkdf2_hmac("sha256", bytes(password, "utf8"), (index*2).to_bytes(16, byteorder="big"), 200000, dklen=16).hex()
    key = pbkdf2_hmac("sha256", bytes(password, "utf8"), index.to_bytes(16, byteorder="big"), 200000, dklen=32).hex()
    obj = AES.new(key[0:32], AES.MODE_CFB, iv[0:16])
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
