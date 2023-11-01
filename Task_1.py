#!/usr/bin/env python3
# dijkstra.py

# Introduction to Algorithms, Fourth edition
# Linda Xiao and Tom Cormen

#########################################################################
#                                                                       #
# Copyright 2022 Massachusetts Institute of Technology                  #
#                                                                       #
# Permission is hereby granted, free of charge, to any person obtaining #
# a copy of this software and associated documentation files (the       #
# "Software"), to deal in the Software without restriction, including   #
# without limitation the rights to use, copy, modify, merge, publish,   #
# distribute, sublicense, and/or sell copies of the Software, and to    #
# permit persons to whom the Software is furnished to do so, subject to #
# the following conditions:                                             #
#                                                                       #
# The above copyright notice and this permission notice shall be        #
# included in all copies or substantial portions of the Software.       #
#                                                                       #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,       #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF    #
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                 #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS   #
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN    #
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN     #
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE      #
# SOFTWARE.                                                             #
#                                                                       #
#########################################################################
from data_load import bidirectional_edges
from data_load import stations
from single_source_shortest_paths import initialize_single_source, relax
from min_heap_priority_queue import MinHeapPriorityQueue


def dijkstra(G, s):
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

    # Key function for the priority queue is distance.
    queue = MinHeapPriorityQueue(lambda u: d[u])
    for u in range(card_V):
        queue.insert(u)

    while queue.get_size() > 0:  # while the priority queue is not empty
        u = queue.extract_min()  # extract a vertex with the minimum distance

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
    #from bellman_ford import bellman_ford
    #from generate_random_graph import generate_random_graph

    # Textbook example.
    #vertices = ['a', 'b', 'c', 'd', 'e']
    #edges = [('a', 'b', 6), ('b', 'a', 6), ('a', 'c', 2), ('c', 'a', 2), ('b', 'e', 3), ('e', 'b', 3),
     #        ('b', 'd', 8), ('d', 'b', 8), ('c', 'e', 4), ('e', 'c', 4)]
    vertices = stations
    edges = bidirectional_edges
    starting_v = input("Enter a starting node: ")  # check if node exists
    if starting_v in vertices:
        pass
    else:
        print("This node does not exist")
    graph1 = AdjacencyListGraph(len(vertices), True, True)
    for edge in edges:
        graph1.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]), edge[2])
    d, pi = dijkstra(graph1, vertices.index(starting_v))
    for i in range(len(vertices)):
        print(vertices[i] + ": d = " + str(d[i]) + ", pi = " + ("None" if pi[i] is None else vertices[pi[i]]))
    print()
