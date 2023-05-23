#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_pool.py
Grupo: 14
Números de aluno: 53299, 53745
"""

# Zona para fazer importação

import time

###############################################################################

class resource_lock:
    def __init__(self):
        """
        Define e inicializa as características de um LOCK num recurso.
        """
        self.state = "UNLOCKED"  # Lock state
        self.lock_count = 0  # How many times was locked
        self.client_id = None  # Client that was the lock
        self.time_lock = 0  # Time of the lock
        #self.num_locks = k  # Remaining locks
        self.clients_list = []  # Clients locking list

    def lock(self, client_id, time_limit):
        """
        Bloqueia o recurso se este não estiver bloqueado ou inativo, ou mantém o bloqueio
        se o recurso estiver bloqueado pelo cliente client_id. Neste caso renova
        o bloqueio do recurso até time_limit.
        Retorna True se bloqueou o recurso ou False caso contrário.
        """
       
        if self.status() == "UNLOCKED":
            self.state = "LOCKED"
            self.lock_count += 1
            self.client_id = client_id
            self.time_lock = time.time() + time_limit
            self.clients_list.append(client_id)
            return True

        elif self.status() == "LOCKED" and self.client_id == client_id:
            self.time_lock = time.time() + time_limit
            self.lock_count = + 1
            return True

        elif self.status() == "LOCKED" and self.client_id != client_id:
            self.lock_count += 1
            self.clients_list.append(client_id)
            return True
        
        else:
            return False

      

    def urelease(self):
        """
        Liberta o recurso incondicionalmente, alterando os valores associados
        ao bloqueio.
        """
        self.state = "UNLOCKED"
        self.time_lock = 0
        self.client_id = None

    def release(self, client_id):
        """
        Liberta o recurso se este foi bloqueado pelo cliente client_id,
        retornando True nesse caso. Caso contrário retorna False.
        """
        if self.client_id == client_id:
            self.state = "UNLOCKED"
            self.time_limit = None
            self.client_id = None
            return True
        else:
            return False

    def status(self):
        """
        Retorna o estado de bloqueio do recurso ou inativo, caso o recurso se
        encontre inativo.
        """
        if self.state == "UNLOCKED":
            return "UNLOCKED"
        elif self.state == "DISABLE":
            return "DISABLE"
        else:
            return "LOCKED"

    def stats(self):
        """
        Retorna o número de vezes que este recurso já foi bloqueado em k.
        """ 
        return self.lock_count

    def disable(self):
        """
        Coloca o recurso inativo/indisponível incondicionalmente, alterando os
        valores associados à sua disponibilidade.
        """
        self.state = "DISABLE"  # Lock state
        self.lock_count = 0  # Times that was locked
        self.client_id = None  # Client that was the lock
        self.time_lock = 0  # Time os the lock
        self.clients_list = []  # Clients locking list


###############################################################################

class lock_pool:
    def __init__(self, N, K, Y, T):
        """
        Define um array com um conjunto de locks para N recursos. Os locks podem
        ser manipulados pelos métodos desta classe.
        Define K, o número máximo de bloqueios permitidos para cada recurso. Ao
        atingir K, o recurso fica indisponível/inativo.
        Define Y, o número máximo permitido de recursos bloqueados num dado
        momento. Ao atingir Y, não é possível realizar mais bloqueios até que um
        recurso seja libertado.
                Define T, o tempo máximo de concessão de bloqueio.
        """

        self.locks_array = [resource_lock() for i in range(N)]
        self.num_resources = N # Num of resources
        self.max_locks = K  # Max lock per resource
        self.max_resource_lock = Y  # Max resource locked
        self.max_lock_time = T # Max lock time

    def clear_expired_locks(self):
        """
        Verifica se os recursos que estão bloqueados ainda estão dentro do tempo
        de concessão do bloqueio. Liberta os recursos caso o seu tempo de
        concessão tenha expirado.
        """
        for i in range(len(self.locks_array)):
            if self.locks_array[i].status() == "LOCKED" and self.locks_array[i].time_lock >= self.max_lock_time:
                self.locks_array[i].urelease()

    def lock(self, resource_id, client_id, time_limit):
        """
        Tenta bloquear o recurso resource_id pelo cliente client_id, até ao
        instante time_limit.
        O bloqueio do recurso só é possível se o recurso estiver ativo, não
        bloqueado ou bloqueado para o próprio requerente, e Y ainda não foi
        excedido. É aconselhável implementar um método __try_lock__ para
        verificar estas condições.
        Retorna True em caso de sucesso e False caso contrário.
        """
        if self.__try_lock__():
            return False
        else:
            for i in range(self.num_resources):
                if resource_id <= self.num_resources and resource_id > 0:
                    resource = self.locks_array[resource_id - 1]
                    if resource.status() == "LOCKED" and client_id == resource.client_id:
                        return resource.lock(client_id, time_limit)
                    elif resource.status() == "UNLOCKED":
                        return resource.lock(client_id, time_limit)
                    else:
                        return False
                else:
                    return None
                

    def __try_lock__(self):
        count_locked = 0
        for i in range(len(self.locks_array)):
            if self.locks_array[i].status() == "LOCKED" or self.locks_array[i].status() == "DISABLE":
                count_locked += 1

        if count_locked == self.max_resource_lock:
            return True
        else:
            return False

    def release(self, resource_id, client_id):
        """
        Liberta o bloqueio sobre o recurso resource_id pelo cliente client_id.
        True em caso de sucesso e False caso contrário.
        """
        if resource_id <= self.num_resources and resource_id > 0:
            return self.locks_array[resource_id - 1].release(client_id)
        else:
            return None

    def status(self, resource_id):
        """
        Retorna True se o recurso resource_id estiver bloqueado e False caso
        não esteja bloqueado ou inativo.
        """
        if resource_id <= self.num_resources and resource_id > 0:
            if self.locks_array[resource_id - 1].status() == "UNLOCKED":
                return False
            elif self.locks_array[resource_id - 1].status() == "LOCKED":
                return True
            else:
                return "disable"
        else:
            return None

    def stats(self, resource_id):
        """
        Retorna o número de vezes que o recurso resource_id já foi bloqueado, dos
        K bloqueios permitidos.
        """
        if resource_id <= self.num_resources and resource_id > 0:
            return self.locks_array[resource_id - 1].stats()
        else:
            return None

    def ystats(self):
        """
        Retorna o número de recursos bloqueados num dado momento do Y permitidos.
        """
        resource_locked = 0
        for i in range(self.max_resource_lock):
            if self.locks_array[i].status() == "LOCKED":
                resource_locked += 1

        return resource_locked

    def nstats(self):
        """
        Retorna o número de recursos disponíneis em N.
        """
        free_resources_count = 0
        for i in range(self.num_resources):
            if self.locks_array[i].status() == "UNLOCKED":
                free_resources_count += 1

        return free_resources_count

    def __repr__(self):
        """
        Representação da classe para a saída standard. A string devolvida por
        esta função é usada, por exemplo, se uma instância da classe for
        passada à função print.
        """
        output = ""
        #
        # Acrescentar na output uma linha por cada recurso bloqueado, da forma:
        # recurso <número do recurso> bloqueado pelo cliente <id do cliente> até
        # <instante limite da concessão do bloqueio>
        #
        # Caso o recurso não esteja bloqueado a linha é simplesmente da forma:
        # recurso <número do recurso> desbloqueado
        # Caso o recurso esteja inativo a linha é simplesmente da forma:
        # recurso <número do recurso> inativo
        #
        for i in range(self.num_resources):
            lock = self.locks_array[i]
            if lock.status() == "LOCKED":
                output += 'Resource <%s> LOCKED by client <%d> until <%f>\n' % (i+1, lock.client_id, time.ctime(lock.time_lock))

            elif lock.status() == "UNLOCKED":
                output += 'Resource <%s> UNLOCKED\n' % (i+1)
            
            elif lock.status() == "DISABLE":
                output += 'Resource <%s> DISABLE\n' % (i+1)

        return output
