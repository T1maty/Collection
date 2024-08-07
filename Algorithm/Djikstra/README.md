Dijkstra's Algorithm
Dijkstra's algorithm is used to find the shortest paths from a single source vertex to all other vertices in a graph, where all edge weights are non-negative. It works on the principle of a greedy approach.

Key Steps of Dijkstra's Algorithm:
Initialization:

Set the distance to the source vertex to 0 and the distances to all other vertices to infinity.
Create an empty set of visited vertices.
Use a priority queue to track vertices with the smallest distance.
Main Loop:

Extract the vertex with the smallest distance from the priority queue.
For each neighbor of this vertex, calculate a new possible distance (current distance + weight of the edge to the neighbor).
If the new distance is smaller than the previously recorded distance to this neighbor, update it and add the neighbor to the priority queue.
Mark the current vertex as visited.
Completion:

The process continues until all vertices have been visited or until the destination vertex has been reached (if we are looking for the shortest path to a specific vertex).
