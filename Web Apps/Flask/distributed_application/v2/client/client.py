"""
Aplicacoes Distribuidas - client.py
    
"""

import sys
import os
import socket
import ssl
import json
import requests

from requests_oauthlib import OAuth2Session


# Informação da aplicação registada no GitHub
client_id = "cb71a9ecf3d04c339c6e5cae21289aee"
client_secret = "1a2f46975a1947caa8b9d97af58b9216"
# Informação sobre a Authorization server
# authorization_base_url = "hhttps://accounts.spotify.com/authorize"
access_token_url = "https://accounts.spotify.com/api/token"
# redirect_uri = "http://localhost:5001/callback"


# # Authenticate and authorize the client with Spotify using OAuth2
# oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
# authorization_url, state = oauth.authorization_url(authorization_base_url)
# print(f"Please visit the following URL to authorize the client: {authorization_url}")

# # Handle the authorization callback
# authorization_response = input("Enter the full callback URL: ")
# token = oauth.fetch_token(
#     token_url,
#     client_secret=client_secret,
#     authorization_response=authorization_response,
# )

s = requests.Session()
certs = ("../certs/client.crt", "../certs/CA.key")
verify = "../certs/CA.crt"
flag = True

# Create an OAuth2 session
spotify = OAuth2Session(client_id)

# Fetch the access token from the server
token = spotify.fetch_token(
    access_token_url,
    verify=verify,
    authorization_response="http://localhost:5000/callback",
    client_secret=client_secret,  # Replace with your Spotify API client secret
)

# Store the access token for future use
access_token = token["access_token"]

headers = {"Authorization": f"Bearer {access_token}"}

while flag:
    try:
        print("Command >> <OPERATION> <PARAM>")
        msg = input("Command >> ")
        print("--------------------------------")

        if msg == "EXIT" or msg == "exit" or msg == "Exit":
            print("Program closed!")
            print("-------END------")
            exit()

        command = msg.split(" ")

        if command[0].upper() == "ADD":
            try:
                if command[1].upper() == "USER":
                    utilizadores = {
                        "nome": command[4],
                        "username": command[2],
                        "password": command[3],
                    }
                    url = "https://localhost:5000/utilizadores"
                    data = json.dumps(utilizadores)
                    print("Sent: {}".format(data))
                    response = spotify.post(url, data=data, verify=verify, cert=certs)
                    print("URL: {}".format(response.url))
                    print("STATUS CODE: {}".format(response.status_code))
                    print("RESULT: User {}".format(json.loads(response.content)))
                    print(response.headers)
                    print("**********")

                elif command[1].upper() == "BANDA":
                    if command[2] in [
                        "pop",
                        "rock",
                        "indy",
                        "metal",
                        "trance",
                        "classic",
                    ]:
                        bandas = {
                            "nome": command[3],
                            "ano": command[4],
                            "genero": command[2],
                        }
                        url = "https://localhost:5000/bandas"
                        data = json.dumps(bandas)
                        print("Sent: {}".format(data))
                        response = spotify.post(
                            url, data=data, verify=verify, cert=certs
                        )
                        print("URL: {}".format(response.url))
                        print("STATUS CODE: {}".format(response.status_code))
                        print("RESULT: Band {}".format(json.loads(response.content)))
                        print(response.headers)
                        print("**********")

                    else:
                        print("Genre not valid!")
                        exit()

                elif command[1].upper() == "ALBUM":
                    albuns = {
                        "id_banda": command[2],
                        "nome": command[3],
                        "ano_album": command[4],
                    }
                    url = "https://localhost:5000/albuns"
                    data = json.dumps(albuns)
                    print("Sent: {}".format(data))
                    response = spotify.post(url, data=data, verify=verify, cert=certs)
                    print("URL: {}".format(response.url))
                    print("STATUS CODE: {}".format(response.status_code))
                    print("RESULT: Album {}".format(json.loads(response.content)))
                    print(response.headers)
                    print("**********")

                else:
                    if command[3] in ["M", "m", "S", "B", "MB"]:
                        rate = {
                            "id_user": command[1],
                            "id_algum": command[2],
                            "rate": command[3],
                        }
                        url = "https://localhost:5000/utilizadores/rate"
                        data = json.dumps(rate)
                        print("Sent: {}".format(data))
                        response = spotify.post(
                            url, data=data, verify=verify, cert=certs
                        )
                        print("URL: {}".format(response.url))
                        print("STATUS CODE: {}".format(response.status_code))
                        print("RESULT: {}".format(json.loads(response.content)))

                    else:
                        print("Rate not valid!")
                        exit()

            except IndexError:
                print("ADD <?> <?> <?>")
                print("Missig one of the arguments")
                sys.exit(1)
            except Exception as e:
                print(e)
                sys.exit(1)

        elif command[0].upper() == "SHOW" or command[0].upper() == "REMOVE":
            try:
                if command[1].upper() == "USER":
                    utilizadores = {"id_user": command[2]}
                    url = "https://localhost:5000/utilizadores/" + command[2]
                    data = json.dumps(utilizadores)
                    print("Sent: {}".format(data))

                    # SHOW USER
                    if command[0].upper() == "SHOW":
                        response = spotify.get(
                            url, data=data, verify=verify, cert=certs, headers=headers
                        )
                        print("URL: {}".format(response.url))
                        print("STATUS CODE: {}".format(response.status_code))
                        print("RESULT: User -> %s" % json.loads(response.content))
                    # REMOVE USER
                    else:
                        response = spotify.delete(url, data=data)
                        print("URL: {}".format(response.url))
                        print("STATUS CODE: {}".format(response.status_code))
                        print("RESULT: User -> %s" % json.loads(response.content))

                elif command[1].upper() == "BANDA":
                    bandas = {"id_banda": command[2]}
                    url = "https://localhost:5000/bandas/" + command[2]
                    data = json.dumps(bandas)
                    print("Sent: {}".format(data))

                    # SHOW BANDA
                    if command[0].upper() == "SHOW":
                        response = spotify.get(
                            url,
                            data=data,
                            verify=verify,
                            cert=certs,
                        )
                        print("URL: {}".format(response.url))
                        print("STATUS CODE: {}".format(response.status_code))
                        print("RESULT: Band -> %s" % json.loads(response.content))

                    # REMOVE BANDA
                    else:
                        response = spotify.delete(
                            url, data=data, verify=verify, cert=certs
                        )
                        print("URL: {}".format(response.url))
                        print("STATUS CODE: {}".format(response.status_code))
                        print("RESULT: Band -> %s" % json.loads(response.content))

                elif command[1].upper() == "AlBUM":
                    albuns = {"id_album": command[2]}
                    url = "https://localhost:5000/albuns/" + command[2]
                    data = json.dumps(albuns)
                    print("Sent: {}".format(data))

                    # SHOW ALBUM
                    if command[0].upper() == "SHOW":
                        response = spotify.get(
                            url, data=data, verify=verify, cert=certs
                        )
                        print("URL: {}".format(response.url))
                        print("STATUS CODE: {}".format(response.status_code))
                        print("RESULT: Album -> %s" % json.loads(response.content))

                    # REMOVE ALBUM
                    else:
                        response = spotify.delete(
                            url, data=data, verify=verify, cert=certs
                        )
                        print("URL: {}".format(response.url))
                        print("STATUS CODE: {}".format(response.status_code))
                        print("RESULT: Album -> %s" % json.loads(response.content))
                # ALL
                elif command[1].upper() == "ALL":
                    if command[2].upper() == "USERS":
                        url = "https://localhost:5000/utilizadores/all"

                        # SHOW ALL USERS
                        if command[0].upper() == "SHOW":
                            response = spotify.get(url, verify=verify, cert=certs)
                            print("URL: {}".format(response.url))
                            print("STATUS CODE: {}".format(response.status_code))
                            print(
                                "RESULT: Users -> {}".format(
                                    json.loads(response.content)
                                )
                            )
                            print("**********")

                        # REMOVE ALL USERS
                        else:
                            response = spotify.delete(url, verify=verify, cert=certs)
                            print("URL: {}".format(response.url))
                            print("STATUS CODE: {}".format(response.status_code))
                            print(
                                "RESULT: Users -> {}".format(
                                    json.loads(response.content)
                                )
                            )
                            print("**********")

                    elif command[2].upper() == "BANDAS":
                        url = "https://localhost:5000/bandas"

                        # SHOW ALL BANDAS
                        if command[0].upper() == "SHOW":
                            response = spotify.get(url, verify=verify, cert=certs)
                            print("URL: {}".format(response.url))
                            print("STATUS CODE: {}".format(response.status_code))
                            print(
                                "RESULT: Bands -> {}".format(
                                    json.loads(response.content)
                                )
                            )
                            print("**********")

                        # REMOVE ALL BANDAS
                        else:
                            response = spotify.delete(url, verify=verify, cert=certs)
                            print("URL: {}".format(response.url))
                            print("STATUS CODE: {}".format(response.status_code))
                            print(
                                "RESULT: Bands -> {}".format(
                                    json.loads(response.content)
                                )
                            )
                            print("**********")

                    elif command[2].upper() == "ALBUNS":
                        url = "https://localhost:5000/albuns"

                        # SHOW ALL ALBUNS
                        if command[0].upper() == "SHOW":
                            response = spotify.get(url, verify=verify, cert=certs)
                            print("URL: {}".format(response.url))
                            print("STATUS CODE: {}".format(response.status_code))
                            print(
                                "RESULT: Albuns -> {}".format(
                                    json.loads(response.content)
                                )
                            )
                            print("**********")

                        # REMOVE ALL ALBUNS
                        else:
                            response = spotify.delete(url, verify=verify, cert=certs)
                            print("URL: {}".format(response.url))
                            print("STATUS CODE: {}".format(response.status_code))
                            print(
                                "RESULT: Albuns -> {}".format(
                                    json.loads(response.content)
                                )
                            )
                            print("**********")

                    elif command[2].upper() == "ALBUNS_B":
                        banda = {"id_banda": command[3]}
                        url = "https://localhost:5000/albuns/banda/" + str(command[3])
                        data = json.dumps(banda)
                        print("Sent: {}".format(data))

                        if command[0].upper() == "SHOW":
                            response = spotify.get(
                                url, data=data, verify=verify, cert=certs
                            )
                            print("URL: {}".format(response.url))
                            print("STATUS CODE: {}".format(response.status_code))
                            print(
                                "All band {} albuns: {}".format(
                                    str(command[3]), json.loads(response.content)
                                )
                            )

                        else:
                            response = spotify.delete(
                                url, data=data, verify=verify, cert=certs
                            )
                            print("URL: {}".format(response.url))
                            print("STATUS CODE: {}".format(response.status_code))
                            print(
                                "RESULT: Albuns -> {}".format(
                                    json.loads(response.content)
                                )
                            )
                            print("**********")

                    elif command[2].upper() == "ALBUNS_U":
                        utilizador = {"id_user": command[3]}
                        url = "https://localhost:5000/albuns/utilizador/" + str(
                            command[3]
                        )
                        data = json.dumps(utilizador)
                        print("Sent: {}".format(data))

                        if command[0].upper() == "SHOW":
                            response = spotify.get(
                                url, data=data, verify=verify, cert=certs
                            )
                            print("URL: {}".format(response.url))
                            print("STATUS CODE: {}".format(response.status_code))
                            print(
                                "All user {} albuns: {}".format(
                                    command[3], json.loads(response.content)
                                )
                            )

                        else:
                            response = spotify.delete(
                                url, data=data, verify=verify, cert=certs
                            )
                            print("URL: {}".format(response.url))
                            print("STATUS CODE: {}".format(response.status_code))
                            print(
                                "RESULT: Albuns -> {}".format(
                                    json.loads(response.content)
                                )
                            )
                            print("**********")

                    elif command[2].upper() == "ALBUNS_R":
                        rate = {"rate": command[3]}
                        url = "https://localhost:5000/albuns/rate/" + str(command[3])
                        data = json.dumps(rate)
                        print("Sent: {}".format(data))

                        if command[0].upper() == "SHOW":
                            response = spotify.get(
                                url, data=data, verify=verify, cert=certs
                            )
                            print("URL: {}".format(response.url))
                            print("STATUS CODE: {}".format(response.status_code))
                            print(
                                "All rate {} albuns: {}".format(
                                    str(command[3]), json.loads(response.content)
                                )
                            )

                        else:
                            response = spotify.delete(
                                url, data=data, verify=verify, cert=certs
                            )
                            print("URL: {}".format(response.url))
                            print("STATUS CODE: {}".format(response.status_code))
                            print(
                                "RESULT: Albuns -> {}".format(
                                    json.loads(response.content)
                                )
                            )
                            print("**********")

            except IndexError:
                print("Missing arguments!")
                sys.exit(1)
            except Exception as e:
                print(e)
                sys.exit(1)

        elif command[0].upper() == "UPDATE":
            if command[1].upper() == "ALBUM":
                album = {
                    "id_user": command[4],
                    "id_album": command[2],
                    "rate": command[3],
                }
                url = "https://localhost:5000/albuns"
                data = json.dumps(album)
                print("Sent {}".format(data))
                response = spotify.put(url, data=data, verify=verify, cert=certs)
                print("URL: {}".format(response.url))
                print("STATUS CODE: {}".format(response.status_code))
                print("RESULT: {}".format(response.content))

            elif command[1].upper() == "USER":
                utilizador = {"id_user": command[2], "password": command[3]}
                url = "https://localhost:5000/utilizadores"
                data = json.dumps(utilizador)
                print("Sent {}".format(data))
                response = spotify.put(url, data=data, verify=verify, cert=certs)
                print("URL: {}".format(response.url))
                print("STATUS CODE: {}".format(response.status_code))
                print("RESULT: {}".format(response.content))

    except ValueError:
        print("Check the given args")
        sys.exit(1)
    except KeyboardInterrupt:
        flag = False
        print("SHUTTING DOWN")

print("---------------END-----------------")
