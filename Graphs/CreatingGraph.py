class Vertex:                              #Define a Vertex class. 
    def __init__(self, key):            #Vertex class has 2 instance variables: self.key & self.connections. First variable represents vertex's key while second variable is a dictionary storing vertices each vertex is adjacent to.
        self.key = key
        self.connections = {}

    def add_adj(self, vertex, weight = 0):  #Method called add_adj that accepts a vertex as parameter and makes it adjacent to vertex you called the method on by adding connection to self.connections. 
        self.connection[vertex] = weight    #The method also accepts a weight as a parameter if you want to add a weight to the relationship.

    def get_connections(self):
        return self.connections.keys()
    
    def get_weight(self,vertex):
        return self.connections[vertex]
    
    class Graph:            #Define a class called Graph. Graph has an instance variable self.vertex_dict that stores the vertices in each graph.
        def __init__(self):
            self.vertex_dict = {}

        def add_vertex(self, key):      #Method add_vertex adds a new vertex to a graph by first creating a vertex and then mapping the key the user passes in as a parameter to the new vertex inside self.vertex_dict.
            new_vertex = Vertex(key)
            self.vertex_dict[key] = new_vertex

        def get_vertex(self, key):          #Method called get_vertex accepts a key as a parameter and checks self.vertex_dict to see if the vertex is your graph
            if key in self.vertex_dict:
                return self.vertex_dict[key]
            return None
        
        def add_edge(self, f, t, weight = 0):   #Method called add_edge that adds an edge between two vertices in your graph.
            if f not in self.vertex_dict:
                self.add_vertex(f)
            if t not in self.vertex_dict:
                self.add_vertex(t)
            self.vertex_dict[f].add_adj(self.vertex_dict[t], weight)