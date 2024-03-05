import React, { useState } from 'react';
import './App.css';
import {calculateShortestPath, fetchGraphs} from "./hooks/ApiService";
import GraphVisualization from "./components/GraphVisualization";


function App() {
  const [graphs, setGraphs] = useState([]);
  const [selectedGraph, setSelectedGraph] = useState(null);
  const [sourceNode, setSourceNode] = useState(null);
  const [destinationNode, setDestinationNode] = useState(null);
  const [shortestPath, setShortestPath] = useState([]);
  const [error, setError] = useState("");
  const [nodeColors, setNodeColors] = useState({}); // New state to track node colors
  const [instructionMessage, setInstructionMessage] = useState("Please select a source node.");

  const handleFetchGraphsClick = () => {
    fetchGraphs(setGraphs, setSelectedGraph)
        .catch((error) => {
          console.error('Failed to fetch graphs:', error);
        });
  };

  const handleCalculateShortestPathClick = () => {
    calculateShortestPath(selectedGraph, sourceNode, destinationNode, setShortestPath, setError, updateNodeColor, setInstructionMessage)
        .catch((error) => {
          console.error('Failed to calculate shortest path:', error);
        });
  };

  const updateNodeColor = (nodeId, color) => {
    setNodeColors(prev => ({ ...prev, [nodeId]: color }));
  };

  const isEdgeInShortestPath = (edge, shortestPath) => {
    return shortestPath.includes(edge.source_node_id) && shortestPath.includes(edge.destiny_node_id);
  };


  // Graph configuration
  const graphData = selectedGraph ? {
    nodes: selectedGraph.features.map(node => ({
      id: node.numeric_id.toString(),
      label: `${node.numeric_id}`,
      title: `Views: ${node.views} | Created: ${node.created_at} | Updated: ${node.updated_at} | Language: ${node.language}`,
      color: nodeColors[node.numeric_id.toString()] || '#D2E5FF',
      fixed: true,
    })),
    edges: selectedGraph.edges.map(edge => {
      const inShortestPath = isEdgeInShortestPath(edge, shortestPath);
      return {
        from: edge.source_node_id.toString(),
        to: edge.destiny_node_id.toString(),
        color: inShortestPath ? '#ff0000' : '#000000', // Red for edges in the shortest path, black for others
        width: inShortestPath ? 3 : 1, // Thicker edges for those in the shortest path
      };
    })
  } : null;

  const graphOptions = {
    autoResize: true,
    height: '500px',
    width: '100%',
    manipulation: false,
    edges: {
      arrows: {
        to: false,
      },
    },
    physics: {
      enabled: false,
    },
  };

  // Defining the behaviour of the Graph
  const events = {
    select: function(event) {
      const {nodes} = event;
      const selectedNodeId = nodes[0]
      if (!sourceNode && (!destinationNode || selectedNodeId !== destinationNode)) {
        setSourceNode(selectedNodeId);
        updateNodeColor(selectedNodeId, 'orange');
        console.log("Source node set to:", selectedNodeId);
        setInstructionMessage("Please select a destination node.");
      } else if (!destinationNode && selectedNodeId !== sourceNode) {
        setDestinationNode(selectedNodeId);
        updateNodeColor(selectedNodeId, 'yellow');
        console.log("Destination node set to:", selectedNodeId);
        setInstructionMessage("Nodes selected. You may now calculate the shortest path or reset.");
      }
    }
  };

  const resetSelection = () => {
    setSourceNode(null);
    setDestinationNode(null);
    setNodeColors({});
    setShortestPath([]); // Reset shortest path
    setError(""); // Clear any errors
    setInstructionMessage("Please select a source node.");
  };

  return (
      <div className="App">
        <header className="App-header">
          <h1>Graph Visualization</h1>
          <button onClick={handleFetchGraphsClick} className="fetch-graphs">Fetch Graphs</button>
          <div className="tabs">
            {graphs.length > 0 ? (
                graphs.map((graph) => (
                    <button
                        key={graph.graph_id}
                        className={`tab ${selectedGraph && graph.graph_id === selectedGraph.graph_id ? 'active' : ''}`}
                        onClick={() => {
                          resetSelection();
                          setSelectedGraph(graph)
                        }}
                    >
                      Graph {graph.graph_id} Nodes
                    </button>
                ))
            ) : (
                <p>No graphs loaded. Click "Fetch Graphs" to load.</p>
            )}
          </div>

          {graphs.length > 0 && selectedGraph && shortestPath !== [] && (
              <p className="instruction-message">{instructionMessage}</p> // Conditionally display instruction message
          )}

          {graphData && (
              <GraphVisualization
                  graphData={graphData}
                  graphOptions={graphOptions}
                  events={events}
              />
          )}
          <div className="node-selection">
            {sourceNode && <p className="node-info">Source Node: {sourceNode}</p>}
            {destinationNode && <p className="node-info">Destination Node: {destinationNode}</p>}
            {sourceNode && destinationNode && (
                <>
                  <button className="action-button calculate-path-button" onClick={handleCalculateShortestPathClick}> Shortest Path (BFS)
                  </button>
                  <button className="action-button reset-button" onClick={resetSelection}>Reset</button>
                </>
            )}
          </div>
          <div className="error-dialog">
            {error && <p>{error}</p>}
          </div>
        </header>
      </div>
  );
}

export default App;