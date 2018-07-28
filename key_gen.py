from primes import is_prime, generate_large_prime


def gcd(x, y):
    x = abs(x)
    y = abs(y)
    while x > 0:
        x, y = y % x, x
    return y


# This method is taken from the internet. I needed a really fast method here so this is from PyCrypto
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
    public_key = 3
    while True:
        if gcd(public_key, phi) == 1:
            return public_key
        public_key += 1


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
