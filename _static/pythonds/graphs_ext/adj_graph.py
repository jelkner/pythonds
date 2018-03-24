#
#  adj_graph
#
#  Created by Brad Miller on 2005-02-24.
#  Copyright (c) 2005 Brad Miller, David Ranum, Luther College. All rights
#  reserved.
#
class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0
        
    def add_vertex(self, key):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex
    
    def get_vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertices
    
    def add_edge(self, f, t, cost=0):
            if f not in self.vertices:
                nv = self.add_vertex(f)
            if t not in self.vertices:
                nv = self.add_vertex(t)
            self.vertices[f].add_neighbor(self.vertices[t], cost)
    
    def get_vertices(self):
        return list(self.vertices.keys())
        
    def __iter__(self):
        return iter(self.vertices.values())


class Vertex:
    def __init__(self, num):
        self.id = num
        self.connected_to = {}
        self.color = 'white'
        self.distance = sys.maxsize
        self.pred = None
        self.discovery = 0
        self.finish = 0

    # def __lt__(self, o):
    #     return self.id < o.id
    
    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight
        
    def get_connections(self):
        return self.connected_to.keys()
        
    def get_weight(self, nbr):
        return self.connected_to[nbr]
                
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + \
               str(self.disc) + ":fin " + str(self.fin) + ":dist " + \
               str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
