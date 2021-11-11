from typing import Dict, Set, Union

class Graph:
    def __init__(self) -> None:
        self.adj_list: Dict[Union[str, int], Set[Union[str, int]]] = {}

    def print_graph(self) -> None:
        for vertex, edges in self.adj_list.items():
            print(f"{vertex}: {edges}")

    def add_vertex(self, vertex: Union[str, int]) -> bool:
        if vertex in self.adj_list:
            return False
        self.adj_list[vertex] = set()
        return True

    def add_edge(self, vertex1: Union[str, int], vertex2: Union[str, int]) -> bool:
        if vertex1 not in self.adj_list or vertex2 not in self.adj_list:
            return False
        self.adj_list[vertex1].add(vertex2)
        self.adj_list[vertex2].add(vertex1)
        return True     


my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)

print(my_graph.add_edge(0, 1))
print(my_graph.add_edge(2, 3))
print(my_graph.add_edge(1, 2))
print(my_graph.add_edge(1, 2))

my_graph.print_graph()

