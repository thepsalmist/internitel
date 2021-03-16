import hashlib


def encrypt_str(word):
    """
    The function takes a string and returns an hashtext using SHA-2 encryption algorithm
    """
    result = hashlib.sha256(word.encode())
    print(result.hexdigest())


encrypt_str(word="With a method like this")
