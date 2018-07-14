import random
from primes import is_prime


# return (g, x, y) such that a*x + b*y = gcd(x, y)
def gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = gcd(b % a, a)
        return g, x - (b // a) * y, y


def multiplicative_inverse(a, m):
    g, x, y = gcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def get_phi(p, q):
    return (p - 1) * (q - 1)


def get_public_key(phi):
    g = 0
    public_key = 0
    while g != 1:
        public_key = random.randrange(1, phi)
        g = gcd(public_key, phi)[0]
    return public_key


def get_private_key(e, phi):
    return multiplicative_inverse(e, phi)


def get_RSA_keys(p, q):
    if p == q:
        raise Exception('Numbers must be different')
    if (not is_prime(p)) or (not is_prime(q)):
        raise Exception('Numbers must be primes')
    n = p * q
    phi = get_phi(p, q)
    e = get_public_key(phi)
    d = get_private_key(e, phi)
    return (e, n), (d, n)

BYTE_SIZE = 256

def getBlocksFromText(message, blockSize=128):
    # Converts a string message to a list of block integers. Each integer
    # represents 128 (or whatever blockSize is set to) string characters.

    messageBytes = message.encode('ascii') # convert the string to bytes

    blockInts = []
    for blockStart in range(0, len(messageBytes), blockSize):
        # Calculate the block integer for this block of text
        blockInt = 0
        for i in range(blockStart, min(blockStart + blockSize, len(messageBytes))):
            blockInt += messageBytes[i] * (BYTE_SIZE ** (i % blockSize))
        blockInts.append(blockInt)
    return blockInts


def getTextFromBlocks(blockInts, messageLength, blockSize=128):
    # Converts a list of block integers to the original message string.
    # The original message length is needed to properly convert the last
    # block integer.
    message = []
    for blockInt in blockInts:
        blockMessage = []
        for i in range(blockSize - 1, -1, -1):
            if len(message) + i < messageLength:
                # Decode the message string for the 128 (or whatever
                # blockSize is set to) characters from this block integer.
                asciiNumber = blockInt // (BYTE_SIZE ** i)
                blockInt = blockInt % (BYTE_SIZE ** i)
                blockMessage.insert(0, chr(asciiNumber))
        message.extend(blockMessage)
    return ''.join(message)