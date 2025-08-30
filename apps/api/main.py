from fastapi import FastAPI, UploadFile, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import uuid
from typing import Dict, Any, Optional

app = FastAPI(title="Binaai API", version="0.1.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class RunCreate(BaseModel):
    pipeline_id: str

class PipelineCreate(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    nodes: list = []
    edges: list = []

class ExportRequest(BaseModel):
    pipeline_id: str
    input_media_url: str
    output_format: str = "mp4"
    duration: Optional[int] = None

# In-memory database (replace with proper DB in production)
DB: Dict[str, Dict[str, Any]] = {
    "pipelines": {},
    "runs": {}
}

@app.get("/healthz")
def healthz():
    """Health check endpoint"""
    return {"ok": True, "service": "binaai-api", "version": "0.1.0"}

@app.post("/v0/pipelines")
def create_pipeline(pipeline: PipelineCreate):
    """Create a new pipeline"""
    pid = pipeline.id or str(uuid.uuid4())
    DB["pipelines"][pid] = {
        "id": pid,
        "name": pipeline.name,
        "description": pipeline.description,
        "nodes": pipeline.nodes,
        "edges": pipeline.edges,
        "created_at": "2024-01-01T00:00:00Z"  # Placeholder
    }
    return {"id": pid}

@app.get("/v0/pipelines/{pid}")
def get_pipeline(pid: str):
    """Get pipeline by ID"""
    pipeline = DB["pipelines"].get(pid)
    if not pipeline:
        return {"error": "Pipeline not found"}
    return pipeline

@app.post("/v0/pipelines/{pid}/runs")
def create_run(pid: str, body: RunCreate):
    """Create a new run for a pipeline"""
    if pid not in DB["pipelines"]:
        return {"error": "Pipeline not found"}
    
    rid = str(uuid.uuid4())
    DB["runs"][rid] = {
        "id": rid,
        "pipeline_id": pid,
        "status": "queued",
        "progress": 0,
        "created_at": "2024-01-01T00:00:00Z"  # Placeholder
    }
    return {"run_id": rid}

@app.get("/v0/runs/{rid}")
def get_run(rid: str):
    """Get run status by ID"""
    run = DB["runs"].get(rid)
    if not run:
        return {"error": "Run not found"}
    return run

@app.post("/v0/upload-url")
def upload_url():
    """Generate signed upload URL (placeholder implementation)"""
    # In production, this would generate a real Supabase signed URL
    return {
        "url": "https://example.com/presigned",
        "fields": {},
        "upload_id": str(uuid.uuid4())
    }

@app.post("/v0/export")
def export_video(request: ExportRequest, bg: BackgroundTasks):
    """Export processed video"""
    rid = str(uuid.uuid4())
    
    def do_export():
        # Simulate processing time
        import time
        time.sleep(2)  # Mock processing
        
        # Update run status
        DB["runs"][rid] = {
            "id": rid,
            "pipeline_id": request.pipeline_id,
            "status": "completed",
            "progress": 100,
            "artifact_url": "https://example.com/processed-video.mp4",
            "created_at": "2024-01-01T00:00:00Z"
        }
    
    # Add background task
    bg.add_task(do_export)
    
    # Initialize run as processing
    DB["runs"][rid] = {
        "id": rid,
        "pipeline_id": request.pipeline_id,
        "status": "processing",
        "progress": 0,
        "created_at": "2024-01-01T00:00:00Z"
    }
    
    return {"run_id": rid, "status": "processing"}

@app.get("/v0/pipelines")
def list_pipelines():
    """List all pipelines"""
    return {"pipelines": list(DB["pipelines"].values())}

@app.get("/v0/runs")
def list_runs():
    """List all runs"""
    return {"runs": list(DB["runs"].values())}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
