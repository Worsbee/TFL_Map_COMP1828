from openpyxl import load_workbook
from adjacency_list_graph import AdjacencyListGraph
import matplotlib.pyplot as plt
import numpy as np
from data_load import *
from dijkstra import dijkstra

# Function to calculate journey times using Dijkstra's algorithm
def calculate_journey_times(graph, source):
    distances, _ = dijkstra(graph, source)
    return distances


# Create the graph
print(bidirectional_edges)
graph = get_graph(stations, bidirectional_edges)

# Calculate journey times before the closure
pre_closure_journey_times = {}
for edge in bidirectional_edges:
    source, target = edge
    journey_times = calculate_journey_times(graph, source)
    pre_closure_journey_times[edge] = journey_times[graph.get_vertex_index(target)]

# Introduce the closure (for example, by removing an edge)
# Assume closure between 'station_a' and 'station_b'
# graph.remove_edge(graph.get_vertex_index('station_a'), graph.get_vertex_index('station_b'))

# Calculate journey times after the closure
post_closure_journey_times = {}
for edge in bidirectional_edges:
    source, target = edge
    journey_times = calculate_journey_times(graph, source)
    post_closure_journey_times[edge] = journey_times[graph.get_vertex_index(target)]

# Create histograms
def plot_histogram(data, title, xlabel, ylabel):
    plt.hist(data.values(), bins=20, alpha=0.5, label='After Closure', color='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

# Plot histograms for journey times
plot_histogram(pre_closure_journey_times, 'Journey Times Before Closure', 'Time (minutes)', 'Frequency')
plot_histogram(post_closure_journey_times, 'Journey Times After Closure', 'Time (minutes)', 'Frequency')



