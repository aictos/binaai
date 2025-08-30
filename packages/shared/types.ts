// Pipeline Types
export interface PipelineNode {
  id: string;
  type: 'input' | 'output' | 'processor';
  data: {
    label: string;
    [key: string]: any;
  };
  position: {
    x: number;
    y: number;
  };
}

export interface PipelineEdge {
  id: string;
  source: string;
  target: string;
  animated?: boolean;
}

export interface Pipeline {
  id: string;
  name: string;
  description?: string;
  nodes: PipelineNode[];
  edges: PipelineEdge[];
  created_at: string;
}

// Run Types
export type RunStatus = 'queued' | 'processing' | 'completed' | 'failed';

export interface Run {
  id: string;
  pipeline_id: string;
  status: RunStatus;
  progress: number;
  artifact_url?: string;
  error_message?: string;
  created_at: string;
}

// API Request/Response Types
export interface CreatePipelineRequest {
  id?: string;
  name: string;
  description?: string;
  nodes: PipelineNode[];
  edges: PipelineEdge[];
}

export interface CreateRunRequest {
  pipeline_id: string;
}

export interface ExportRequest {
  pipeline_id: string;
  input_media_url: string;
  output_format?: string;
  duration?: number;
}

export interface UploadUrlResponse {
  url: string;
  fields: Record<string, string>;
  upload_id: string;
}

// Node Processor Types
export interface YOLODetection {
  class_id: number;
  class_name: string;
  confidence: number;
  bbox: [number, number, number, number]; // [x, y, width, height]
}

export interface BlazePoseLandmark {
  x: number;
  y: number;
  z?: number;
  visibility?: number;
}
