from Tkinter import *


def click_enc():
    print plain_text_entry.get()


def click_dec():
    print cipher_text_entry.get()


root = Tk()

root.title('RSA Client')

# label_key_size = Label(root, text='Key Size: ')
# key_size = Entry(root)
# label_key_size.pack()
# key_size.pack()


l = Label(root, text='Plaintext: ')
l.pack()

plain_text_entry = Entry(root)
plain_text_entry.pack()

button_enc = Button(root, text="Encrypt", command=click_enc)
button_enc.pack()

show = Label(root, text='Cipher:')
show.pack()
listbox = Listbox(root, height=1, width=40)
listbox.pack()


label = Label(root, text='Input the ciphertext')
label.pack()

# input ciphertext
cipher_text_entry = Entry(root)
cipher_text_entry.pack()

# click the Decrypt button
button_dec = Button(root, text="Decrypt", command=click_dec)
button_dec.pack()

# show the plaintext info.
show2 = Label(root, text='Show Plaintext:')
show2.pack()
listbox2 = Listbox(root, height=1, width=40)
listbox2.pack()
# ******************ciphertext input ending*****************


root.mainloop()
