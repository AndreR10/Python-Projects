# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 2 - net_client.py
Grupo: 14
Números de aluno: 53299, 53745
"""

# zona para fazer importação

from sock_utils import create_tcp_client_socket

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
        self.add = address
        self.port = port

    def connect(self):
        """
        Estabelece a ligação ao servidor especificado na inicialização do
        objeto.
        """
        self.sock = create_tcp_client_socket(self.add, self.port)

    def send_receive(self, data):
        """
        Envia os dados contidos em data para a socket da ligação, e retorna a
        resposta recebida pela mesma socket.
        """
        serialize(data, self.sock)
        response = unserialize(self.sock)
        return response

    def close(self):
        """
        Termina a ligação ao servidor.
        """
        self.sock.close()
