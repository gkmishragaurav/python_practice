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
        print _edges

    def add_vertex(self, name):
        if not self._graph_dict[name]:
            self._graph_dict[name] = []

    def add_edges(self, name, edge):
        if self._graph_dict[name]:
            if edge not in self._graph_dict[name].keys():
                self._graph_dict[name].append(edge)

    def find_path(self, start, end, path=None):
        '''This will find the path from start vertes to end vertex if present'''
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

g = { "a" : ["d", "f"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : ["d"]
    }
graph = Graph(g)
print str(graph)
print graph.find_path('a', 'b')

