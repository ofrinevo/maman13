# coding=utf-8
import consts
import key_gen
from RSA import RSA


def console_mode():
    print 'Welcome to RSA!'
    p, q = _get_primes_from_user()
    if not p or not q:
        bit_len = _get_bit_len_from_user()
    else:
        bit_len = max(p, q).bit_length()
    keys = key_gen.get_RSA_keys(bit_len, p, q)
    rsa_instance = RSA(n=keys[0][1], public_key=keys[0][0], private_key=keys[1][0], key_size=bit_len)
    while True:
        msg = _get_msg_to_enc()
        if msg == 'exit':
            break
        try:
            enc = rsa_instance.encrypt(msg)
            print 'Enc msg is: {}'.format(enc)
            dec = rsa_instance.decrypt(enc)
            print 'Dec msg is: {}'.format(dec)
        except Exception as e:
            print e


def _get_bit_len_from_user():
    while True:
        print 'Please enter the wanted primes size in bits, make sure it is a power of 2. The default is: {}'.format(
            consts.DEFAULT_KEY_SIZE)
        try:
            user_input = raw_input()
            if user_input == '':
                print 'Running with {}'.format(consts.DEFAULT_KEY_SIZE)
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


def _get_msg_to_enc():
    print 'Please enter a msg to enc or type exit to quit:'
    msg = raw_input()
    return msg
