*************************
* Grupo 014             *
* André Ramos 53299     *
* João Nunes 53745	    *
*************************

1. Iniciar ligação:

Correr server.py e client.py em dois terminais distintos, executando primeiro o "server.py". Ex: "python3 server.py", "python3 client.py".

2. Autenticar o utilizador para aceder aos recursos do servidor:

Seguir as instruções indicadas no terminal relativo ao programa "client.py".

3. Introduzir um dos comandos indicados abaixo para pesquisa:

Adicionar ADD:

    1) ADD USER  <username> <password> <nome>
    2) ADD BANDA <genero> <nome> <ano> 
    3) ADD ALBUM <id_banda> <nome> <ano_album>
    	3.1) <id_user> <id_album> <rate>      

    Por exemplo: 
        genero = pop, rock, indy, metal, trance, classic
        rate = M, m, S, B, MB
        
Remover REMOVE:

    1) REMOVE USER <id_user>
    2) REMOVE BANDA <id_banda>
    3) REMOVE ALBUM <id_album>
    4) REMOVE ALL <USERS | BANDAS | ALBUNS>         
    5) REMOVE ALL ALBUNS_B <id_banda>
    6) REMOVE ALL ALBUNS_U <id_user>
    7) REMOVE ALL ALBUNS   <rate>
           
Mostrar SHOW:

    1) SHOW USER <id_user>
    2) SHOW BANDA <id_banda>
    3) SHOW ALBUM <id_album>
    4) SHOW ALL <USERS | BANDAS | ALBUNS>         
    5) SHOW ALL ALBUNS_B <id_banda>
    6) SHOW ALL ALBUNS_U <id_user>
    7) SHOW ALL ALBUNS   <rate>

Atualizar UPDATE:

    1) UPDATE ALBUM <id_album> <rate> <id_user>
    2) UPDATE USER  <id_user> <password>


LIMITAÇÕES:
Quando a verificação de certificado está ativa é nos dados o erro seguinte que nos impede processar qualquer pedido na parte do cliente, 
embora ter sido criado os devidos certificados com assinatura de uma Certificate Authority. 
SSLError(136, '[X509: NO_CERTIFICATE_OR_CRL_FOUND] no certificate or crl found (_ssl.c:4232)

