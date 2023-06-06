# Itinerary Distance and Builder

This code calculates the distance of a given itinerary and builds an itinerary between a given origin and destination using a set of cities.

## Prerequisites

- Python 3.x
- math module
- argparse module

## Usage

1. Clone the repository or download the script.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script with the following command:

```bash
python main.py origin destination
```

Replace `main.py` with the actual name of the script file.
Replace `origin` and `destination` with the desired origin and destination cities.

## Example

```bash
python itinerary_builder.py Lisbon Porto
```

## Description

The code consists of several functions:

1. `get_geo(pairs)`: Collects the latitude and longitude coordinates of each city pair found in the city dictionary.

2. `city_dist(c)`: Calculates the distance between two points based on their coordinates.

3. `itinerary_distance(cities_list)`: Calculates the total distance of a given itinerary. It takes a list of cities as input.

4. `add_city(itinerary, city)`: Adds a given city to a given itinerary, considering the optimal route between the origin and destination.

5. `build_itinerary(origin, destination, cities_list)`: Builds an itinerary between the origin and destination using a given set of cities.

The code also includes examples and doctests to demonstrate the usage and expected output of each function.

## Input

The script prompts the user to enter a list of cities. Each city should be entered one at a time, and the input can be terminated by typing "done". Typing "list" will display a list of available cities.

## Output

The script prints the itinerary distance and the complete itinerary as output.

Example Output:

```bash
Itinerary Distance: 271.407km
Itinerary: -> Lisbon -> Setúbal -> Porto
```

## Author

- Name: André Ramos
- Email: andrem.tramos@gmail.com
