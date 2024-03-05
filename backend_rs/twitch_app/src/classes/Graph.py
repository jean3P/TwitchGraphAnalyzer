from typing import List, Dict, Generic, TypeVar

NodeId = TypeVar('NodeId')


class Graph(Generic[NodeId]):
    """
    This class allows adding edges between nodes, retrieving adjacent nodes of a given node,
    checking if a node exists in the graph.
    """
    def __init__(self):
        self.graph: Dict[NodeId, List[NodeId]] = {}

    def add_edge(self, source: NodeId, destination: NodeId) -> None:
        if source not in self.graph:
            self.graph[source] = []
        self.graph[source].append(destination)

    def get_adjacent_nodes(self, node: NodeId) -> List[NodeId]:
        return self.graph.get(node, [])

    def __getitem__(self, node: NodeId) -> List[NodeId]:
        return self.get_adjacent_nodes(node)

    def __contains__(self, node: NodeId) -> bool:
        return node in self.graph
