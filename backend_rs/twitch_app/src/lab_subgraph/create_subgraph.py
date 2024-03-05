import pandas as pd
import networkx as nx
from itertools import islice

from twitch_app.src.lab_subgraph.paths import large_twitch_features, large_twitch_edges, outputs_path

# Load dataset
features_df = pd.read_csv(large_twitch_features)
relationships_df = pd.read_csv(large_twitch_edges)


# Function to create a graph and extract subgraphs with N nodes
def create_graph_and_extract(features_df, relationships_df, n):
    """
    Create a graph from the relationships and extract a subgraph with N nodes.
    """
    # Create a graph from the relationships
    G = nx.from_pandas_edgelist(relationships_df, 'numeric_id_1', 'numeric_id_2')

    # Extract subgraph with N nodes
    nodes_subset = list(islice(G.nodes, n))
    subgraph = G.subgraph(nodes_subset)

    # Extract features for the nodes in the subgraph
    features_subset_df = features_df[features_df['numeric_id'].isin(nodes_subset)]

    # Save the features to a CSV file
    features_subset_df.to_csv(f'{outputs_path}/features_{n}.csv', index=False)

    # Extract and save edges of the subgraph
    edges_df = pd.DataFrame(list(subgraph.edges), columns=['numeric_id_1', 'numeric_id_2'])
    edges_df.to_csv(f'{outputs_path}/edges_{n}.csv', index=False)

    return subgraph


for node_count in [50, 75, 100]:
    subgraph = create_graph_and_extract(features_df, relationships_df, node_count)
    print(f"Created and saved features and relationships for graph with {node_count} nodes.")
