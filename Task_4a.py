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
    """Removes the station connection from the edges list"""
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

    try:
        # Gets numerical index of each station pair in edges
        source_index0 = edge_list.index(source_destination_list[0])
        source_index1 = edge_list.index(source_destination_list[1])

    except IndexError:
        print("The stations list are not adjacent on any line")
        exit()

    for element in source_destination_list:
        edge_list.remove(element)

    return edge_list, source_index0, source_index1

def viability_test(rbs, rbd, ras, rad):
    """
    Tests the viability of a connection closure.
    Variables are shorthand for "result"_"before/after"_"source/destination"
    """

    # Counts the number of impossible stations before and after the change
    result_before = str(rbs[0]).count('inf') + str(rbs[1]).count('inf')
    result_after = str(ras[0]).count('inf') + str(ras[1]).count('inf')

    # Rejects any changes which increase the number of impossible stations
    if result_before is not result_after:
        message = "Shut down is not possible as some stations become inaccessible"

    return message

if __name__ == "__main__":
    # Rename variables to improve readability
    vertices = stations
    edges = bidirectional_edges

    # Collects input for user
    rm_source_station = input("What is the source station: ")
    rm_destination_station = input("What is the destination station: ")

    # Produces a graph
    graph1 = get_graph(vertices, edges)

    try:
        # Produces a breath first search from source and destination
        result_before_source = bfs(graph1, vertices.index(rm_source_station))
        result_before_destination = bfs(graph1, vertices.index(rm_destination_station))

    except ValueError:
        print("One or both stations are not recognised")
        exit()

    updated_edges, index0, index1 = remove_station(edges, rm_source_station, rm_destination_station)

    # Produces a graph
    graph2 = (get_graph(vertices, updated_edges))

    # Produces a breath first search from source and destination
    result_after_source = bfs(graph2, vertices.index(rm_source_station))
    result_after_destination = bfs(graph2, vertices.index(rm_destination_station))

    feasible = viability_test(result_before_source, result_before_destination, result_after_source, result_after_destination)

    # Print the results
    print(f"Results for closure between: {rm_source_station} -- {rm_destination_station}")
    print(feasible)


    print(f"Source station before change: {result_before_source}")
    print(f"Destination station before change: {result_before_source}")
    print(f"Source station after change: {result_after_source}")
    print(f"Destination station after change: {result_after_destination}")