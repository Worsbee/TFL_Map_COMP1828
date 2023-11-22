# import the excel data in the form of a list for the stations (vertices) and a nested list for each station's adjacent station
# (the edges of the graph).
from data_load import bidirectional_edges  # edges
from data_load import stations           # vertices
from single_source_shortest_paths import initialize_single_source, relax
from min_heap_priority_queue import MinHeapPriorityQueue
import time

# Assuming the code for print_path is available

if __name__ == "__main__":
    from adjacency_list_graph import AdjacencyListGraph

    # list of all the stations
    vertices = stations
    # nested list in the structure (station1, station2)
    edges = bidirectional_edges

    starting_v = input("Enter the station you are starting from: ")
    if starting_v not in vertices:
        print("This node does not exist")
    ending_v = input("Enter a destination station: ")
    if ending_v not in vertices:
        print("This node does not exist")

    start_time = time.time()  # Define start_time here

    # create a graph storing all the connections between the stations so dijkstra's algorithm can calculate the shortest paths
    graph1 = AdjacencyListGraph(len(vertices), True, True)
    for edge in edges:
        graph1.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]), 1)  # Weight of 1 representing a stop

    d, pi = dijkstra(graph1, vertices.index(starting_v), vertices.index(ending_v))

    if d[vertices.index(ending_v)] != float('inf'):
        print(f"Shortest number of stops from {starting_v} to {ending_v} is {d[vertices.index(ending_v)]}")
        path = print_path(pi, vertices.index(starting_v), vertices.index(ending_v), lambda i: vertices[i])

        if path is not None:
            result = ", ".join(map(str, path))
            print(f"Shortest path from {starting_v} to {ending_v}: {result}")
        else:
            print(f"No path from {starting_v} to {ending_v}")
    else:
        print(f"No path from {starting_v} to {ending_v}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{elapsed_time} seconds")