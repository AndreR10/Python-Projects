# Description

In this version 2 the communication is serialized, and the messages exchanged between the client and server follow the format presented in Table bellow, using lists. The client sends a list containing the operation code it wants the server to perform, as well as its parameters. In response, the server will also send a list, with an operation code that will always be the code sent by the client plus one unit. In addition to this, the server will send a result value that replaces the strings from the previous version 1 `("OK", "NOK", "UNKNOWN RESOURCE", "DISABLE", ...)`. For example, if a person identified by client ID 15 enters the command `"LOCK 100 20"`, the client program will send the list `[10, 100, 20, 15]`, and the server will respond with `[11, None]` if resource 20 does not exist.

## Commands

| Command | Request sent by the client                      | Responce of the server                |
| ------- | ----------------------------------------------- | ------------------------------------- |
| LOCK    | [10, <time limit>, <resource num>, <client id>] | [11, True] or [11, False], [11, None] |
| RELEASE | [20, <resource num>, <client id>]               | [21, True] or [21, False], [21, None] |
| STATUS  | [30, <resource num>]                            | [31, True] or [31, False], [31, None] |
| STATS   | [40, <resource num>]                            | [41, True] or [41, False], [41, None] |
| YSTATS  | [50]                                            | [51, <num locked resources in k>]     |
| NSTATS  | [60]                                            | [61, <num avaiable resouces>]         |

## Usage/Examples

#### Server

```bash
python lock_server.py <port> <num resources> <num lock per resources> <num resource locked at the same time> <time limit>
```

The server should receive the following parameters through the command line, in the presented order:

- `<port>` : TCP port where it will listen for connection requests;

- `<num resources>` : number of resources to be managed by the server (N);

- `<num lock per resources>` : number of allowed locks per resource (K);

- `<number resource locked at the same time>` : maximum number of resources that can be locked at a given time (Y).

- `<time limit>` : The timeout for each lock.

#### Client

```bash
python lock_client.py <client_id> <server> <port>
```

The client, to be implemented in the provided file lock_client.py, should receive the following parameters through the command line, in the presented order:

- `<client_id>` : Unique client ID.

- `<server>` : IP address of the server providing the resources.

- `<port>` : TCP port where the server receives connection requests.
