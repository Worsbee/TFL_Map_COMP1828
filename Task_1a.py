 importing other library code and excel data for vertices and edges
from data_load import bidirectional_edges
from data_load import stations_1
# implementation of Dijkstra's algorithm library code
from dijkstra import dijkstra
from print_path import print_path
import time
start_time = time.time()


if __name__ == "__main__":

	from adjacency_list_graph import AdjacencyListGraph

vertices = stations_1
edges = bidirectional_edges

graph1 = AdjacencyListGraph(len(vertices), True, True)
for edge in edges:
	graph1.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]), edge[2])

source_station = input("Enter the source station: ")
destination_station = input("Enter the destination station: ")

# Check for the existence of the stations in the list of vertices
if source_station not in vertices or destination_station not in vertices:
	print("One or both of the stations do not exist")
else:
	# Use Dijkstra's algorithm to find the shortest path and distance
	source_index = vertices.index(source_station)
	destination_index = vertices.index(destination_station)

	d, pi = dijkstra(graph1, source_index)

	if d[destination_index] != float('inf'):
		# Print the shortest distance and path
		print(f"Shortest distance from {source_station} to {destination_station} is {d[destination_index]} minutes")
		# Get the path from the starting to ending vertices
		path = print_path(pi, vertices.index(source_station), vertices.index(destination_station), lambda i: vertices[i])

		# Print the result
		if path is not None:
			result = ", ".join(map(str, path))
			print(f"Shortest path from {source_station} to {destination_station}: {result}")
		else:
			print(f"No path from {source_station} to {destination_station}")
	else:
		print(f"No path from {source_station} to {destination_station}")

	end_time = time.time()
	elapsed_time = end_time - start_time
	# print the running time of the algorithm
	print(f"{elapsed_time} seconds")
