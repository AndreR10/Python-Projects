#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_server.py
Grupo: 14
Números de aluno: 53299
"""

# Zona para fazer importação
import sys
import time
import sock_utils
import socket as s
import select
import struct
from lock_skel import lock_skel
from lock_pool import lock_pool


###############################################################################


# código do programa principal
if len(sys.argv) == 6:
    try:
        HOST = '127.0.0.1'
        PORT = int(sys.argv[1])
        N = int(sys.argv[2])
        K = int(sys.argv[3])
        Y = int(sys.argv[4])
        T = int(sys.argv[5])

        print('HOST: %s' % (HOST))
        print('PORT: %i' % (PORT))
        print('Poll size: %i' % (N))
        print('Locks per resource: %s' % (K))
        print('Max resources locked: %s' % (Y))
        print('Max time per lock: %s' % (T))      

    except ValueError:
        print("All the arguments need to be type INT.")
        exit(1)
else:
     print("Missing Arguments")

ListenSocket = sock_utils.create_tcp_server_socket(HOST, PORT, 1)
SocketList = [ListenSocket, sys.stdin]
skel = lock_skel(N, K, Y, T)
flag = True
li = []

while flag:
    try:
        R, W, X = select.select(SocketList, [], [])
        for sckt in R:
            if sckt is ListenSocket:
                conn_sock, addr = ListenSocket.accept()
                addr, port = conn_sock.getpeername()
                print("New client connected since %s:%d" %(addr, port))
                SocketList.append(conn_sock)
            elif sckt is sys.stdin:
                line = sys.stdin.readline()
                if line == "EXIT\n":
                    flag = False
            else:
                skel.pool.clear_expired_locks()
                income_message = sock_utils.unserialize(sckt)
                if income_message == 'EXIT':
                    exit()
                else:
                    send_message = skel.process_message(income_message)
                    sock_utils.serialize(send_message, sckt)

                 
    except Exception as error:
        if type(error) == s.error:
            sckt.close()
            SocketList.remove(sckt)
        else:
            resp = []
            if type(error) == ValueError:
                resp.append('INVALID ARGUMENT')
            else:
                resp.append("UKNOWN ERROR")

            sock_utils.serialize(resp, sckt)
    finally:
        ListenSocket.close()
    
    print('############ END #############')

ListenSocket.close()