# coding=utf-8
import primes
import consts
import key_gen
import RSA


def main():
    print 'Welcome to RSA!'
    bit_len = _get_bit_len_from_user()
    p, q = _get_primes_from_user()
    keys = key_gen.get_RSA_keys(bit_len, p, q)
    n = keys[0][1]
    public_key = keys[0][0]
    private_key = keys[1][0]
    msg = 'שלום ליאור'
    enc = RSA.encrypt_str(msg, public_key, n)
    print enc
    dec = RSA.decrypt_str(enc, private_key, n)
    print dec


def _get_bit_len_from_user():
    while True:
        print 'Please enter the wanted primes size in bits, make sure it is a power of 2. The default is: {}'.format(
            consts.DEFAULT_KEY_SIZE)
        try:
            user_input = raw_input()
            if user_input == '':
                print 'Running with 1024.'
                return consts.DEFAULT_KEY_SIZE
            bit_len = int(user_input)
            return bit_len
        except:
            print 'You entered a non valid number, try again.'


def _get_primes_from_user():
    p, q = None, None
    while True:
        print 'Enter 2 different primes. Default will generate random primes: '
        try:
            print 'Enter the first one: '
            user_input = raw_input()
            if user_input == '':
                print 'Will generate prime.'
                p = None
            else:
                p = int(user_input)
            print 'Enter the second one: '
            user_input = raw_input()
            if user_input == '':
                print 'Will generate prime.'
                q = None
            else:
                q = int(user_input)
        except:
            print 'You entered a non valid number, try again.'
        return p, q


main()
