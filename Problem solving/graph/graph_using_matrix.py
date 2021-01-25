class Vertex:
    '''This class will define the vertex of the Graph.'''
    def __init__(self, id):
        self.id = id

class Graph:
    '''This class will define the graph it self.'''
    def __init__(self, size):
        self.matrix = [[0]*size for _ in range(size)]
        self.size = size
        self.vertices = []
        for i in range(self.size):
            new_vertex = Vertex(i)
            self.vertices.append(new_vertex)

    def set_vertex(self, vtx_position, id):
        '''
        1. Vertex id to be added in vertices
        2. add id to matrix
        :return:
        '''
        self.vertices[vtx_position] = Vertex(id)

    def get_vertex_from_index(self, index):
        return self.vertices[index].id

    def _get_index(self, id):
        vp = None
        for x in self.vertices:
            if x.id == id:
                vp = self.vertices.index(x)
        return vp

    def add_edge(self, id1, id2, wt):
        vp1 = self._get_index(id1)
        vp2 = self._get_index(id2)
        self.matrix[vp1][vp2] = wt

    def delete_edge(self, id1, id2):
        vp1 = self._get_index(id1)
        vp2 = self._get_index(id2)
        self.matrix[vp1][vp2] = 0

    def get_nbr(self, node):
        nbr = []
        vp = self._get_index(node)
        for element in self.matrix[vp]:
            if element:
                index = self.matrix[vp].index(element)
                nbr.append(self.vertices[index].id)

        return nbr

    def is_cycle_in_graph(self):
        '''Given a directed graph, check whether the graph contains a cycle or not.
        Your function should return true if the given graph contains at least one cycle, else return false.'''
        pass

    def dfs(self, start):
        stack = [start]
        visited = []
        while stack:
            temp = stack.pop()
            if temp not in visited:
                visited.append(temp)

            for nbr in self.get_nbr(temp):
                if nbr not in visited:
                    stack.append(nbr)

        return visited

    def bfs(self, start):
        stack = [start]
        visited = []
        while stack:
            temp = stack.pop(0)
            if temp not in visited:
                visited.append(temp)

            for nbr in self.get_nbr(temp):
                if nbr not in visited:
                    stack.append(nbr)

        return visited

    def print_graph(self):
        print("Printing matrix-")
        for row in range(0, self.size):
            print(self.matrix[row])

g=Graph(5)
# Add vertexes
g.set_vertex(0, 'a')
g.set_vertex(1, 'b')
g.set_vertex(2, 'c')
g.set_vertex(3, 'd')
g.set_vertex(4, 'e')

# Add edges
g.add_edge('a', 'b', 12)
g.add_edge('b', 'c', 9)
g.add_edge('c', 'd', 6)
g.add_edge('d', 'e', 9)
g.add_edge('a', 'c', 6)

g.print_graph()
print(g.dfs('a'))
print(g.bfs('a'))

