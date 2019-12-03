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
        pass

    def getVetex(self, id):
        pass

    def addEdge(self, frm, to):
        pass

    def getEdge(self):
        pass

    def deleteEdge(self, frm, to):
        pass

    def printGraph(self):
        pass



