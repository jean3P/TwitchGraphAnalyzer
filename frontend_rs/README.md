# Twitch Gamers Social Network Visualization

This React application serves as the frontend for visualizing the Twitch Gamers Social Network. It interacts with a Django REST API to fetch graph data and calculate the shortest paths between nodes, enabling users to explore Twitch's complex social dynamics through an intuitive interface.

## Features

- **Graph Visualization**: Utilize `react-vis-network-graph` to display the Twitch Gamers Social Network, allowing users to visually navigate through nodes (users) and edges (mutual relationships).
- **Shortest Path Calculation**: Provides functionality to select any two nodes within the graph and compute the shortest path between them, highlighting the path within the visualization.
- **Dynamic Data Fetching**: Seamlessly integrates with the backend API to fetch the latest graph data and updates the visualization accordingly.
- **Interactive UI**: Offers an interactive user interface for selecting nodes and initiating graph-based operations like shortest path calculation.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Node.js (Preferably the latest LTS version)
- npm (Comes with Node.js)

### Installation

1. **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install Dependencies**
    ```bash
    npm install
    ```

3. **Start the Development Server**
    ```bash
    npm start
    ```
   This will launch the app in the development mode.\
   Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

### Usage

After starting the application, navigate through the interactive UI to explore the Twitch Gamers Social Network. The application facilitates:

- **Graph Visualization**: Dynamically visualize Twitch users and their connections.
- **Shortest Path Discovery**: Select two nodes and calculate the shortest path between them.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
