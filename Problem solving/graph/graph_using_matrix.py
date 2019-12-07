class Vertex:
    def __init__(self, id):
        self.id=id
        self.visited=False

class Graph:
    def __init__(self, num_of_vertices):
        self.matrix = [[0]*num_of_vertices for _ in range(num_of_vertices)]
        self.num_of_vertices=num_of_vertices
        self.vertices=[]
        for i in range(num_of_vertices):
            new_vertex=Vertex(i)
            self.vertices.append(new_vertex)

    def set_Vertex(self, id):
        if id < self.num_of_vertices:
            new_vertex = Vertex(id)
            self.vertices.append(new_vertex)

    def get_Vetex(self, id):
        for i in range(self.num_of_vertices):
            if id == self.vertices[i]:
                return i
        return -1

    def add_edge(self, frm, to):
        self.matrix[frm-1][to-1] = 1

    def get_edge(self, frm, to):
        return self.matrix[frm-1][to-1]

    def delete_Edge(self, frm, to):
        self.matrix[frm-1][to-1] = 0

    def print_Graph(self):
        print self.matrix

    def __str__(self):
        return str(self.matrix)


g=Graph(5)
g.add_edge(1, 4)
g.add_edge(4, 2)
g.add_edge(4, 5)
g.add_edge(2, 5)
g.add_edge(5, 3)

print str(g)

