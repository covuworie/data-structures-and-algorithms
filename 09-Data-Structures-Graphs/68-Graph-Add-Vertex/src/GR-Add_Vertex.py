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


my_graph = Graph()

print(my_graph.add_vertex('A'))
print(my_graph.add_vertex('A'))

my_graph.print_graph()

