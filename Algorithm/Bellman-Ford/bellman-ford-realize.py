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
       
     