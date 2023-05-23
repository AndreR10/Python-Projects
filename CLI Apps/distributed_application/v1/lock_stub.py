#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 2 - lock_skel.py
Grupo: 14
Números de aluno: 53299, 53745
"""

from net_client import server
import time, sys

class stub:
    def __init__(self,server_addr, server_port):
        """
        """
        self.adress = server_addr
        self.port = server_port
        self.connection = server(server_adr, server_port)
        self.connection.connect()

    def lock(self, client_id, num_lock):
        msg = ['10', client_id, num_lock]
        response = self.connection.send_receive(msg)
        return response

    def release(self, client_id, num_lock):
        msg = ['20', client_id, num_lock]
        response = self.connection.send_receive(msg)
        return response

    def test(self, num_lock):
        msg = ['30', num_lock]
        response = self.connection.send_receive(msg)
        return response

    def stats(self, num_lock):
        msg = ['40', num_lock]
        response = self.connection.send_receive(msg)
        return response

    def stats_k(self, num_lock):
        msg = ['50', num_lock]
        response = self.connection.send_receive(msg)
        return response

    def close(self):
        self.connection.close()
