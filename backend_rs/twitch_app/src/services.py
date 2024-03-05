import os
from pathlib import Path
from typing import Set, Dict, Any, Optional, List
from .classes.BFS import BFS
from .classes.Graph import Graph
from .data_access import read_csv_to_dataframe, parse_features_to_nodes, parse_edges_to_list


def get_graph_ids(directory: Path) -> Set[str]:
    """Extract unique graph identifiers based on CSV filenames."""
    return {filename.split("_")[1].split('.')[0] for filename in os.listdir(directory)}


def build_graph_data(graph_id: str, graphs_dir: Path) -> Dict[str, Any]:
    """Construct graph data from features and edges CSV files."""

    features_path = graphs_dir / f'features_{graph_id}.csv'
    edges_path = graphs_dir / f'edges_{graph_id}.csv'
    graph_data: Dict[str, Any] = {'graph_id': graph_id}

    if features_path.is_file() and edges_path.is_file():
        features_df = read_csv_to_dataframe(features_path)
        edges_df = read_csv_to_dataframe(edges_path)

        graph_data['features'] = parse_features_to_nodes(features_df) if not features_df.empty else []
        graph_data['edges'] = parse_edges_to_list(edges_df) if not edges_df.empty else []

    return graph_data


def calculate_shortest_path(graph: Graph[int], source_node: int, destination_node: int) -> Optional[List[int]]:
    bfs = BFS(graph)
    return bfs.shortest_path(source_node, destination_node)
