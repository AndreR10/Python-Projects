
import sys

class Node(object):
    def __init__(self, ID, name, power, generation):
        """
        Requires: name is a string
        """
        self.id = ID
        self.name = name
        self.power = power
        self.generation = generation
    
    def getId(self):
       return self.id

    def getName(self):
        return self.name
    
    def getPower(self):
        return self.power
    
    def getGeneration(self):
        return self.generation
        
    def allInfo(self):
        return "ID: "+str(self.id)+" | NAME: "+self.name +" | POWER: "+str(self.power)+" | GENERATION: "+str(self.generation)
    
    def __str__(self):
        return self.name
    
    


class Edge(object):
    def __init__(self, src, dest):
        """
        Requires: src and dst Nodes
        """
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()



class Digraph(object):
    #nodes is a list of the nodes in the graph
    #edges is a dict mapping each node to a list of its children
    def __init__(self):
        self.nodes = []
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                + dest.getName() + '\n'
        return result

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

        
def printPath(path):
    """
    Requires: path a list of nodes
    """
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result



def DFS(graph, start, end, path, bestTime,time):
    """
    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes
    Ensures:
    a shortest path from start to end in graph
    """
    path = path + [start]
    
    #print('Current DFS path:', printPath(path))

    if start == end:
        return time
    
    for node in graph.childrenOf(start):
        #checks node to avoid loops and also avoids stations with generation 97 in "superior" paths
        if node not in path and pathGeneration(path) > 97 < node.getGeneration():
            #get father generation
            fatherGeneration = start.getGeneration()
            #get child generation
            childGeneration = node.getGeneration()
            
            #adds the time according to power and generation
            if fatherGeneration == childGeneration == 99:
                time += start.getPower()**-1
            elif fatherGeneration == 98 or childGeneration == 98:
                time += (start.getPower()**-1) * 2
                
            #continues recursive search if time still below the best 
            if bestTime == 0 or time < bestTime:
                bestTime = DFS(graph, node, end, path, bestTime, time)
            
        #takes care of generation 97 paths
        elif node not in path and pathGeneration(path) == node.getGeneration():
            #adds the time according to power and generation
            time += (start.getPower()**-1) * 4
            if bestTime == 0 or time < bestTime:
                 bestTime = DFS(graph, node, end, path, bestTime, time)

        #reset time to 0 for each child node
        time = 0


    return bestTime
            
def pathGeneration(path):
    """
    Requires:
    path a path
    Ensures:
    path generation
    """
    generation = 97
    for node in path:
        if(node.getGeneration() > generation):
            generation = node.getGeneration()
    return generation

def search(graph, start, end):
    """
    Requires:
    graph  a Digraph;
    start and end are nodes
    Ensures:
    shortest path from start to end in graph
    """
    #if not same station
    if(start.getId() != end.getId()):
        #call to path finder algorithm
        time = DFS(graph, start, end, [], 0, 0)
        if time == 0:
            #Didn't find path
            return start.getName() +" and "+end.getName()+" do not communicate"
        
    return 0

def findStation(stations, name):
    """
    """
    #Search in stations for station with given name
    for i in range(len(stations)):
        if(stations[i].getName() == name):
            #returns the station when found
            return stations[i]
    #returns None when not found
    return None


def runMambos(args):
    
    #Init nodes list
    stations = []
    #Init list that will contain each node sub-nodes
    conns = []
    
    #opens file
    file_in = open(args[1], "r")
    
    #runs every line creating Nodes/Station and saves all the sub stations(in str) in conns
    #also ignores lines stating with '#'
    for line in file_in:
        if (line[0] != "#"):
           station_info = line.split(", ")
           stations.append(Node(int(station_info[0]),
                             station_info[1], 
                             int(station_info[2]),
                             int(station_info[3])))
           conns.append(line.split("(")[1].split(", "))
    

    #starts the diagraph
    g = Digraph()   
    
    #add all the stations to the graph
    for station in stations:
        g.addNode(station)
                
    #get the substations(str) from conns and creates edges with the current postion station
    aux = 0
    for station in stations:
        for s in conns[aux]:
            #Fixes the last station in the file ex:  6)
            #IMPORTANT: On macOS the 1st parameter in s.replace needs to be changed to ")\r\n"
            pos = (int(s.replace(")\n", "")))-1
               #adds edge do graph
            g.addEdge(Edge(station, stations[int(pos)]))     
        aux += 1
    
    #closes file
    file_in.close()
    
    #opens 2nd read file
    file_in = open(args[2], "r")
    maxTest = len(file_in.readlines())
    file_in.close()
    file_in = open(args[2], "r")
    #opens 1st output file
    file_out = open(args[3], "w")
    
    count = 0
    for line in file_in:
        #removes break from lines
        line = line.replace("\n", "")
        #splits the line to get the name into a list
        stationNames = line.split(" ")
        
        #flag to stop the execution in case of non existing stations
        stop = False
        
        #gets stationA
        stationA = findStation(stations, stationNames[0])
        if stationA == None:
            file_out.write(stationNames[0] + " out of the network\n")
            stop = True
            
        #gets stationB
        stationB = findStation(stations, stationNames[1])
        if stationB == None:
            file_out.write(stationNames[1] + " out of the network\n")
            stop = True
        
        #if both stations exist executes the search
        if not stop:
            file_out.write(str(search(g, stationA, stationB))+"\n")
            
        count+=1    
        percentage = round(count*100/maxTest,1)
        sys.stdout.write("\r     Progress: "+str(percentage)+"%     |     ")
        sys.stdout.write("Tested: " + str(count) + " of "+str(maxTest)+" connections!")
        sys.stdout.flush()
        
    sys.stdout.write("\n")
       
    #closes files
    file_in.close()
    file_out.close()


def testArgs(args):
    """
    """
    if len(args) != 4:
        print("\nCommand not recognized!\nPlease use: \n     "+
              "$ python relayStations.py <input file1> <input file2> <output file>")
        return False
    return True
    

#bypass = ["","in.txt", "myTestSet.txt", "out.txt"]
    
#checks number os parameters and executes if all ok
if (testArgs(sys.argv)):
    print("\n##########################  Relay Stations  ############################")
    print("\nRelayStations is running...\n")
    runMambos(sys.argv)
    print("\n\nProgram as finished!")
    print("##########################################################################")

