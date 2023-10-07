#!/usr/bin/env python3

import blowfish
from os import listdir, path
from pathlib import Path

dir = 'Decrypted/Config/'

def repak(dir):
    for file in listdir(dir):
        print(Path(file))

repak(dir)
