#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 2 - lock_skel.py
Grupo: 14
Números de aluno: 53299, 53745
"""

# Zona para fazer importação
import time
from sock_utils import serialize, unserialize
from lock_pool import lock_pool

class lock_skel:

    def __init__(self, N, K, Y, T):
        self.N = N
        self.K = K
        self.Y = Y
        self.T = T
        self.recordList = []
        self.pool = lock_pool(N,K,Y,Y)

    def process_message(self, msg_bytes):
        
        
        response = []

        msg_part = msg_bytes

        print("Received: %s" %(msg_part))
        

        if msg_part == None or len(msg_part) == 0:
            response.append('INVALID MESSAGE')

        else:
            # Lock
            if msg_part[0] == "10":
                self.recordList.append(msg_part)
                lock_time = int(msg_part[1])
                resource_id = int(msg_part[2])
                client_id = int(msg_part[3])
                response.append("11")
                resp = self.pool.lock(resource_id, client_id, lock_time)
                if resp == True:
                    response.append(True)
                elif resp == False:
                    response.append(False)
                else:
                    response.append(None)
            
            # Release
            elif msg_part[0] == "20":
                self.recordList.append(msg_part)
                resource_id = int(msg_part[1])
                client_id = int(msg_part[2])
                response.append("21")
                resp = self.pool.release(resource_id, client_id)
                if resp == True:
                    response.append(True)
                elif resp == False:
                    response.append(False)
                else:
                    response.append(None)

            # Status
            elif msg_part[0] == "30":
                self.recordList.append(msg_part)
                resource_id = int(msg_part[1])
                response.append("31")
                resp = self.pool.status(resource_id)
                if resp == True:
                    response.append(True)
                elif resp == False:
                    response.append(False)
                else:
                    response.append(None)


            # Stats
            elif msg_part[0] == "40":
                self.recordList.append(msg_part)
                resource_id = int(msg_part[1])
                response.append("41")
                resp = self.pool.stats(resource_id)
                if resp == None:
                    response.append(None)
                else:
                    response.append(resp)

            # YStats
            elif msg_part[0] == "50":
                self.recordList.append(msg_part)
                response.append("51")
                response.append(self.pool.ystats())
            
            # NStats
            elif msg_part[0] == "60":
                self.recordList.append(msg_part)
                response.append("61")
                response.append(self.pool.nstats())

            else:
                response.append('INVALID MESSAGE')

        # print(self.pool)
        return response
        