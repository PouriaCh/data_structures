class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def print_graph(self):
        for vertex, edges in self.adj_list.items():
            print(vertex, " : ", edges)

    def add_vertex(self, vertex):
        if not vertex in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        all_vertices = self.adj_list.keys()
        if v1 in all_vertices and v2 in all_vertices:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        all_vertices = self.adj_list.keys()
        if v1 in all_vertices and v2 in all_vertices and v1 in self.adj_list[v2]:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for edged_vertex in self.adj_list[vertex]:
                self.remove_edge(edged_vertex, vertex)
            del self.adj_list[vertex]
            return True  
        return False


a = Graph()
a.add_vertex("A")
a.add_vertex("B")
a.add_vertex("C")
a.add_vertex("D")

a.print_graph()
print("$$$$$$$$$$$$$$$$$$$$")
a.add_edge("A", "B")
a.add_edge("A", "C")
a.add_edge("C", "B")

a.print_graph()
print("$$$$$$$$$$$$$$$$$$$$")

# a.remove_edge("A", "B")
# print(a.remove_edge("A", "D"))
a.remove_vertex("C")
a.print_graph()
