"""
Description: Finding stations to remove without heavily impacting feasibility
"""

from data_load import *
from bfs import bfs
from Task_3a import task_3a


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


def check_station(source_station, destination_station, task_4b_bool):
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

    # If called from task 4b and the station is feasible print more information
    if task_4b_bool is True and str(feasible) == "Feasible":
        task_3a(variable_cleaner(source_station), variable_cleaner(destination_station),
                stations, updated_edges)
        ##########################################
        #
        # IMPLEMENT FUNCTION CALL FOR HISTOGRAM HERE
        #
        ##########################################

    print(f"{source_station} -- {destination_station}: {feasible}")


def task_4a(stations, bidrectional_edges, task_4b_bool):

    graph1 = get_graph(stations, bidirectional_edges)
    station_checker = []
    adjacent_stations_text = []

    for station0 in set(stations):

        # Find where the station appears in stations
        station_occurrences = [index for index, item in enumerate(stations)
                               if item == station0]

        # If the station is not the first or last station on a line find the station before and after it
        if station0 != stations[0] and station0 != stations[-1]:
            # Find station adjacent stations
            adjacent_stations = {item + offset for item in
                                 station_occurrences for offset in [-1, 0, 1]}

        # If the station is the first station on a line do not check for stations before it
        elif station0 == stations[0]:
            # Find station adjacent stations
            adjacent_stations = {item + offset for item in
                                 station_occurrences for offset in [0, 1]}

        # If the station is the last station do not check the station after it
        elif station0 == stations[-1]:

            # Find station adjacent stations
            adjacent_stations = {item + offset for item in
                                station_occurrences for offset in [-1, 0]}

        adjacent_stations_text = []

        # Prevents duplicate connections on different lines
        for item in adjacent_stations:
            if stations[item] not in adjacent_stations_text:
                adjacent_stations_text.append(stations[item])

        # Iterate through all adjacent stations
        for station1 in adjacent_stations_text:

            # If the stations are the same skip
            if station1 is station0:
                pass

            # If the station pair has already been calculated skip
            elif station1 in station_checker:
                pass

            # Else check station feasibility
            else:
                check_station(station0, station1, task_4b_bool)

        # Once a station has been checked add station to checker list
        station_checker.append(station0)

if __name__ == "__main__":
    task_4a(stations, bidirectional_edges, False)