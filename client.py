# coding=utf-8
import socket
from Tkinter import *

from RSA import RSA


class Client(object):
    server = None
    RSA = None

    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.server = self._init_connection_to_server()
        try:
            self._get_public_key_from_server()
        except:
            raise

    def _init_connection_to_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((self.host, self.port))
        return server

    def _get_public_key_from_server(self):
        data = self.server.recv(10240)
        key = self._get_key(data)
        self.RSA = RSA(public_key=key[0], n=key[1])

    def close(self):
        if self.server:
            self.server.close()

    def send_to_server(self, msg):
        self.server.send(str(msg))

    def _get_key(self, data):
        # Parses the received key from the server
        tup_key = eval(data)
        return tup_key[0], tup_key[1]

    def encrypt_msg(self, msg):
        return self.RSA.encrypt(msg.encode('utf-8'))


def run_client(host, port):
    try:
        # Create client instance, and then run GUI
        if host is None or port is None:
            client = Client()
        else:
            client = Client(host, port)
        _gui(client)
    except:
        raise


def _gui(client):
    def click_enc():
        # Handles the click on the encryption button
        msg = plain_text_entry.get()
        if msg:
            enc = client.encrypt_msg(msg)
            cipher_listbox.delete(0, 'end')
            cipher_listbox.insert(0, enc)
            client.send_to_server(str(enc))

    def on_closing():
        client.close()
        root.destroy()

    root = Tk()

    root.title('RSA Client')
    plaintext_label = Label(root, text='Plaintext: ')
    plaintext_label.pack()

    plain_text_entry = Entry(root, justify='center', width=200)
    plain_text_entry.pack()

    button_enc = Button(root, text="Encrypt", command=click_enc)
    button_enc.pack()

    show = Label(root, text='Cipher:')
    show.pack()
    cipher_listbox = Entry(root, justify='center', width=200)
    cipher_listbox.pack()
    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()
