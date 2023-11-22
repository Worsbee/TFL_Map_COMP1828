# importing the Excel data in the form of a list of vertices and a nested list of edges
from data_load import bidirectional_edges, stations_clean, stations
from data_load import variable_cleaner, variable_search
# importing the Bellman Ford library code, print_path and AdjacencyListGraph from adjacency_list_graph
from bellman_ford import bellman_ford
from print_path import print_path
from adjacency_list_graph import AdjacencyListGraph

# Running the code
if __name__ == "__main__":
    # assign the vertices and vertices using the imported Excel data
    vertices = stations
    edges = bidirectional_edges

    # Create the Graph
    graph1 = AdjacencyListGraph(len(vertices), True, True)
    for edge in edges:
        graph1.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]), edge[2])

    # prompt the user for a starting and destination station
    # Variable cleaner removes spaces and upper case letters
    source_station = variable_cleaner(input("Enter the source station: "))
    destination_station = variable_cleaner(input("Enter the destination station: "))

    # Reformat stations to their correct capitalised and spaced format for printing
    source_station = variable_search(stations_clean, stations, source_station)
    destination_station = variable_search(stations_clean, stations, destination_station)

    # Check for the existence of the stations in the list of vertices
    if source_station not in vertices or destination_station not in vertices:
        print("One or both of the stations do not exist")
    else:
        # run the bellman_ford algorithm
        d, pi, cycle = bellman_ford(graph1, vertices.index(source_station))
        if d is not None:
            # if there is a distance between the two stations, get the path using the imported print_path function
            path = print_path(pi, vertices.index(source_station), vertices.index(destination_station),
                              lambda i: vertices[i])
            # If there is a path, print the result
            if path is not None:
                result = ", ".join(map(str, path))
                print(f"The Number of stops or stations between: {source_station} and {destination_station} is "
                      f"{len(path)}")
            else:
                print(f"No path from {source_station} to {destination_station}")
