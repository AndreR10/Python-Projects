__author__ = "André Ramos"
__email__ = "fc53299@alunos.fc.ul.pt"

from math import dist, sqrt
import argparse
import functools
from cities import cities as cities_dict





def get_geo(pairs):
    """
    Collects the lat and long coordinates of each city in the pair found in the city dictionary.
    Args:
        pairs (tuple): The pair of cities.
    Returns:
        list: The list with the pair in coordinates.
    """
    return list(map(lambda x: (cities_dict.get(x[0]), cities_dict.get(x[1])), pairs))


def city_dist(c):
    """ 
    Calculates the distance between two points.
    Args:
        c (tuple): Tuple of tuples with the coordinates of the two cities.

    Returns:
        float: The distance between the two cities.
    """
    


    # Old version
    geo = list(map(lambda x: (x[0] * 111.1949, x[1] * 85.1102), c))


    return sqrt((geo[1][0] - geo[0][0])**2 + (geo[1][1] - geo[0][1])**2)




"""
    Características     |   Blocos    |    
lista = 2               | True, False |
lista > 2               | True, False | 
lista contem duplicados | True, False |

    Características e Blocos    |                   Testes
        = 2  | > 2   | Dupl     |       Entrada                              Resultado
        ------------------------------------------------------------------------------
        True | False | False    | ['Lisboa', 'Porto']                         271.407
        True | False | True     | ['Lisboa', 'Lisboa']                            0.0
        False| True  | True     | ['Lisboa', 'Porto', 'Porto']                271.407
        False| True  | True     | ['Lisboa', 'Coimbra', 'Porto', 'Coimbra']   271.407
"""


def itinerary_distance(cities_list):
    """
    Calculates the total distance of a given itinerary.

    Pre:
        The list contains at least 2 cities.
    Args:
        list_cidades (list): List of cities.
    Returns:
        float: Total distance of an itinerary.

    >>> itinerary_distance(['Lisboa', 'Porto']) #(True, False, False)
    271.407
    >>> itinerary_distance(['Lisboa', 'Lisboa']) #(True, False, True)
    0.0
    >>> itinerary_distance(['Lisboa', 'Porto', 'Porto']) #(False, True, True)
    271.407
    >>> itinerary_distance(['Lisboa', 'Coimbra', 'Porto', 'Coimbra']) #(False, True, True)
    385.45
    
    """

    # Reftored version
    it_distance = 0.0
    city_count = len(cities_list)

    for i in range(city_count - 1):
        
        city1 = cities_dict.get(cities_list[i])
     
        city2 = cities_dict.get(cities_list[i+1])
        
        it_distance += city_dist((city1, city2))
 
    it_distance = round(it_distance, 3)

    return it_distance
  
    


# itinerary_distance(['Lisboa', 'Setúbal', 'Coimbra', 'Aveiro', 'Viseu', 'Porto']))
#__________________________________________________________________________________________|
"""
            Características                         |   Blocos    |                
dist cidade-destino > dist origem-destino           | True, False |
cidade next origem                                  | True, False | 
cidade before destino                               | True, False |
cidade in itinerario                                | True, False |

Características e Blocos           |                   Testes
d(c)>d(o) | next  | before | in    |       Entrada                                          Resultado
----------------------------------------------------------------------------------------------------------------------------
False     | False | False  | False | (['Lisboa', 'Setúbal', 'Aveiro', 'Porto'], 'Viseu')                ['Lisboa', 'Setúbal', 'Porto']
True      | True  | True   | False | (['Lisboa', 'Porto'], 'Setúbal')                                   ['Lisboa', 'Setúbal', 'Porto']
False     | False | True   | False | (['Lisboa', 'Setúbal', 'Porto'], 'Aveiro')                         ['Lisboa', 'Setúbal', 'Aveiro', 'Porto']
False     | True  | True   | False | (['Lisboa', 'Porto'], 'Aveiro')                                    ['Lisboa', 'Aveiro', 'Porto']
False     | False | True   | True  | (['Lisboa', 'Setúbal', 'Aveiro', 'Porto'], 'Aveiro')               ['Lisboa', 'Setúbal', 'Aveiro', 'Porto']
False     | False | False  | True  | (['Lisboa', 'Setúbal', 'Coimbra', 'Aveiro', 'Porto'], 'Coimbra')   ['Lisboa', 'Setúbal', 'Coimbra', 'Aveiro', 'Porto']
"""


def add_city(itinerary, city):
    """
    Adds a given city to a given itinerary, considering the optimal route between the origin and destination.

    Pre:
        The itinerary must be organized, and the city must not exist in the itinerary.
    Args:
        itinerary (list): Itinerary to which the city will be added.
        city (str): City to be added.
    Returns:
        list: The itinerary with the new city added.

    >>> add_city(['Lisboa', 'Setúbal', 'Aveiro', 'Porto'], 'Viseu') #(False, False, False, False)
    ['Lisboa', 'Setúbal', 'Viseu', 'Aveiro', 'Porto'] 
    >>> add_city(['Lisboa', 'Porto'], 'Setúbal') #(True, True, True, False)
    ['Lisboa', 'Setúbal', 'Porto']
    >>> add_city(['Lisboa', 'Setúbal', 'Porto'], 'Aveiro') #(False, False, True, False)
    ['Lisboa', 'Setúbal', 'Aveiro', 'Porto']
    >>> add_city(['Lisboa', 'Porto'], 'Aveiro') #(False, True, True, False)
    ['Lisboa', 'Aveiro', 'Porto']
    >>> add_city(['Lisboa', 'Setúbal', 'Aveiro', 'Porto'], 'Aveiro') #(False, False, True, True)
    ['Lisboa', 'Setúbal', 'Aveiro', 'Porto']
    >>> add_city(['Lisboa', 'Setúbal', 'Coimbra', 'Aveiro', 'Porto'], 'Coimbra') #(False, False, False, True)
    ['Lisboa', 'Setúbal', 'Coimbra', 'Aveiro', 'Porto']
    """
    
    start = itinerary.pop(0)
    end = itinerary.pop(len(itinerary) - 1)
    itinerary.insert(len(itinerary) // 2, city)
    pair_distances = list(
        map(city_dist, get_geo([(end, x) for x in itinerary])))

    citys_dist_dict = {
        itinerary[i]: pair_distances[i]
        for i in range(len(itinerary))
    }

    sorted_tuples = sorted(citys_dist_dict.items(),
                           key=lambda item: item[1],
                           reverse=True)

    new_iti = list({k: v for k, v in sorted_tuples}.keys())
    new_iti.insert(0, start)
    new_iti.insert(len(new_iti), end)

    return new_iti


#  print(add_city(['Lisboa', 'Setúbal', 'Coimbra', 'Viseu', 'Porto'], 'Aveiro'))

#__________________________________________________________________________________________|
"""
            Características                         |   Blocos    |                
origem = destino                                    | True, False |
list >= 1                                           | True, False | 
origem or destion in list                           | True, False |


Características e Blocos |                        Testes
o = d  |  >= 1  |  o in  |            Entrada                                          Resultado
----------------------------------------------------------------------------------------------------------------------------
False  |  False | False  | ('Lisboa', 'Porto', [])                                 ['Lisboa', 'Porto']
True   |  False | False  | ('Lisboa', 'Lisboa', [])                                ['Lisboa', 'Lisboa']
True   |  True  | False  | ('Lisboa', 'Lisboa', ['Porto'])                         ['Lisboa', 'Porto', 'Lisboa']
True   |  True  | True   | ('Lisboa', 'Porto', ['Lisboa'])                         ['Lisboa', 'Lisboa', 'Porto']
False  |  True  | False  | ('Lisboa', 'Porto', ['Viseu', 'Coimbra'])               ['Lisboa', 'Coimbra', 'Viseu', 'Porto']
False  |  True  | True   | ('Lisboa', 'Porto', ['Setúbal', 'Coimbra', 'Lisboa'])   ['Lisboa', 'Setúbal', 'Lisboa', 'Coimbra', 'Porto']
"""


def build_itinerary(origin, destiny, cities_list):
    """ 
    Builds an itinerary between the origin and destination using a given set of cities.

    Args:
        origem (str): The city where the itinerary will start.
        destino (str): The city where the itinerary will end.
        lista_cidades (list): The list of cities that will make up the itinerary.
    Returns:
        list: The complete itinerary with all the cities.


    >>> build_itinerary('Lisboa', 'Porto', []) #(False, False, False)
    ['Lisboa', 'Porto']
    >>> build_itinerary('Lisboa', 'Lisboa', []) #(True, False, False)
    ['Lisboa', 'Lisboa']
    >>> build_itinerary('Lisboa', 'Lisboa', ['Porto']) #(True, True, False)
    ['Lisboa', 'Porto', 'Lisboa']
    >>> build_itinerary('Lisboa', 'Porto', ['Lisboa']) #(True, True, True)
    ['Lisboa', 'Lisboa', 'Porto']
    >>> build_itinerary('Lisboa', 'Porto', ['Viseu', 'Coimbra']) #(False, True, False)
    ['Lisboa', 'Coimbra', 'Viseu', 'Porto']
    >>> build_itinerary('Lisboa', 'Porto', ['Setúbal', 'Coimbra', 'Lisboa']) #(False, True, True)
    ['Lisboa', 'Setúbal', 'Lisboa', 'Coimbra', 'Porto']
    """

    itinerary = [origin, destiny]
    final_itinerary = functools.reduce(add_city, cities_list, itinerary)

    return final_itinerary


# build_itinerary('Lisboa', 'Porto',
#                      ['Viseu', 'Coimbra', 'Aveiro', 'Setúbal'])

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Calculate itinerary distance and build itinerary')

    # Add the arguments
    parser.add_argument('origin', type=str, help='The city where the itinerary will start')
    parser.add_argument('destination', type=str, help='The city where the itinerary will end')

    # Parse the arguments
    args = parser.parse_args()

    # Get the values from the arguments
    origin = args.origin
    destination = args.destination

    # Get the keys of cities_dict
    city_keys = list(cities_dict.keys())

    # Prompt the user for the list of cities
    cities = []

    while True:
        city = input("Enter a city (or 'done' to finish): ")
        if city.lower() == "done":
            break
        elif city.lower() == "list":
            print(city_keys)
            continue
        while city not in cities_dict:
            
            if city.lower() == "done":
                break
            elif city.lower() == "list":
                print(city_keys)
                continue
                
            
            city = input("Enter a city ('done' to finish | 'list' for list of cities): ")
        cities.append(city)


    # Call the functions with the provided arguments
    
    itinerary = build_itinerary(origin, destination, cities)
    itinerary_distance = itinerary_distance(itinerary)

    # Print the results
    print(f"Itinerary Distance: {itinerary_distance}km")
    itinerary_string = "Itinerary: "
    for city in itinerary:
        itinerary_string += f"-> {city} " 
    print(itinerary_string)
