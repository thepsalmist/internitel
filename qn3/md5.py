import hashlib


def encrypt_string(word):
    """
    The function takes a work and returns an encrypted text using MD5 encryption algorithm
    """
    result = hashlib.md5(word.encode())
    print(result.hexdigest())


encrypt_string(word="The best of best")

encrypt_string(word="The test of time")
