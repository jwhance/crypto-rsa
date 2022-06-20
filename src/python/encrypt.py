import base64
import rsa

# Convert keys from PCKS#8 to PKCS#1 and back
# https://stackoverflow.com/questions/18039401/how-can-i-transform-between-the-two-styles-of-public-key-format-one-begin-rsa

# RSA Cryto in Python
# https://www.section.io/engineering-education/rsa-encryption-and-decryption-in-python/


def loadKeys():
    with open('keys/rsapublicKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('keys/privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return privateKey, publicKey


def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open('keys/pubKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('keys/privKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))


def rsa_decrypt(ciphertext, key):
    # Base64 decode ciphertext
    b64_decoded = base64.b64decode(ciphertext)

    try:
        # Decrypt and then return an ASCII string from the bytes returned by
        return rsa.decrypt(b64_decoded, key).decode('ascii')

    except Exception as e:
        print(e)
        return False


CIPHERTEXT = 'ji4gBygY5OcJ69XPvhm7asNM61s5CCVU6RVW3uyUQqcO37kXvKX/5J25L6OPXQj5Vb767csza1Qcb92CYMWrHk4YSQGIeUgbni86JpnB1WxQv4nhkl9LsxO3LzKdnP7OtTMRUU+Q3mKszgGRuCZwxklmxaAveh/qcYTT8R8v6nM='

# generateKeys()
privateKey, publicKey = loadKeys()
print('Loaded keys')

plaintext = rsa_decrypt(CIPHERTEXT, privateKey)
print('Plaintext:', plaintext)
