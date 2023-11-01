"""
This project has been changed for testing
"""

vertices = ['s', 't', 'x', 'y', 'z']
edges = [('s', 't', 10), ('s', 'y', 5), ('t', 'x', 1), ('t', 'y', 2), ('x', 'z', 4),
         ('y', 't', 3), ('y', 'x', 9), ('y', 'z', 2), ('z', 's', 7), ('z', 'x', 6)]

dijkstra(edges, vertices)

