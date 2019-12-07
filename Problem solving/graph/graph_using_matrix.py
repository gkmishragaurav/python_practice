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

    def get_connected(self, id):
        '''Return all non zero index'''
        nbr=[]
        for index in range(len(self.matrix[id-1])):
            if self.matrix[index]:
                nbr.append(index+1)

        return nbr

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

    def dfs(self, start):
        stack=[start]
        visited=[]
        while stack:
            temp=stack.pop() # one difference from BFS is to pop last element here instead of first one
            if temp not in visited:
                visited.append(temp)

                for nbr in self.get_connected(temp):
                    if nbr not in visited:
                        stack.append(nbr)

        return visited

    def bfs(self, start):
        stack=[start]
        visited=[]
        while stack:
            temp=stack.pop(0)
            if temp not in visited:
                visited.append(temp)

                for nbr in self.get_connected(temp):
                    if nbr not in visited:
                        stack.append(nbr)

        return visited


g=Graph(5)
g.add_edge(1, 4)
g.add_edge(1, 3)
g.add_edge(1, 5)
g.add_edge(4, 2)
g.add_edge(4, 5)
g.add_edge(2, 5)
g.add_edge(5, 3)

print str(g)
print g.get_connected(1)
print "dfs", g.dfs(1)
print "bfs",g.bfs(1)

