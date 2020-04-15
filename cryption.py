from cryptography.fernet import Fernet


def generateKey():
    key = Fernet.generate_key()  # generating random key
    return key.decode()


def encryptMessage(givenMessage, key):
    encryptedMessage = Fernet(key).encrypt(givenMessage.encode())  # encrypting the message
    return encryptedMessage.decode()


def decryptMessage(givenMessage, key):
    decryptedMessage = Fernet(key).decrypt(givenMessage)
    return decryptedMessage