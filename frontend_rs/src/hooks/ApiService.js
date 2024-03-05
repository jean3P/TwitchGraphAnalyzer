import axios from "axios";
import {BASE_API_URL} from "../utils/constants";

export const fetchGraphs = async (setGraphs, setSelectedGraph) => {
    try {
        const response = await axios.get(`${BASE_API_URL}/list_graphs/`);
        const sortedGraphs = response.data.graphs.sort((a, b) => parseInt(a.graph_id, 10) - parseInt(b.graph_id, 10));
        setGraphs(sortedGraphs);
        setSelectedGraph(null); // Reset selected graph upon fetching new list
    } catch (err) {
        console.error('Failed to fetch graphs', err);
    }
};

export const calculateShortestPath = async (
        selectedGraph,
        sourceNode,
        destinationNode,
        setShortestPath,
        setError,
        updateNodeColor,
        setInstructionMessage,
    ) => {
    const url = `${BASE_API_URL}/shortest_path/`;

    console.log('Selected Graph ID:', selectedGraph.graph_id);
    console.log('Source Node:', sourceNode);
    console.log('Destination Node:', destinationNode);

    const data = JSON.stringify({
        graph_id: selectedGraph.graph_id.toString(),
        source_node: sourceNode.toString(),
        destination_node: destinationNode.toString(),
    });

    console.log('Sending data:', data);

    try {
        const response = await axios.post(url, data, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        console.log('Shortest path calculated:', response.data);
        if (response.data.path) {
            setShortestPath(response.data.path);
            setError(""); // Clear any previous errors
            // Update node colors for the shortest path
            response.data.path.forEach((nodeId, index) => {
                // Optionally, keep the source and destination node colors unchanged
                if (nodeId !== sourceNode && nodeId !== destinationNode) {
                    updateNodeColor(nodeId, '#90ee90'); // Light green, for example
                }
            });
            const pathString = response.data.path.join(' -> ');
            setInstructionMessage(`The path is: [${pathString}].`);
        } else {
            setError("No path found");
            setShortestPath([]); // Clear any previous path
            setInstructionMessage("Please select new source and destination nodes.");
        }
    } catch (error) {
        console.error('Failed to calculate shortest path:', error.response ? error.response.data : error);
        setError("Failed to calculate shortest path");
        setInstructionMessage("Please try again.");
    }
};
