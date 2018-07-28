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


def decrypt_int(cipher, dkey, n):
    return pow(cipher, dkey, n)


class RSA(object):
    def __init__(self, n=None, public_key=None, private_key=None, key_size=consts.DEFAULT_KEY_SIZE):
        self.key_size = key_size
        self.n = n
        self.private_key = private_key
        self.public_key = public_key

    def _encrypt_str(self, message):
        long_msg = convert_str_to_long(message)
        return encrypt_int(long_msg, self.public_key, self.n)

    def _decrypt_str(self, cipher):
        long_msg = decrypt_int(cipher, self.private_key, self.n)
        return convert_long_to_str(long_msg)

    def encrypt(self, data):
        try:
            block_size = self.key_size / 4
            data_stream = (data[i:i + block_size] for i in range(0, len(data), block_size))
            enc = b''
            for block in data_stream:
                enc_block = str(self._encrypt_str(block))
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
                dec += self._decrypt_str(int(block))
            return dec
        except:
            raise Exception('Had an error decrypting')
