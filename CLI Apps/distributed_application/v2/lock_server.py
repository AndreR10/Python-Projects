#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_server.py
Grupo: 14
Números de aluno: 53299, 53745
"""

# Zona para fazer importação
import sys
import time
import sock_utils
import socket as s
import select
import struct
import pickle
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

        print("SERVER -> IP: <{0}>, PORT: <{1}>\n".format(HOST, str(PORT)))
        print("Number resources: <{0}>".format(str(N)))
        print("Number lock per resource: <{0}>".format(str(K)))
        print("Number resource locked at the same time: <{0}>".format(str(Y)))
        print("Time limit: <{0}>\n".format(str(T)))

        
        
    except ValueError:
        print("All the arguments need to be type INT.")
        exit(1)
else:
     print("Missing Arguments")
     exit(1)

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
                print("New client connected to %s:%d" %(addr, port))
                SocketList.append(conn_sock)
            elif sckt is sys.stdin:
                line = sys.stdin.readline()
                if line == "EXIT\n" or line == "exit\n":
                    flag = False
                    sckt.close()
            else:
                # Receber
                size_bytes = sckt.recv(4)
                size = struct.unpack('!i', size_bytes)[0]
                msg = sock_utils.receive_all(sckt, size)
                
                # Processar
                send_msg = skel.process_message(msg)
                send_msg_bytes = pickle.dumps(send_msg, - 1)  
                send_size_bytes = struct.pack('!i', len(send_msg_bytes))
                
                # Enviar
                sckt.sendall(send_size_bytes)
                sckt.sendall(send_msg_bytes)

                                 
    except struct.error:
        addr, port = sckt.getpeername()
        print("Client {0}:{1} disconected".format(str(addr), str(port)))
        SocketList.remove(sckt)

    except ValueError:
        print("Check given arguments")
   

    print('--------------------------------')

ListenSocket.close()
print('############ SERVER TERMINATED #############')