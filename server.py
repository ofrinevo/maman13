import os
import socket
import threading
from Tkinter import *

import consts
import key_gen
from RSA import RSA


class Server(object):
    def __init__(self, host='', port=8080):
        self.host = host
        self.port = port
        self.conn = None
        self.socket = self._init_socket()
        self.init_new_client()

    def init_new_client(self):
        self._init_rsa()
        self.connect_client()

    def _init_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(1)
        return s

    def _init_rsa(self):
        rsa_keys = key_gen.get_RSA_keys(consts.DEFAULT_KEY_SIZE)
        self.public_keys = rsa_keys[0]
        self.rsa_instance = RSA(n=rsa_keys[1][1], private_key=rsa_keys[1][0])

    def connect_client(self):
        conn, addr = self.socket.accept()
        print 'Connected by', addr
        self.conn = conn
        conn.send('{}'.format(self.public_keys))

    def listen_to_client(self):
        enc_msg = self.conn.recv(10240)
        if not enc_msg:
            print 'User disconnected, waiting for a new one'
            self.conn.close()
            self.conn = None
            return None
        return int(enc_msg)

    def decrypt_msg(self, cipher):
        return self.rsa_instance.decrypt(str(cipher))

    def close(self):
        self.socket.close()


def run_server(host, port):
    try:
        print 'Waiting for client, will open gui after a client connects'
        if host is None or port is None:
            server = Server()
        else:
            server = Server(host, port)
        _gui(server)
    except:
        raise


def _gui(server):
    def handle_clients():
        while True:
            if not server.conn:
                server.init_new_client()
                n_entry.insert(0, server.rsa_instance.n)
            handle_existing_client()
        # root.after(0, handle_clients())

    def handle_existing_client():
        while True:
            enc_msg = server.listen_to_client()
            if not enc_msg:
                return
            dec_msg = server.decrypt_msg(enc_msg)

            cipher_listbox.delete(0, 'end')
            plain_listbox.delete(0, 'end')

            cipher_listbox.insert(0, enc_msg)
            plain_listbox.insert(0, dec_msg)

    def on_closing():
        server.close()
        root.destroy()
        os._exit(0)

    root = Tk()

    root.title('RSA Server')
    n_label = Label(root, text='n: ')
    n_label.pack()

    n_entry = Entry(root, justify='center', width=200)
    n_entry.insert(0, server.rsa_instance.n)
    n_entry.pack()

    show = Label(root, text='Cipher:')
    show.pack()
    cipher_listbox = Entry(root, justify='center', width=200)
    cipher_listbox.pack()

    show_plain = Label(root, text='Plain Text:')
    show_plain.pack()
    plain_listbox = Entry(root, justify='center', width=200)
    plain_listbox.pack()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    t1 = threading.Thread(target=handle_clients)
    t2 = threading.Thread(target=root.mainloop)
    t1.start()
    t2.start()
