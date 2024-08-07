Bellman-Ford Algorithm
The Bellman-Ford algorithm is used to find the shortest paths from a single source vertex to all other vertices in a graph. It can handle graphs with negative edge weights, unlike Dijkstra's algorithm. Additionally, it can detect negative weight cycles in the graph.

Key Steps of the Bellman-Ford Algorithm:
Initialization:

Set the distance to the source vertex to 0 and the distances to all other vertices to infinity.
Initialize an empty set of visited vertices.
Relaxation:

For each vertex, apply relaxation for all edges. This process is repeated for a total of (V-1) times, where V is the number of vertices.
Relaxation involves checking if the known distance to a vertex can be improved by taking an edge to another vertex. If so, update the distance.
Negative Weight Cycle Detection:

After V-1 iterations, perform one more iteration to check for negative weight cycles.
If any distance can still be updated, a negative weight cycle exists in the graph.
Completion:
If no negative weight cycles are detected, the algorithm returns the shortest distances from the source to all other vertices.
If a negative weight cycle is detected, the algorithm can report it, indicating that no shortest path solution exists.
