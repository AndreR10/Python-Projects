# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 2 - net_client.py
Grupo: 14
Números de aluno: 53299, 53745
"""

# zona para fazer importação

import sock_utils
import pickle, struct
import socket
# definição da classe server

class server:
    """
    Abstrai uma ligação a um servidor TCP. Implementa métodos para: estabelecer
    a ligação; envio de um comando e receção da resposta; terminar a ligação.
    """
    def __init__(self, address, port):
        """
        Inicializa a classe com parâmetros para funcionamento futuro.
        """
        self.addr = address
        self.port = port
        self.sock = None
        
    
    def connect(self):
        """
        Estabelece a ligação ao servidor especificado na inicialização do
        objeto.
        """
        self.sock = sock_utils.create_tcp_client_socket(self.addr, self.port)

    def send_receive(self, data):
        """
        Envia os dados contidos em data para a socket da ligação, e retorna a
        resposta recebida pela mesma socket.
        """

        # Enviar
        msg_bytes = pickle.dumps(data, - 1)  
        size_bytes = struct.pack('!i', len(msg_bytes))
        self.sock.sendall(size_bytes)
        self.sock.sendall(msg_bytes)

        # Receber
        size_bytes = self.sock.recv(4)
        size = struct.unpack('!i', size_bytes)[0]
        msg = sock_utils.receive_all(self.sock, size)
        return msg


    def close(self):
        """
        Termina a ligação ao servidor.
        """
        self.sock.close()
