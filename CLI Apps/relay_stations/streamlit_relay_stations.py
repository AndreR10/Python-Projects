
# 2018-2019 Programação 2 LTI
# Grupo 12
# 53299 André Ramos
# 53325 Manuel Machado

import sys
import streamlit as st
import ast
import time

class Node(object):
    def __init__(self, id, name, power, generation):
        """
        Creates Node Object

        Requires: (id = int), (name = string), (power = int), (generation = int)
        """
        self.id = id
        self.name = name
        self.power = power
        self.generation = generation

    def get_id(self):
        """
        Gets id atribute.
        """
        return self.id

    def get_name(self):
        """
        Get name atribute.
        """
        return self.name

    def get_power(self):
        """
        Get power atribute.
        """
        return self.power

    def get_generation(self):
        """
        Get generation atribute.
        """
        return self.generation

    def all_info(self):
        '''
        Gives a representation of each node atribiutes
        '''
        return "ID: " + str(self.id) + " | NAME: " + self.name + " | POWER: " + str(self.power) + " | GENERATION: " + str(self.generation)

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        """
        Creates Edges of each Node

        Requires: (src = string), (dest = string).
        """
        self.src = src
        self.dest = dest

    def get_source(self):
        """
        Gets Source.
        """
        return self.src

    def get_destination(self):
        """
        Gets Destination.
        """
        return self.dest

    def __str__(self):
        """
        Gives the string representation of source name and destination name.
        """
        return self.src.get_name() + '->' + self.dest.get_name()


class Digraph(object):

    def __init__(self):
        """
        Nodes is a list of the nodes in the graph.

        Edges is a dict mapping each node to a list of its children.
        """

        self.nodes = []
        self.edges = {}

    def add_node(self, node):
        """
        Adds the nodes.
        """
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def add_edge(self, edge):
        """
        Adds the edges.
        """
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def children_of(self, node):
        """
        Gives the edges of node
        """
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def __str__(self):
        '''
        Gives the string representation off the connection between source and dest.
        '''
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.get_name() + '->'\
                    + dest.get_name() + '\n'
        return result


class Graph(Digraph):

    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        Digraph.add_edge(self, rev)


def print_path(path):
    """
    Requires: path a list of nodes
    """
    result = ''

    for i, station in enumerate(path):
        result += str(station)
        if i != len(path) - 1:
            result += '->'
    return result


def DFS(graph, start, end, path, best_time, time):
    """
    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes
    Ensures:
    a shortest path from start to end in graph
    """
    path = path + [start]

    if start == end:
        return time

    for node in graph.children_of(start):
        if node not in path and path_generation(path) > 97 < node.get_generation():
            father_generation = start.get_generation()
            child_generation = node.get_generation()
            if father_generation == child_generation == 99:
                time += start.get_power()**-1
            elif father_generation == 98 or child_generation == 98:
                time += (start.get_power()**-1) * 2
            if best_time == 0 or time < best_time:
                best_time = DFS(graph, node, end, path, best_time, time)

        elif node not in path and path_generation(path) == node.get_generation():
            time += (start.get_power()**-1) * 4
            if best_time == 0 or time < best_time:
                best_time = DFS(graph, node, end, path, best_time, time)

        time = 0

    return best_time


def path_generation(path):
    """
    Requires:
    path a path
    Ensures:
    path generation
    """
    generation = 97
    for node in path:
        if (node.get_generation() > generation):
            generation = node.get_generation()
    return generation


def search(graph, start, end):
    """
    Requires:
    graph  a Digraph;
    start and end are nodes
    Ensures:
    shortest path from start to end in graph
    """
    time = 0
    if (start.get_id() != end.get_id()):
        time = DFS(graph, start, end, [], 0, 0)
        if time == 0:
            return "{} <-> {} do not communicate \n".format(start.get_name(),  end.get_name())
        else:
            return "{} <-> {} have communicate  in {}s \n".format(start.get_name(),  end.get_name(), time)
    


def find_station(stations, name):
    """
    Requires:
    stations a list of stations ?
    name is a string tha is the name of the station we are loking for
    Ensures:
    gives the name of the station and none when not found
    """
    
    for idx, station in enumerate(stations):
       
        if station.get_name() == name:
            
            return station
   
    return None


def main():
    '''
    Main function that receives args as the files given in the shell to iniciate program operation
    Requires:
    args is the older for the multiple files given to be read
    Ensures:
    Creates the output file with the stations time connections
    '''

    st.title("Relay Stations Project")


    stations_file = st.file_uploader("Upload stations network file", type="txt")

    
    stations = []
    conns = []
    
    if stations_file is not None:
        data_rows = []
   
        stations_file_contents = stations_file.read().decode("utf-8")
        for line in stations_file_contents.split("\n"):
            if line and line[0] == "#":
                column_names = line[1:].split(', ')
          
            if line and line[0] != "#":
                
               
                station_info = line.split(", ")
                row = station_info[:4]
            
                stations.append(Node(int(station_info[0]),
                                    station_info[1].strip(),
                                    int(station_info[2]),
                                    int(station_info[3])))
                
       
                tuple_str = station_info[4:]
           
                conns_tuple = [int(val.strip("(')\r ")) for val in tuple_str]

                # Convert the integers to strings
                str_list = [str(num) for num in conns_tuple]

                # Join the strings with commas
                result_string = ', '.join(str_list)
          
                row.append(result_string)

                data_rows.append(row)

                conns.append(conns_tuple)
        
      
        st.subheader("Stations list")
        # Display the column names and data in a table        
        st.table([column_names] + data_rows)

        g = Digraph()

        for station in stations:
            g.add_node(station)

        aux = 0

        for station in stations:
            
            for s in conns[aux]:
           
                pos = s - 1
               
                g.add_edge(Edge(station, stations[pos]))
            aux += 1
    
    else:
        st.text("Please provide the needed files.")

    test_file = st.file_uploader("Upload test file", type="txt")

    if test_file is not None:
        
        test_file_contents = test_file.read().decode("utf-8")
        results = []
        count = 0
        max_test = len(test_file_contents.split("\n"))

        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for line in test_file_contents.split("\n"):
          
            line = line.replace("\n", "")
            station_names = line.split(" ")

            stop = False

            station_a = find_station(stations, station_names[0])

            if station_a is None:
               
                results.append(station_names[0] + " out of the network\n")
                stop = True

            station_b = find_station(stations, station_names[1])
    
            if station_b is None:
              
                results.append(station_names[1] + " out of the network\n")
                stop = True


            if not stop:
                
                results.append(str(search(g, station_a, station_b)) + "\n")
          
            count += 1
            percentage = int(count * 100 / max_test)
            print(percentage)
            time.sleep(0.001)
            my_bar.progress(percentage, text=progress_text)
        
        for result in results:
            st.write(result)
    else:
        st.text("Please provide the needed files.")
    


if __name__ == "__main__":
    main()