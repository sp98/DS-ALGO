"""
"""

class Vertex:
    """ Vertex class """
    def __init__(self, n):
        self.name = n
        self.neighbours = list()
        
        self.color = "black"
        self.distance = 9999

    def add_neighbours(self, n):
        """ Add neighbours to the vertex list"""
        if n not in self.neighbours:
            self.neighbours.append(n)
            self.neighbours.sort()


class Graph:
    """ Graph Class """
    vertices = {}

    def add_vertex(self, v):
        """ Add a new vertex into the graph dict"""
        if isinstance(v, Vertex) and v not in self.vertices.keys():
            self.vertices[v.name] = v
            return True
        else:
            return False

    def add_edge(self, u, v):
        """ Add and edge into the graph """
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key is u:
                    value.add_neighbours(v)
                if key is v:
                    value.add_neighbours(u)
            return True
        else:
            return False

    def display(self):
        """ Display the graph """
        for key in sorted(list(self.vertices.keys())):
            print(key + " : " + str(self.vertices[key].neighbours))

if __name__ == '__main__':
    g = Graph()
    
    # Adding vertices:
    for v in range(ord('A'), ord('K')):
        g.add_vertex(Vertex(chr(v)))

    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH' , 'FG', 'FI', 'FI', 'FJ',
            'GJ', 'HI']
    for edge in edges:
        g.add_edge(edge[:1], edge[1:])

    g.display()
