import pandas as pd
from pathlib import Path
from typing import List, Dict
from dataclasses import asdict
from datetime import datetime
from twitch_app.src.classes.Edge import Edge
from twitch_app.src.classes.TwitchNode import TwitchNode


def read_csv_to_dataframe(file_path: Path) -> pd.DataFrame:
    """Read CSV file into a pandas Dataframe with error handling"""
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading {file_path}:{e}")
        return pd.DataFrame()


def format_datetime(date, date_format='%Y-%m-%d'):
    if isinstance(date, datetime):
        return date.strftime(date_format)
    return date


def parse_features_to_nodes(features_df: pd.DataFrame) -> List[Dict]:
    nodes = []
    for _, row in features_df.iterrows():
        node = TwitchNode(
            numeric_id=int(row["numeric_id"]),
            views=int(row["views"]),
            created_at=row["created_at"],
            updated_at=row["updated_at"],
            mature=int(row["mature"]),
            language=row["language"]
        )
        node_dict = asdict(node)
        node_dict['created_at'] = format_datetime(node.created_at)
        node_dict['updated_at'] = format_datetime(node.updated_at)
        nodes.append(node_dict)
    return nodes


def parse_edges_to_list(edges_df: pd.DataFrame) -> List[Dict]:
    edges = []
    for _, row in edges_df.iterrows():
        edge = Edge(
            source_node_id=int(row["numeric_id_1"]),
            destiny_node_id=int(row["numeric_id_2"])
        )
        edges.append(asdict(edge))
    return edges
