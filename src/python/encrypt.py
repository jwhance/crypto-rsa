import rsa

def loadKeys():
    with open('keys/publicKey.pem', 'rb') as p:
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


# generateKeys()
loadKeys()