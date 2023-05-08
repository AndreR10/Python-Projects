
# Relay Station

It is a software that allows to determine the transmission time of a signal from one station to another in a network using a depth first search approache.


## Functionality

The program receives a network of stations. It also receives two specific stations, A and B, from that network.
The program delivers the shortest possible time (in milliseconds) that a signal takes to travel from one of these stations to the other.

### Input

The program receives pairs of station names and a file containing the description of the (re)transmitter network, with an internal structure for storing similar information to that of the following fragmentary example:

    #Id, Name, Power, Generation, Connected:
    1, Baki, 24, 99, (22, 34, 2, 5)
    2, Murai, 82, 98, (17, 13)
    3, Nanbuko, 17, 98, (24, 5)
    4, Sasume, 103, 97, (11)
where the **Connected** field of a given line stores the IDs of the stations in direct contact with the station described in that line.

### Output

The program produces:

- *"X out of the network"* if X is not part of the network;
- or *"A and B do not communicate"* if there is no signal transmission between A and B;
- or a float indicating the shortest possible time, in milliseconds, that a signal takes to travel from the first of these stations to the other, otherwise.


## General specification

- A signal is transmitted between stations connected directly and transitively between stations in communication mediated by other stations.
- Between two stations **A** and **B** connected indirectly through the mediation of other stations different from **A** and **B**, **B** receives a signal from **A** in **X** milliseconds, where **X** is the sum of the times of each connection between the various other stations involved.
- Between two stations **A** and **B** connected indirectly, there may be more than one path through other stations that connects **A** and **B**: the goal is to consider the path that corresponds to the shortest possible time for the transmission of a signal between **A** and **B**.
- Between two stations **A** and **B**, both with **99G**, connected directly, **B** receives a signal from **A** in **X** milliseconds, where **X** is obtained by the inverse of the power of **A**.
- Between two stations **A** and **B**, in which at least one is with **98G**, connected directly, **B** receives a signal from **A** in **Y** milliseconds, where **Y** is obtained by double the inverse of the power of **A**.
- Between two stations **A** and **B**, in which both are with **97G**, connected directly, **B** receives a signal from **A** in **Y** milliseconds, where **Y** is obtained by quadruple the inverse of the power of **A**.
- A station **A** with **97G** communicates with another station **B** if **B**, and all intermediate stations, if any, are also with **97G**.
- The direct relationships between stations in the network are symmetrical, i.e., if **B** is in a direct relationship with **A**, in the same way, **A** is in a direct relationship with **B** (even if only one of these two directions is recorded in the file with the network description).
- Each of the stations has to be declared in the stations_network.txt file and is declared only once.
## Dependencies

- Python 3.XX
## Run Locally

#### Clone the project

```bash
  git clone https://github.com/AndreR10/Python-Projects.git
```

#### Go to the project directory

```bash
  cd Python-Projects/CLI\Apps/relay_stations
```

#### Sofware execution

```bash
  python relay_stations.py station_network.txt test_set.txt results_test_set.txt
```

- `station_network.txt` is a file with the network of stations in the format exemplified above;
- `test_set.txt` is a file with a pair of station names per line, as in the following;
- `results_test_set.txt` is the name of the file where the results for each pair in `test_set.txt` are written, in the respective order.
