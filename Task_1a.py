from data_load import bidirectional_edges
from data_load import stations_1
from single_source_shortest_paths import initialize_single_source, relax
from min_heap_priority_queue import MinHeapPriorityQueue
import time
start_time = time.time()

# Assuming the code for print_path is available

def dijkstra(G, s, end):
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
            relax(u, v, edge.get_weight(), d, pi,
                  lambda v: queue.decrease_key(v, d[u] + edge.get_weight()))

    return d, pi


def print_path(pi, s, v, mapping_func):
    if v == s:
        return [mapping_func(s)]
    elif pi[v] is None:
        return None
    else:
        return print_path(pi, s, pi[v], mapping_func) + [mapping_func(v)]


if __name__ == "__main__":
    from adjacency_list_graph import AdjacencyListGraph

    vertices = stations_1
    edges = bidirectional_edges

    starting_v = input("Enter the station you are starting from: ")
    if starting_v not in vertices:
        print("This node does not exist")
    ending_v = input("Enter a destination station: ")
    if ending_v not in vertices:
        print("This node does not exist")

    graph1 = AdjacencyListGraph(len(vertices), True, True)
    for edge in edges:
        graph1.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]), edge[2])

    d, pi = dijkstra(graph1, vertices.index(starting_v), vertices.index(ending_v))

    if d[vertices.index(ending_v)] != float('inf'):
        print(f"Shortest distance from {starting_v} to {ending_v} is {d[vertices.index(ending_v)]} minutes")
        # Get the path from the starting to ending vertices
        path = print_path(pi, vertices.index(starting_v), vertices.index(ending_v), lambda i: vertices[i])

        # Print the result
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
