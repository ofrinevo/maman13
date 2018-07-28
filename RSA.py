import consts


def convert_str_to_long(s):
    # RSA needs the msg to be an integer
    hex_str = s.encode('hex')
    return long(hex_str, 16)


def convert_long_to_str(number):
    # Converts msg from long to string, because that's what the user wants.
    hex_int = hex(number)
    stripped_str = hex_int.rstrip('L')
    if hex_int.startswith('0x'):
        stripped_str = stripped_str[2:]
    return stripped_str.decode('hex')


def _encrypt_int(message, public_key, n):
    return pow(message, public_key, n)


def _decrypt_int(cipher, private_key, n):
    return pow(cipher, private_key, n)


def _encrypt_str(message, public_key, n):
    long_msg = convert_str_to_long(message)
    return _encrypt_int(long_msg, public_key, n)


def _decrypt_str(cipher, private_key, n):
    long_msg = _decrypt_int(cipher, private_key, n)
    return convert_long_to_str(long_msg)


class RSA(object):
    """
    Uses the given inputs to encrypt and decrypt msgs.
    """

    def __init__(self, n=None, public_key=None, private_key=None, key_size=consts.DEFAULT_KEY_SIZE):
        self.key_size = key_size
        self.n = n
        self.private_key = private_key
        self.public_key = public_key

    def encrypt(self, data):
        try:
            # In order to encrypt long msgs, divides the msg into blocks of manageable size
            block_size = self.key_size / 4
            data_stream = (data[i:i + block_size] for i in range(0, len(data), block_size))
            enc = b''
            for block in data_stream:
                # Encrypt each block and concat it
                enc_block = str(_encrypt_str(block, self.public_key, self.n))
                enc += enc_block + ','
            enc = enc[:-1]
            return enc
        except Exception as e:
            raise Exception('Had an error encrypting', e)

    def decrypt(self, data):
        try:
            data_stream = data.split(',')
            dec = b''
            for block in data_stream:
                # Decrypt each block
                dec += _decrypt_str(int(block), self.private_key, self.n)
            return dec
        except:
            raise Exception('Had an error decrypting')
