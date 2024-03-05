import React from 'react';
import Graph from 'react-vis-network-graph';
import './GraphVisualization.css'
import { v4 as uuidv4 } from 'uuid';

const GraphVisualization = ({ graphData, graphOptions, events }) => {
    return (
        <div className="graph-visualization">
            {graphData && (
                <Graph
                    key={uuidv4()}
                    graph={graphData}
                    options={graphOptions}
                    events={events}
                />
            )}
        </div>
    );
};

export default GraphVisualization;
