class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self,u,v,weight):
        self.edges.append((u,v,weight))


    def bellman_ford(self,start):
        #Initialization of distances to all vertices as infinity 

     distances ={i: float('inf') for i in range(self.vertices)}
     distances[start] = 0

     #Relaxation of edges |V| - 1 times
     for _ in range(self.vertices - 1):
        for u, v, weight in self.edges:
           if distances[u] != float('inf') and distances[u] + weight < distances[v]:
              distances[v] = distances[u] + weight

    
     for u, v, weight in self.edges:
       if distances[u] != float('inf') and distances[u] + weight < distances[v]:
          print("Graph contains a negative weight cycle ")
          return None


     return distances



if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    start_vertex = 0
    distances = g.bellman_ford(start_vertex)

    if distances:
        print("distances from weight", start_vertex)
        for vertex in range(g.vertices):
            print(f"Weight {vertex}: {distances[vertex]}")
       
     