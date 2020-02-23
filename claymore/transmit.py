from Crypto.Cipher import AES

pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]

def encrypt(message, password, iv):
    obj = AES.new(password, AES.MODE_CFB, iv)
    ciphertext = obj.encrypt(message)
    return ciphertext

def decrypt(ciphertext, password, iv):
    obj = AES.new(password, AES.MODE_CFB, iv)
    message = obj.decrypt(ciphertext)
    return message

def convert(m, p):
    m = encrypt(m, pad(p), pad("IV"))

    return m

def unconvert(m, p):
    m = decrypt(m, pad(p), pad("IV"))
    m = m.decode("utf8")

    return m
