#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 2 - sock_utils.py
Grupo: 14
Números de aluno: 53299, 53745
"""


import socket as s
import pickle
import struct


def create_tcp_server_socket(address, port, queue_size):
    listener_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    listener_socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    listener_socket.bind((address, port))
    listener_socket.listen(queue_size)
    return listener_socket


def create_tcp_client_socket(address, port):
    client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    client_socket.connect((address, port))
    return client_socket



def receive_all(socket, length):
    #data = ""
    size = 0
    while size <= length:
        if size <= 1024:
            size = length

        data_received = socket.recv(size)
        data_received = pickle.loads(data_received)
        size = size + len(data_received)
    return data_received


def serialize(data, socket):
	msg_bytes = pickle.dumps(data, - 1)  
	size_bytes = struct.pack('!i', len(msg_bytes))
	socket.sendall(size_bytes)
	socket.sendall(msg_bytes)

def unserialize(socket):
	size_bytes = socket.recv(4)
	size = struct.unpack('!i', size_bytes)[0]
	msg_bytes = receive_all(socket, size)
	msg = pickle.loads(msg_bytes)
	return msg