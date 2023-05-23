#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Distributed Application - version 1 - lock_client.py
"""
# Zona para fazer imports
import sys
from lock_stub import *
from net_client import *

# Programa principal

client_id = sys.argv[1]
HOST = sys.argv[2]
PORT = int(sys.argv[3])

client = stub(client_id, HOST, PORT)

check = True

while check:
    prompt = input('Comando >')

    if prompt == 'EXIT':
        exit()
        check = False
    else:
        client.connect()
        print(client.send_receive(prompt))
        client.disconnect()
