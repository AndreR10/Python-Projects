#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 2 - lock_stub.py
Grupo: 14
Números de aluno: 53299, 53745
"""

from net_client import server
import time, sys

class lock_stub:
  
    def __init__(self, address, port):
      """
      """
      self.address = address
      self.port = port
      self.server = server(address, port)

    
    def connect(self):
      self.server.connect()
          

    def disconnect(self):
      self.server.close()

    def lock(self, time_limit, resource_id, client_id):
      msg = ['10', time_limit, resource_id, client_id]
      response = self.server.send_receive(msg)
      return response

    def release(self, resource_id, client_id):
      msg = ['20', resource_id, client_id]
      response = self.server.send_receive(msg)
      return response

    def status(self, resource_id):
      msg = ['30', resource_id]
      response = self.server.send_receive(msg)
      return response

    def stats(self, resource_id):
      msg = ['40', resource_id]
      response = self.server.send_receive(msg)
      return response

    def ystats(self):
      msg = ['50']
      response = self.server.send_receive(msg)
      return response

    def nstats(self):
      msg = ['60']
      response = self.server.send_receive(msg)
      return response


    
