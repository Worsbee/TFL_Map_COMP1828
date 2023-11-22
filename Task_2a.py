# import the excel data in the form of a list for the stations (vertices) and a nested list for each station's adjacent station
# (the edges of the graph).
from data_load import bidirectional_edges  # edges
from data_load import stations           # vertices
from single_source_shortest_paths import initialize_single_source, relax
from min_heap_priority_queue import MinHeapPriorityQueue
import time

# Assuming the code for print_path is available

def dijkstra(G, s, end):
    """Solve single-source shortest-paths problem with no negative-weight edges.

	Arguments:
	G -- a directed, weighted graph
	s -- index of source vertex
	Assumption:
	All weights are nonnegative

	Returns:
	d -- distances from source vertex s
	pi -- predecessors
	"""
    card_V = G.get_card_V()

    d, pi = initialize_single_source(G, s)

    queue = MinHeapPriorityQueue(lambda u: d[u])
    for u in range(card_V):
        queue.insert(u)

    while queue.get_size() > 0:
        u = queue.extract_min()
        if u == end:
            break
        for edge in G.get_adj_list(u):
            v = edge.get_v()
            relax(u, v, 1, d, pi,  # *NEW* Assume each edge has a weight of 1 representing a stop
                  lambda v: queue.decrease_key(v, d[u] + 1))
    # returns the shortest distance from one station to another, plus a list storing all the predecessors of the ending station
    return d, pi

def print_path(pi, s, v, mapping_func):
    # this function takes in the predecessor list, the indexes of the starting and destination stations
    #to print the path from one station to another (this function is used to give a list of all the stations the user passes to get to their destination)
    if v == s:
        return [mapping_func(s)]
    elif pi[v] is None:
        return None
    else:
        return print_path(pi, s, pi[v], mapping_func) + [mapping_func(v)]

if __name__ == "__main__":
    from adjacency_list_graph import AdjacencyListGraph

    # list of all the stations
    vertices = stations
    # nested list in the structure (station1, station2)
    edges = bidirectional_edges

    # takes user travel input
    starting_v = input("Enter the station you are starting from: ")
    if starting_v not in vertices:
        # checks if the station entered by the user exists in the vertices list
        print("This node does not exist")
    ending_v = input("Enter a destination station: ")
    if ending_v not in vertices:
        print("This node does not exist")

    # create a graph storing all the connections between the stations so dijkstra's algorithm can calculate the shortest paths
    graph1 = AdjacencyListGraph(len(vertices), True, True)
    for edge in edges:
        graph1.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]), 1)  # Weight of 1 representing a stop

    d, pi = dijkstra(graph1, vertices.index(starting_v), vertices.index(ending_v))

    if d[vertices.index(ending_v)] != float('inf'):
        # *NEW* prints amount of stops from one station to another
        print(f"Shortest number of stops from {starting_v} to {ending_v} is {d[vertices.index(ending_v)]}")  # *NEW* changed from shortest distance to shortest number of stops
        # Get the path from the starting to ending vertices
        # run path function
        path = print_path(pi, vertices.index(starting_v), vertices.index(ending_v), lambda i: vertices[i])

        # prints the result
        if path is not None:
            result = ", ".join(map(str, path))
            print(f"Shortest path from {starting_v} to {ending_v}: {result}")  # prints the path from one station to another
        else:
            print(f"No path from {starting_v} to {ending_v}")
    else:
        print(f"No path from {starting_v} to {ending_v}")

#    end_time = time.time()
#  elapsed_time = end_time - start_time
#   print(f"{elapsed_time} seconds")  #prints running time of the algorithm