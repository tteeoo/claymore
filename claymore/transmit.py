from Crypto.Cipher import AES
from hashlib import pbkdf2_hmac, sha256

index = 0

def encrypt(message, password):
    global index
    key = sha256((password + str(index**9)).encode("utf8")).digest()
    iv = key[0:16]
    obj = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = obj.encrypt(message)
    return ciphertext

def decrypt(ciphertext, password):
    global index
    key = sha256((password + str(index**9)).encode("utf8")).digest()
    iv = key[0:16]
    obj = AES.new(key, AES.MODE_CFB, iv)
    message = obj.decrypt(ciphertext)
    return message

def convert(m, p):
    global index
    m = bytes(m, "utf8")
    m = encrypt(m, p)
    index += 1

    return m

def unconvert(m, p):
    global index
    m = decrypt(m, p)
    try:
        m = m.decode("utf8")
    except UnicodeDecodeError:
        return "Error: Cannot decode message"

    index += 1

    return m

def hashpass(password):
    password = pbkdf2_hmac("sha256", bytes(password, "utf8"), (123456789).to_bytes(16, byteorder="big"), 200000).hex()
    return password
