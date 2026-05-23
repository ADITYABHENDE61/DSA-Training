# { A:[B,C,D],
#   B:[A,E],
#   C:[A,D],
#   D:[A,C,E]
    # E:[B,D]
#   }
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            return True
        return False
    
    def remove_vertex(self,vertex):
        if vertex in self.adjacency_list.keys():
            del self.adjacency_list[vertex]
            for other_vertex in self.adjacency_list:
                self.adjacency_list[other_vertex] = [v for v in self.adjacency_list[other_vertex] if v != vertex]
            return True
        return False

my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")
# my_graph.print_graph()
my_graph.add_edge("A","B")
my_graph.add_edge("A","C")
my_graph.add_edge("A","D")
my_graph.add_edge("B","A")
my_graph.add_edge("B","E")
my_graph.add_edge("C","A")
my_graph.add_edge("C","D")
my_graph.add_edge("D","A")
my_graph.add_edge("D","C")
my_graph.add_edge("D","E")
my_graph.add_edge("E","B")
my_graph.add_edge("E","D")



my_graph.print_graph()


