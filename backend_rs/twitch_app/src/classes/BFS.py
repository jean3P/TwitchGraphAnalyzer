from typing import List, TypeVar, Generic, Optional
from collections import deque

from twitch_app.src.classes.Graph import Graph

# Generic type variable for the node identifier

NodeId = TypeVar('NodeId')


class BFS(Generic[NodeId]):
    """
    This class implements the Breadth-First Search algorithm to find the shortest path between two nodes in a graph.
    """
    def __init__(self, graph: Graph[NodeId]):
        self.graph = graph

    def shortest_path(self, start: NodeId, goal: NodeId) -> Optional[List[NodeId]]:
        if start == goal:
            return [start]

        visited = {start}
        queue = deque([(start, [start])])

        while queue:
            current_node, path = queue.popleft()
            for neighbor in self.graph[current_node]:
                if neighbor == goal:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None
