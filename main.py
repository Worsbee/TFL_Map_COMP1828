import heapq


class Graph:
	def __init__(self):
		self.graph = {}

	def add_edge(self, u, v, w):
		if u not in self.graph:
			self.graph[u] = []
		self.graph[u].append((v, w))
		if v not in self.graph:
			self.graph[v] = []

	def dijkstra(self, start):
		# Initialize distances and predecessors
		distances = {vertex: float('inf') for vertex in self.graph}
		predecessors = {vertex: None for vertex in self.graph}
		distances[start] = 0

		# Priority queue to keep track of vertices to visit
		priority_queue = [(0, start)]

		while priority_queue:
			current_distance, current_vertex = heapq.heappop(priority_queue)

			# Skip processing if we've already found a shorter path to this vertex
			if current_distance > distances[current_vertex]:
				continue

			for neighbor, weight in self.graph[current_vertex]:
				distance = current_distance + weight

				# If we found a shorter path, update the distance and predecessor
				if distance < distances[neighbor]:
					distances[neighbor] = distance
					predecessors[neighbor] = current_vertex
					heapq.heappush(priority_queue, (distance, neighbor))

		return distances, predecessors

	def shortest_path(self, start, end):
		distances, predecessors = self.dijkstra(start)
		path = []
		current_vertex = end

		while current_vertex is not None:
			path.insert(0, current_vertex)
			current_vertex = predecessors[current_vertex]

		return path


# Example usage:
if __name__ == "__main__":
	graph = Graph()
	graph.add_edge('A', 'B', 6)
	graph.add_edge('A', 'C', 2)
	graph.add_edge('B', 'E', 3)
	graph.add_edge('B', 'D', 8)
	graph.add_edge('C', 'E', 4)
	graph.add_edge('C', 'F', 1)
	graph.add_edge('E', 'F', 2)

	start_node = 'D'
	end_node = 'A'

	shortest_path = graph.shortest_path(start_node, end_node)
	print(f'Shortest path from {start_node} to {end_node}: {shortest_path}')


