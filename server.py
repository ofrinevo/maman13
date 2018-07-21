# Echo server program
import socket

import RSA
import consts
import key_gen


def run_server():
    host = ''
    port = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print 'Creating rsa keys'
    rsa_keys = _init_server_rsa()
    print 'Done making rsa keys, can connect client'
    conn, addr = s.accept()
    print 'Connected by', addr
    conn.send('0 {}'.format(rsa_keys[0]))
    while True:
        print 'Ready to receive msgs from client'
        enc_msg = conn.recv(10240)
        if not enc_msg:
            print 'User disconnected, exiting'
            break
        plain_text = RSA.decrypt_str(int(enc_msg), rsa_keys[1][0], rsa_keys[1][1])
        print plain_text
    conn.close()


def _init_server_rsa():
    print 'Welcome to RSA Server!'
    p, q = _get_primes_from_user()
    if not p or not q:
        bit_len = _get_bit_len_from_user()
    else:
        bit_len = consts.DEFAULT_KEY_SIZE / 4
    keys = key_gen.get_RSA_keys(bit_len, p, q)
    return keys


def _get_bit_len_from_user():
    while True:
        print 'Please enter the wanted primes size in bits, make sure it is a power of 2. The default is: {}'.format(
            consts.DEFAULT_KEY_SIZE)
        try:
            user_input = raw_input()
            if user_input == '':
                print 'Running with {}.'.format(consts.DEFAULT_KEY_SIZE)
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
