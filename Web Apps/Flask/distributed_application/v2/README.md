# Description

In this version 2 the aim was to improve performance, regardless of the server's capabilities or configuration, the client developed using the `requests` module should ensure that multiple requests sent to the server are made on the same **TCP** connection (persistent connections in HTTP). The **SSL/TLS** protocol should be used with **Flask** and the `requests` module to allow mutual authentication and ensure confidential communication (encryption) between the client and the server. To achieve this, both the client and the server use public key certificates signed by a **Certificate Authority (CA)**. In **Flask**, the implementation will be done using the `SSLContext` class from the `ssl` module of the _Python_ standard library.

The _OAuth2_ protocol is used with _Flask_ and the `requests-oauthlib` module to allow the client to request authorization to access the resources provided by the server. For this purpose, the server's URI is registered with an Google and Spotify OAuth API, so that the client can be authenticated and authorized by that API.

## Server

The web service is implemented using the Flask framework, and the REST API will be made available through three base URLs:

1 - /users
For operations related to users.
2 - /bands
For operations related to bands.
3 - /albums
For operations related to albums.

## Client

The client program interactively accepts three operations and their parameters (entered via keyboard in a console), and communicates with the server for it to process the operations and store the information in a database.

| Command | Params                              | Observations                                |
| ------- | ----------------------------------- | ------------------------------------------- |
| ADD     | USER <username> <password> <name>   |                                             |
| ADD     | BAND <gender> <name> <year>         | gender = pop\rock\indy\metal\trance\classic |
| ADD     | ALBUM <band_id> <name> <album year> |                                             |
| ADD     | <user_id> <album_id> <rate>         | rate = 1\2\3\4\5                            |

| Command | Params                       | Observations     |
| ------- | ---------------------------- | ---------------- |
| SHOW    | USER <user_id>               |                  |
| SHOW    | BAND <band_id>               |                  |
| SHOW    | ALBUM <album_id>             |                  |
| SHOW    | ALL <USERS \ BANDS \ ALBUMS> |                  |
| SHOW    | ALL ALBUMS_B <band_id>       |                  |
| SHOW    | ALL ALBUMS_U <user_id>       |                  |
| SHOW    | ALL ALBUMS <rate>            | rate = 1\2\3\4\5 |

| Command | Params                       | Observations     |
| ------- | ---------------------------- | ---------------- |
| REMOVE  | USER <user_id>               |                  |
| REMOVE  | BAND <band_id>               |                  |
| REMOVE  | ALBUM <album_id>             |                  |
| REMOVE  | ALL <USERS \ BANDS \ ALBUMS> |                  |
| REMOVE  | ALL ALBUMS_B <band_id>       |                  |
| REMOVE  | ALL ALBUMS_U <user_id>       |                  |
| REMOVE  | ALL ALBUMS <rate>            | rate = 1\2\3\4\5 |

| Command | Params                            |
| ------- | --------------------------------- |
| UPDATE  | USER <user_id> <password>         |
| UPDATE  | ALBUM <album_id> <rate> <user_id> |

## Dependencies

- Python 3.X

## Run Locally

Start the server

```bash
  python server.py
```

Start the client

```bash
  python client.py
```
