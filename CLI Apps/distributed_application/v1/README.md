# Description

In this version, the server accepts client connections, receives and processes requests, responds to the client, and terminates the connection. The client initiates a connection request to the server, sends the request to the server, receives the response, and terminates the connection.

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

## Commands

The server will support 6 commands that will be sent by the client as strings with a specific format, and it will also respond with a string indicating the result of processing the command.

In total, there are 7 available commands to use:

- `LOCK` - locks the resource, requiring the specification of the resource to be locked. It returns "TRUE" if the resource is locked, "FALSE" otherwise, and "NONE" if the resource does not exist.
- `RELEASE` - releases the lock on the resource previously locked by the client. It returns "True" if successful and "False" otherwise.
- `STATUS` - returns "True" if the resource is locked and "False" if it is not locked or inactive.
- `STATS` - returns the number of times the resource has been locked out of the permitted K locks.
- `YSTATS` - returns the number of resources currently locked out of the permitted Y resources.
- `NSTATS` - returns the number of available resources out of N.
- `EXIT` - allows the user to terminate the client or the server.

| Command | Request sent by the client                   | Responce of the server                             |
| ------- | -------------------------------------------- | -------------------------------------------------- |
| LOCK    | LOCK <time limit> <resource num> <client_id> | OK or NOK ou UNKNOWN RESOURCE                      |
| RELEASE | RELEASE <resource num> <client_id>           | OK or NOK ou UNKNOWN RESOURCE                      |
| STATUS  | STATUS <resource num>                        | LOCKED or UNLOCKED or DISABLED or UNKNOWN RESOURCE |
| STATS   | STATS <resorce num>                          | <num locks on the resource> or UNKNOWN RESOURCE    |
| YSTATS  | YSTATS                                       | <num locked resources>                             |
| NSTATS  | NSTATS                                       | <num avaiable resources>                           |
