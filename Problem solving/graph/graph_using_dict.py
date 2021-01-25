class Graph:
    def __init__(self, graph_dict=None):
        self._graph_dict = graph_dict

    def vertices(self):
        return list(self._graph_dict.keys())

    def edges(self):
        _edges = []
        for key in self._graph_dict.keys():
            for item in self._graph_dict[key]:
                _edges.append((key, item))
        print(_edges)

    def add_vertex(self, name):
        if not self._graph_dict[name]:
            self._graph_dict[name] = []

    def add_edges(self, name, edge, wt):
        if self._graph_dict[name]:
            if edge not in self._graph_dict[name].keys():
                self._graph_dict[name].append(edge)

    def delete_nbr_edge(self, name, all_nbr):
        # This will delete the edge to the nbr for a given node.
        if self._graph_dict[name]:
            for nbr in all_nbr:
                if nbr in self._graph_dict[name]:
                    self._graph_dict[name].remove(nbr)

    def degree(self):
        '''This denotes number of incoming connections to a node'''
        dg={}
        for item in self._graph_dict.keys():
            dg[item] = 0
            for key in self._graph_dict.keys():
                if item != key:
                    if item in self._graph_dict[key]:
                        dg[item]=dg[item]+1

        return dg

    def find_path(self, start, end, path=None):
        '''This will find the path from start vertex to end vertex if present'''
        if not path:
            path = []

        path.append(start)
        if start == end:
            return path

        if start not in self._graph_dict.keys():
            return None

        else:
            for item in self._graph_dict[start]:
                if item not in path:
                    temp = self.find_path(item, end, path)
                    if temp:
                        return temp

        return None

    def __str__(self):
        return str(self._graph_dict)

    def get_connection(self, key):
        return self._graph_dict(key)

    def dfs(self, start):
        stack=[start]
        visited=[]
        while stack:
            temp=stack.pop() # one difference from BFS is to pop last element here instead of first one
            if temp not in visited:
                visited.append(temp)

                for nbr in self._graph_dict[temp]:
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

                for nbr in self._graph_dict[temp]:
                    if nbr not in visited:
                        stack.append(nbr)

        return visited

    def topological_sort(self):
        pass

    def is_cycle_in_graph(self, start):
        '''Given a directed graph, check whether the graph contains a cycle or not.
        Your function should return true if the given graph contains at least one cycle, else return false.'''
        stack = [start]
        visited = []
        while stack:
            temp=stack.pop()
            if temp not in visited:
                visited.append(temp)

                for nbr in self._graph_dict[temp]:
                    if nbr not in visited:
                        stack.append(nbr)
            else:
                return False
        return True

    def cyclic_to_acyclic(self, start):
        '''To make a cyclic graph to acyclic.'''
        if not self.is_cycle_in_graph(start):
            stack = [start]
            visited = []
            delete_nbr = []
            while stack:
                temp = stack.pop()
                if temp not in visited:
                    visited.append(temp)
                    for nbr in self._graph_dict[temp]:
                        if nbr not in visited:
                            stack.append(nbr)

                        else:
                            delete_nbr.append(nbr)

                    if delete_nbr:
                        self.delete_nbr_edge(temp, delete_nbr)
                    delete_nbr=[]

        else:
            return True


g = { "a" : ["c", "b", "d"],
      "b" : ["d", "c"],
      "c" : ["e"],
      "d" : ["e"],
      "e" : []
      }
graph = Graph(g)
print(str(graph))
# print(graph.find_path('a', 'b'))
# print(graph.dfs('a'))
# print(graph.bfs('a'))
# print(graph.degree())

print(graph.cyclic_to_acyclic('a'))
print(str(graph))

