# coding=utf-8
import socket
import RSA
from Tkinter import *


class Client(object):
    server = None
    public_key = None
    n = None

    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.server = self._init_server()
        try:
            self._get_public_key_from_server()
        except:
            raise

    def _init_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((self.host, self.port))
        return server

    def _get_public_key_from_server(self):
        data = self.server.recv(10240)
        if self._is_public_key(data):
            self.public_key, self.n = self._get_key(data)
        else:
            raise Exception('Bad key form server')

    def close(self):
        self.server.close()

    def send_to_server(self, msg):
        self.server.send(str(msg))

    def _is_public_key(self, data):
        return data.startswith('0 ')

    def _get_key(self, data):
        trimmed_key = data[2:]
        tup_key = eval(trimmed_key)
        return tup_key[0], tup_key[1]

    def encrypt_msg(self, msg):
        return RSA.encrypt_str(msg, self.public_key, self.n)


# def _get_msg_to_enc():
#     print 'Please enter a msg to enc or type exit to exit:'
#     msg = raw_input()
#     return msg


def run_client():
    try:
        client = Client()
    except:
        raise
    _gui(client)
    # while True:
    #     msg = _get_msg_to_enc()
    #     if msg == 'exit':
    #         break
    #     enc_msg = client.encrypt_msg(msg)
    #     client.send_to_server(str(enc_msg))
    # client.close()


def _gui(client):
    def click_enc():
        msg = plain_text_entry.get()
        print msg
        enc = client.encrypt_msg(msg)
        cipher_listbox.insert(0, enc)
        client.send_to_server(str(enc))

    def on_closing():
        client.close()
        root.destroy()

    root = Tk()

    root.title('RSA Client')

    plaintext_label = Label(root, text='Plaintext: ')
    plaintext_label.pack()

    plain_text_entry = Entry(root)
    plain_text_entry.pack()

    button_enc = Button(root, text="Encrypt", command=click_enc)
    button_enc.pack()

    show = Label(root, text='Cipher:')
    show.pack()
    cipher_listbox = Listbox(root, height=1, width=40)
    cipher_listbox.pack()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

# def run_client(self):
#     host = 'localhost'
#     port = 8080
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.connect((host, port))
#     data = server.recv(10240)
#     if self._is_public_key(data):
#         public_key, n = self._get_key(data)
#     else:
#         print 'No good format, exit'
#         return
#     _gui()
#     while True:
#         msg = _get_msg_to_enc()
#         if msg == 'exit':
#             break
#         enc_msg = RSA.encrypt_str(msg, public_key, n)
#         server.send(str(enc_msg))
#     server.close()
