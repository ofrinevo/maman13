import random
from primes import is_prime, generate_large_prime


# return (g, x, y) such that a*x + b*y = gcd(x, y)
def gcd(x, y):
    x = abs(x)
    y = abs(y)
    while x > 0:
        x, y = y % x, x
    return y


def multiplicative_inverse(u, v):
    u3, v3 = long(u), long(v)
    u1, v1 = 1L, 0L
    while v3 > 0:
        q = divmod(u3, v3)[0]
        u1, v1 = v1, u1 - v1 * q
        u3, v3 = v3, u3 - v3 * q
    while u1 < 0:
        u1 = u1 + v
    return u1


def get_phi(p, q):
    return (p - 1) * (q - 1)


def generate_public_key(phi):
    g = 0
    public_key = 0
    while g != 1:
        public_key = random.randrange(1, phi)
        g = gcd(public_key, phi)
    return public_key


def generate_private_key(e, phi):
    return multiplicative_inverse(e, phi)


def get_RSA_keys(bit_len, p=None, q=None):
    if p and q:
        if p == q:
            raise Exception('Numbers must be different')
        if (not is_prime(p)) or (not is_prime(q)):
            raise Exception('Numbers must be primes')
    if p is None:
        p = generate_large_prime(bit_len)
    if q is None:
        q = generate_large_prime(bit_len)
    n = p * q
    phi = get_phi(p, q)
    e = generate_public_key(phi)
    d = generate_private_key(e, phi)
    return (e, n), (d, n)
