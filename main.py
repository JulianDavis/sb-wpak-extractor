#!/usr/bin/env python3

import blowfish
from os import listdir, path
from pathlib import Path

base_dir = 'D:\SBReforged'


key = b'\x85\x71\x40\x3C\x14\x50\x0B\x52\x73\x2D\x10\x08\x63\x59\x5B\xAA'
cipher = blowfish.Cipher(key)

def decrypt_dir(src_dir, dest_dir):
    for file in listdir(src_dir):
        if Path(file).suffix != '.zip' and Path(file).suffix != '.txt':
            file = path.join(src_dir, file)
            plaintext = decrypt_file(file)

            with open(f'{dest_dir}\{path.basename(file)}', 'w') as decrypted:
                decrypted.write(plaintext)

def decrypt_file(file):
    with open(file, 'rb') as encrypted:
        ciphertext = encrypted.read()
        iv = ciphertext[:8]

        plaintext = b''.join(cipher.decrypt_cfb(ciphertext[8:], iv))
        try:
            print(plaintext.decode())
        except:
             print(f'Failed to decode file: {file}')

def encrypt_file(file):
    with open(file, 'r') as decrypted:
        plaintext = decrypted.read()
        iv = b'\x25\x7A\x86\x0C\x9D\xE0\x53\x70'

        ciphertext = b''.join(cipher.encrypt_cfb(plaintext.encode(), iv))
        with open('test/Emotes-test.cfg', 'wb') as emotes:
            emotes.write(ciphertext)


#decrypt_file('D:\SBReforged\Config\_Config.wpak.extracted\XPCredits.cfg')
#decrypt_dir(f'{base_dir}\Config\_Transitions.wpak.extracted', 'D:\Documents\Projects\sb-wpak-extractor\Decrypted\Config\Transitions')

encrypt_file('test/Emotes.cfg')
#decrypt_file('test/Emotes-test.cfg')
