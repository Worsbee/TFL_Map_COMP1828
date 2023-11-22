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


def remove_station(edge_list, source_station, destination_station):
    print(source_station, destination_station)

    # Filter edges to including only source_station and destination_station
    source_list = [item for item in edge_list if source_station in item]
    destination_list = [item for item in edge_list if destination_station in item]

    source_destination_list = []

    # Get all entries of both stations in edges
    for element in source_list:
        for item in destination_list:
            if element is item:
                source_destination_list.append(element)
                break

    # Gets numerical index of each station pair in edges
    source_index0 = edge_list.index(source_destination_list[0])
    source_index1 = edge_list.index(source_destination_list[1])

    for element in source_destination_list:
        edge_list.remove(element)

    return edge_list, source_index0, source_index1


if __name__ == "__main__":
    # Rename variables to improve readability
    vertices = stations
    edges = bidirectional_edges

    # Collects input for user
    rm_source_station = input("What is the source station: ")
    rm_destination_station = input("What is the destination station: ")

    # Produces a graph
    graph1 = get_graph(vertices, edges)

    # Produces a breath first search from source and destination
    result_before_source = bfs(graph1, vertices.index(rm_source_station))
    result_before_destination = bfs(graph1, vertices.index(rm_destination_station))

    updated_edges, index0, index1 = remove_station(edges, rm_source_station, rm_destination_station)

    # Produces a graph
    graph2 = (get_graph(vertices, updated_edges))

    # Produces a breath first search from source and destination
    result_after_source = bfs(graph2, vertices.index(rm_source_station))
    result_after_destination = bfs(graph2, vertices.index(rm_destination_station))

    # Print the results
    print(f"Source station before change: \n {result_before_source}")
    print(f"Destination station before change: \n {result_before_source}")
    print(f"Source station after change: \n {result_after_source}")
    print(f"Destination station after change: \n {result_after_destination}")