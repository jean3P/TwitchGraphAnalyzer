from dataclasses import dataclass


@dataclass
class Edge:
    source_node_id: int
    destiny_node_id: int
