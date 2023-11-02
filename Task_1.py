from data_load import bidirectional_edges   # importing nested list with all [stations, next station, time]
from data_load import stations              # importing list of all the stations to be the vertices
from single_source_shortest_paths import initialize_single_source, relax   # importing graph - adjacency list graph
from min_heap_priority_queue import MinHeapPriorityQueue     # importing queue


def dijkstra(G, s, end):
    # G takes in a bidirectional, weighted graph. S is the starting vertex and end is the ending vertex.
    # This function returns d distances from the source vertex s and pi for the predecessors

    card_V = G.get_card_V()

    d, pi = initialize_single_source(G, s)

    # Key function for the priority queue is distance.
    queue = MinHeapPriorityQueue(lambda u: d[u])
    for u in range(card_V):
        queue.insert(u)

    while queue.get_size() > 0:  # while the priority queue is not empty
        u = queue.extract_min()  # extract a vertex with the minimum distance
        # If the end node has been reached stop the algorithm
        if u == end:
            break
        # Relax each edge and update d and pi.
        for edge in G.get_adj_list(u):
            v = edge.get_v()
            # Upon each relaxation, decrease the key in the priority queue.
            relax(u, v, edge.get_weight(), d, pi,
                  lambda v: queue.decrease_key(v, d[u] + edge.get_weight()))

    return d, pi


# Testing
if __name__ == "__main__":

    from adjacency_list_graph import AdjacencyListGraph
    vertices = stations
    edges = bidirectional_edges
    # prompt user to input a starting station
    starting_v = input("Enter the station you are starting from: ")
    if starting_v in vertices:   # check if the station exists in the vertices list
        pass
    else:
        print("This node does not exist")
    # prompt user for a final destination
    ending_v = input("Enter a destination station: ")
    if ending_v in vertices:  # check if the final destination is in the vertices list
        pass
    else:
        print("This node does not exist")
    graph1 = AdjacencyListGraph(len(vertices), True, True)
    for edge in edges:
        graph1.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]), edge[2])
    d, pi = dijkstra(graph1, vertices.index(starting_v), vertices.index(ending_v))

    # Print the distance between the starting and ending vertices
    if d[vertices.index(ending_v)] != float('inf'):
        print(f"Shortest distance from {starting_v} to {ending_v} is {d[vertices.index(ending_v)]} minutes")
        #print(pi[ending_v])
    else:
        print(f"No path from {starting_v} to {ending_v}")


    # Getting all the stations passed by the user by storing all of the predecessors of the ending vertex in a list
    if d[vertices.index(ending_v)] != float('inf'):
        print(f"Shortest distance from {starting_v} to {ending_v} is {d[vertices.index(ending_v)]} minutes")

        # Backtrack from the ending vertex to the starting vertex using the "pi" array
        path = []
        current_vertex = vertices.index(ending_v)
        while current_vertex != vertices.index(starting_v):
            path.append(vertices[current_vertex])
            current_vertex = pi[current_vertex]
        path.append(starting_v)
        path.reverse()

        # Print the path (predecessors) from ending to starting
        print(f"Path from {starting_v} to {ending_v}: {' -> '.join(path)}")
    else:
        print(f"No path from {starting_v} to {ending_v}")
