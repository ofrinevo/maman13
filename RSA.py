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
    print 'longmsg1 is ' + str(long_msg)
    return encrypt_int(long_msg, ekey, n)


def decrypt_str(cypher, dkey, n):
    long_msg = decrypt_int(cypher, dkey, n)
    print 'longmsg2 is ' + str(long_msg)
    return convert_long_to_str(long_msg)
