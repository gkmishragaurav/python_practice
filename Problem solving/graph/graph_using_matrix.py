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

    def setVertex(self, id):
        if id < self.num_of_vertices:
            new_vertex = Vertex(id)
            self.vertices.append(new_vertex)

    def getVetex(self, id):
        for i in range(self.num_of_vertices):
            if id == self.vertices[i]:
                return i
        return -1

    def addEdge(self, frm, to):
        self.matrix[frm][to] = 1

    def getEdge(self, frm, to):
        return self.matrix[frm][to]

    def deleteEdge(self, frm, to):
        self.matrix[frm][to] = 0

    def printGraph(self):
        print self.matrix

    def __str__(self):
        return str(self.matrix)


g=Graph(5)
g.setVertex(1)
print str(g)

