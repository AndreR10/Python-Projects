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
    data = ""
    while len(data) < length:
        data_received = socket.recv(length - len(data))
        data += data_received
    return data


def serialize(data, socket):
	msg_bytes = pickle.dumps(data, -1)  
	size_bytes = struct.pack('!i', len(msg_bytes))
	socket.sendall(size_bytes)
	socket.sendall(msg_bytes)

def unserialize(socket):
	size_bytes = socket.recv(4)
	size = struct.unpack('!i', size_bytes)[0]
	msg_bytes = receive_all(socket, size)
	msg = pickle.loads(msg_bytes)
	return msg