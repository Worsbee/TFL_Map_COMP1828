"""
Description: Finding stations to remove without heavily impacting feasibility
"""

"""
Notes

AdjacentListGraph returns a graph in the format of 'Station[n]: connecting stations (minutes)'
for example Harrow & Wealdstone(stations[0]): 'Kenton'(stations[1]) (2 minutes) == '0: 1 (2)'

Bfs returns the distance of each stations from the source.
"""


from data_load import *
from bfs import bfs
from adjacency_list_graph import AdjacencyListGraph

if __name__ == "__main__":
    # Rename variables to improve readability
    vertices = stations
    edges = bidirectional_edges

    # Produces a graph
    graph1 = get_graph(vertices, edges)

    print(stations)
    result = bfs(graph1, 13)

    print(result)

