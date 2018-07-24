import consts


def convert_str_to_long(s):
    hex_str = s.encode('hex')
    return long(hex_str, 16)


def convert_long_to_str(number):
    hex_int = hex(number)
    stripped_str = hex_int.rstrip('L')
    if hex_int.startswith('0x'):
        stripped_str = stripped_str[2:]
    return stripped_str.decode('hex')


def encrypt_int(message, ekey, n):
    return pow(message, ekey, n)


def decrypt_int(cyphertext, dkey, n):
    return pow(cyphertext, dkey, n)


def encrypt_str(message, ekey, n):
    long_msg = convert_str_to_long(message)
    return encrypt_int(long_msg, ekey, n)


# TODO add support for longer msgs using blocks
def decrypt_str(cypher, dkey, n):
    long_msg = decrypt_int(cypher, dkey, n)
    return convert_long_to_str(long_msg)


class RSA(object):
    def __init__(self, key_size=consts.DEFAULT_KEY_SIZE, p=None, q=None, e=None, d=None):
        self.d = d
        self.e = e
        self.q = q
        self.p = p
        self.key_size = key_size

    def encrypt_str(self, message, ekey, n):
        long_msg = convert_str_to_long(message)
        print 'longmsg1 is ' + str(long_msg)
        return encrypt_int(long_msg, ekey, n)
