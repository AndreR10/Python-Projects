# Description

The overall objective of the project is to implement a web service to manage a simplified system for classifying music albums by users. The implementation will use the REST architectural style and a relational database accessible through SQL. For this purpose, the server will use the Flask web development framework and the SQLite database engine. The client program will utilize the requests module to implement client/server interaction based on HTTP.

## Database Schema

![Database schema]([https://via.placeholder.com/468x300?text=App+Screenshot+Here](https://github.com/AndreR10/Python-Projects/blob/main/Web%20Apps/Flask/distributed_application/v1/database_schema.png))

The intended application has an initialization routine that checks if the database already exists. If it doesn't exist, it creastes and initializes with the provided code (table creation and insertion of records into the rates table).

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
