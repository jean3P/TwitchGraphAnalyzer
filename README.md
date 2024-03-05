# TwitchGraphAnalyzer

TwitchGraphAnalyzer is an interactive platform designed for analyzing the Twitch streamer networks. It combines the robust backend capabilities of Django with the dynamic and responsive frontend provided by React. This solution offers users the ability to visualize network graphs, calculate the shortest path between streamers, and preprocess data for deeper insights into the Twitch streaming community.

## System Workflow

The platform operates through a series of user interactions, facilitated by the React frontend and processed by the Django backend. Here's an overview of the workflow:

1. **Fetch Graphs**: Users initiate a request to view available network graphs by clicking the "Fetch Graphs" button. The React app sends a request to the Django backend, which retrieves the list of graphs from the database and returns it to the frontend. The available graphs are then displayed to the user.

2. **Select Graph**: Upon displaying the graph list, users can select a specific graph for analysis. The UI updates to show the selected graph.

3. **Set Source and Destination Nodes**: Users choose a source node and a destination node within the graph for which they wish to calculate the shortest path. The UI updates to highlight the selected nodes.

4. **Calculate Shortest Path**: With both nodes selected, users request the calculation of the shortest path by clicking the "Calculate Path" button. This sends a request to the backend, which executes the shortest path algorithm and returns the path to the frontend. The React app then updates the visualization to display this path.

## Running with Docker Compose

The application is containerized using Docker, simplifying deployment and ensuring consistent environments across development and production. Docker Compose orchestrates the containers for both the frontend and backend services.

### Prerequisites

- Docker
- Docker Compose

### Steps to Run

1. Clone the project repository to your local machine.
2. Navigate to the project root directory.
3. Execute the following command to start the application:

    ```bash
    docker-compose up --build
    ```

    This command builds the Docker images for both services if necessary and starts the containers.

4. Access the React frontend at `http://localhost:3000` and the Django backend at `http://localhost:8000`.

5. To stop the application and remove the containers, use the following command:

    ```bash
    docker-compose down
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
