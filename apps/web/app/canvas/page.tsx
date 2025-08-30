'use client';

import { useCallback, useState } from 'react';
import {
  ReactFlow,
  Node,
  Edge,
  addEdge,
  Connection,
  useNodesState,
  useEdgesState,
  Controls,
  Background,
} from '@xyflow/react';
import '@xyflow/react/dist/style.css';

const initialNodes: Node[] = [
  { 
    id: '1', 
    data: { label: 'Media In' }, 
    position: { x: 50, y: 50 }, 
    type: 'input' 
  },
  { 
    id: '2', 
    data: { label: 'ObjectDetect (YOLO)' }, 
    position: { x: 250, y: 50 },
    type: 'default'
  },
  { 
    id: '3', 
    data: { label: 'PoseEstimate (BlazePose*)' }, 
    position: { x: 450, y: 50 },
    type: 'default'
  },
];

const initialEdges: Edge[] = [
  { 
    id: 'e1-2', 
    source: '1', 
    target: '2', 
    animated: false 
  },
  { 
    id: 'e2-3', 
    source: '2', 
    target: '3', 
    animated: false 
  }
];

export default function Canvas() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect = useCallback(
    (params: Connection) => setEdges((eds) => addEdge(params, eds)),
    [setEdges]
  );

  return (
    <main className="h-[80vh] p-4">
      <div className="h-full border rounded bg-gray-50">
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          onConnect={onConnect}
          fitView
        >
          <Controls />
          <Background />
        </ReactFlow>
      </div>
    </main>
  );
}
