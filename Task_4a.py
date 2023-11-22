"""
Description: Finding stations to remove without heavily impacting feasibility
"""

"""
Notes

AdjacentListGraph returns a graph in the format of 'Station[n]: connecting stations (minutes)'
for example Harrow & Wealdstone(stations[0]): 'Kenton'(stations[1]) (2 minutes) == '0: 1 (2)'

Bfs returns the distance of each stations from the source. Output is in original order for example
the first element of the list is stations[0]. The numbers in the place of stations is the distance from the
input source in stops.
"""

from data_load import *
from bfs import bfs


def remove_station(source_station, destination_station):
    pass


if __name__ == "__main__":
    # Rename variables to improve readability
    vertices = stations
    edges = bidirectional_edges

    # Collects input for user
    # rm_source_station = input("What is the source station: ")
    # rm_destination_station = input("What is the destination station: ")

    # Get all entries of both stations in edges
    # source_destination = [element for element in source if rm_destination_station in element]

    # Gets numerical index of each station pair in edges
    # source_index0 = edges.index(source_destination[0])
    # source_index1 = edges.index(source_destination[1])

    # Produces a graph
    graph1 = get_graph(vertices, edges)

    # Produces a breath first search from source and destination
    result = bfs(graph1, 0)

    print(result)

    i = 0
    for x in result:
        i += 1

    print(i)

    """
    result1 = bfs(graph1, destination_index)

    remove_station(source, destination)

    # Produces a graph
    graph2 = (get_graph(vertices, edges))

    # Produces a breath first search from source and destination
    rm_result = bfs(graph1, source_index)
    rm_result1 = bfs(graph1, destination_index)

 
    print(edges)

    print(result)
    print(rm_result)

    print(result1)
    print(rm_result1)
"""