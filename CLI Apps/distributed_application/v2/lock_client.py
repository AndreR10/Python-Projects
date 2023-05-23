#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Distributed Application - version 1 - lock_client.py
"""
# Zona para fazer imports
import sys
from lock_stub import lock_stub
from net_client import server

# Programa principal

try:
    client_id = sys.argv[1]
    HOST = sys.argv[2]
    PORT = int(sys.argv[3])

    print("Client ID: {0}".format(str(client_id)))

except ValueError:
    print("All the arguments need to be type INT.\n")
    exit(1)

except NameError:
    print("Missing one of the arguments.\n")
    exit(1)

except IndexError:
    print("Missing one of the arguments.\n")
    exit(1)


stub = lock_stub(HOST, PORT)
stub.connect()


flag = True

while flag:
    try:
        command = input('Command > ')

        msg = command.split()

        if len(msg) == 0:
            print("Missing command")

        elif msg[0] == 'EXIT\n' or msg[0] == "exit":
            flag = False
            stub.disconnect()

        # LOCK
        elif msg[0] == 'LOCK':
            if len(msg) < 3 or len(msg) > 3:
                print("This command needs 4 arguments")
            else:
                resp = stub.lock(msg[1], msg[2], client_id)
                print("SERVER: ", resp)

        # RELEASE
        elif msg[0] == 'RELEASE':
            if len(msg) < 3 or len(msg) > 3:
                print("This command needs 3 arguments")
            else:
                resp = stub.release(msg[1], client_id)
                print("SERVER: ", resp)

        # STATUS
        elif msg[0] == 'STATUS':
            if len(msg) < 2 or len(msg) > 2:
                print("This command needs 2 arguments")
            else:
                resp = stub.status(msg[1])
                print("SERVER: ", resp)

        # STATS
        elif msg[0] == 'STATS':
            if len(msg) < 2 or len(msg) > 2:
                print("This command needs 2 arguments")
            else:
                resp = stub.stats(msg[1])
                print("SERVER: ", resp)

        # YSTATS
        elif msg[0] == 'YSTATS':
            if len(msg) > 1:
                print("This command needs 1 arguments")
            else:
                resp = stub.ystats()
                print("SERVER: ", resp)

        # NSTATS
        elif msg[0] == 'NSTATS':
            if len(msg) > 1:
                print("This command needs 1 arguments")
            else:
                resp = stub.nstats()
                print("SERVER: ", resp)
        else:
            resp = "INVAlID COMMAND!"
            print(resp)

    except ValueError:
        print("Check type of given arguments")


stub.disconnect()
