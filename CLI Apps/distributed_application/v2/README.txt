A partir do ficheiro lock_server.py é possível manipular os recursos do servidor.

No total existem à disposição 7 comandos possíveis de utilizar: LOCK, RELEASE, STATUS, STATS, YSTATS, NSTATS e EXIT.
As funcionalidades dos comandos indicados são:

	LOCK - bloqueia o recurso, sendo necessário indicar qual o recurso que se pretende bloquear. Irá retornar "TRUE" se bloquear o recurso, retorna "FALSE" caso contrário, e retorna "NONE" caso recurso não exista.
	RELEASE : liberta o bloqueio sobre o recurso bloqueado pelo cliente. Retorna "True" em caso de sucesso e "False" caso contrário.
	STATUS : retorna "True" se o recurso estiver bloqueado e "False" caso não esteja bloqueado ou inativo.
	STATS : retorna o número de vezes que o recurso já foi bloqueado, dos K bloqueios permitidos.
	YSTATS : retorna o número de recursos bloqueados num dado momento do Y permitidos.
	NSTATS : retorna o número de recursos disponíneis em N.
	EXIT : permite que o utilizador termine o cliente ou o servidor.

Execução do servidor:

	lock_server.py <port> <number resources> <number lock per resources> <number resource locked at the same time> <time limit>

		<port> : o número da porta

		<number resources> : o número de recursos.

		<number lock per resources> : o número de bloqueios por recursos.

		<number resource locked at the same time> : o número máximo de recursos bloqueados num dado momento.

		<time limit> : o tempo limite de cada bloqueio.

Execução do cliente:

	lock_client.py <client_id> <server> <port>

		<client_id> : o id do cliente.

		<server> : o IP do servidor.

		<port> : o número da porta


LIMITAÇÕES:
Não foi possível implementar a "__repr__" da "class lock_pool"