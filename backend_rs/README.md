# Twitch Gamers Social Network Analysis API

This Django-based API provides functionality for analyzing and visualizing the Twitch Gamers Social Network. Utilizing graph algorithms and the Django REST framework, this project offers insights into Twitch's social dynamics through data-driven endpoints.

## Dataset Overview

The project leverages the Twitch Gamers Social Network dataset, a comprehensive collection of Twitch user interactions and relationships. This dataset, assembled from the public API in Spring 2018, features mutual follower connections among Twitch users, forming a single strongly connected component ideal for various analytical tasks.

- **Nodes**: 168,114 (Twitch users)
- **Edges**: 6,797,557 (mutual follower relationships)
- **Density**: 0.0005
- **Transitivity**: 0.0184

For more details about the dataset: [Twitch Gamers Social Network](https://snap.stanford.edu/data/twitch_gamers.html).

## Features

- **Shortest Path Calculation**: Implementing the Breadth-First Search (BFS) algorithm, the API calculates the shortest path between any two nodes (users) in the graph.
- **Graph Data Management**: Upload, list, and manage graph data derived from the Twitch dataset, facilitating easy access to node and edge information for analysis.
- **Visualization Endpoints**: Serve pre-processed data suitable for frontend graph visualization tools, enhancing the interpretability of Twitch's complex social network.

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   ```
2. Navigate to the project directory and install dependencies:
   ```sh
   pip install -r requirements.txt
   ``` 
3. Start the development server:
   ```sh
   python manage.py runserver
   ``` 
   
Access the API at http://localhost:8000.

## Endpoints

### List Graphs
- **Endpoint**: `GET /api/list_graphs/`
- **Description**: Retrieves a list of graphs available for analysis, including basic statistics like the number of nodes and edges.

### Calculate Shortest Path
- **Endpoint**: `POST /api/shortest_path/`
- **Description**: Calculates the shortest path between two nodes using the Breadth-First Search (BFS) algorithm.

## BFS Algorithm Pseudocode

The algorithm explores the graph level by level from the start node, ensuring the shortest path to each reachable node is identified. Below is an abstract representation of the BFS algorithm:

### Algorithm Pseudocode

```plaintext
BFS(Graph, StartNode, GoalNode):
    Initialize an empty set Visited
    Initialize a queue Q and enqueue the tuple (StartNode, [StartNode])

    while Q is not empty:
        currentNode, path <- Q.dequeue()

        for each neighbor of Graph[currentNode]:
            if neighbor == GoalNode:
                return path with neighbor appended  // Shortest path found
            if neighbor not in Visited:
                Add neighbor to Visited
                Enqueue (neighbor, path with neighbor appended) to Q

    return None  // GoalNode is not reachable from StartNode
```