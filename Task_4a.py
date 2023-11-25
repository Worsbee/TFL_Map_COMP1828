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
    # Finds common connections between source and destination stations
    common_elements = [element for element in edge_list if source_station in element and destination_station in element]

    # Removes connections between the two stations
    for element in common_elements:
        edge_list.remove(element)

    return edge_list


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
        message = "Not feasible"

    else:
        message = "Feasible"

    return message


def check_station(source_station, destination_station):
    # Rename variables to improve readability
    vertices = stations
    edges = bidirectional_edges

    source_index = vertices.index(source_station)
    destination_index = vertices.index(destination_station)

    # Produces a graph
    graph2 = get_graph(vertices, edges)

    try:
        # Produces a breath first search from source and destination
        result_before_source = bfs(graph2, source_index)
        result_before_destination = bfs(graph2, destination_index)

    except ValueError:
        print("One or both stations are not recognised")

    updated_edges = remove_station(edges, source_station, destination_station)

    # Produces a graph
    graph2 = get_graph(vertices, updated_edges)

    # Produces a breath first search from source and destination
    result_after_source = bfs(graph2, source_index)
    result_after_destination = bfs(graph2, destination_index)

    feasible = viability_test(result_before_source, result_before_destination, result_after_source,
                              result_after_destination)

    # Print the results
    print(f"{source_station} -- {destination_station} : {feasible}")


if __name__ == "__main__":

    graph1 = get_graph(stations, bidirectional_edges)

    for station0 in stations:
        station_occurrences = [index for index, item in enumerate(stations)
                               if item == station0]

        if station0 != stations[0] and station0 != stations[-1]:
            adjacent_stations = {item + offset for item in
                                 station_occurrences for offset in [-1, 0, 1]}
        elif station0 == stations[0]:
            adjacent_stations = {item + offset for item in
                                 station_occurrences for offset in [0, 1]}
        elif station0 == stations[-1]:
            adjacent_stations = {item + offset for item in
                                station_occurrences for offset in [-1, 0]}

        for station1 in adjacent_stations:

            if stations[station1] is station0:
                pass
            else:
                check_station(station0, stations[station1])
        stations.remove(station0)
